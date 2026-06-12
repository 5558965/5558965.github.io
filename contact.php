<?php
header('Content-Type: application/json; charset=utf-8');

// Start session for CSRF token validation
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// If Composer autoload exists, require it to enable PHPMailer installation
$autoload = __DIR__ . '/vendor/autoload.php';
if (file_exists($autoload)) {
    require_once $autoload;
}

$response = [
    'isSuccess' => false,
    'nameError' => '',
    'emailError' => '',
    'subjectError' => '',
    'messageError' => ''
];

// Simple file-based rate limit (per IP) — max 5 submissions per 60 seconds
$rateLimitDir = sys_get_temp_dir() . '/portfolio_rate';
if (!is_dir($rateLimitDir)) {
    @mkdir($rateLimitDir, 0700, true);
}

$clientIp = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$rateFile = $rateLimitDir . '/' . preg_replace('/[^a-z0-9_\-\.]/i', '_', $clientIp) . '.log';
$timestamps = [];
if (file_exists($rateFile)) {
    $timestamps = array_filter(array_map('intval', explode("\n", trim(@file_get_contents($rateFile)))));
}
$now = time();
$timestamps = array_filter($timestamps, function($t) use ($now) { return ($now - $t) < 60; });
if (count($timestamps) >= 5) {
    $response['messageError'] = 'Trop de tentatives. Veuillez réessayer plus tard.';
    echo json_encode($response);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // CSRF token validation
    $postedToken = $_POST['csrf_token'] ?? '';
    $sessionToken = $_SESSION['csrf_token'] ?? '';
    if (!$postedToken || !$sessionToken || !hash_equals($sessionToken, $postedToken)) {
        $response['messageError'] = 'Jeton CSRF invalide. Veuillez recharger la page.';
        echo json_encode($response);
        exit;
    }
    // Basic sanitization
    $name = substr(trim($_POST['name'] ?? ''), 0, 200);
    $email = trim($_POST['email'] ?? '');
    $subject = substr(trim($_POST['subject'] ?? ''), 0, 200);
    $message = trim($_POST['message'] ?? '');

    // Prevent header injection by removing CRLF
    $name = str_replace(["\r", "\n"], ' ', $name);
    $subject = str_replace(["\r", "\n"], ' ', $subject);

    if ($name === '') {
        $response['nameError'] = 'Veuillez saisir votre nom.';
    }

    if ($email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $response['emailError'] = 'Veuillez saisir une adresse email valide.';
    }

    if ($subject === '') {
        $response['subjectError'] = 'Veuillez saisir un sujet.';
    }

    if ($message === '') {
        $response['messageError'] = 'Veuillez saisir un message.';
    }

    if (
        empty($response['nameError']) &&
        empty($response['emailError']) &&
        empty($response['subjectError']) &&
        empty($response['messageError'])
    ) {
        // Destination address should be configured via env var
        $to = getenv('CONTACT_TO_ADDRESS') ?: 'contact@exemple.com';

        $body = "Nom: $name\nEmail: $email\nSujet: $subject\nMessage:\n$message";

        $sendOk = false;

        // If PHPMailer is available, prefer SMTP (not bundled here)
        if (class_exists('PHPMailer\PHPMailer\PHPMailer')) {
            try {
                $mail = new PHPMailer\PHPMailer\PHPMailer(true);
                // Configure SMTP from env if provided
                $smtpHost = getenv('SMTP_HOST');
                if ($smtpHost) {
                    $mail->isSMTP();
                    $mail->Host = $smtpHost;
                    $mail->Port = getenv('SMTP_PORT') ?: 587;
                    $mail->SMTPAuth = true;
                    $mail->Username = getenv('SMTP_USER');
                    $mail->Password = getenv('SMTP_PASS');
                    $mail->SMTPSecure = getenv('SMTP_SECURE') ?: 'tls';
                }
                $from = getenv('MAIL_FROM_ADDRESS') ?: $email;
                $fromName = getenv('MAIL_FROM_NAME') ?: $name;
                $mail->setFrom($from, $fromName);
                $mail->addAddress($to);
                $mail->Subject = $subject;
                $mail->Body = $body;
                $mail->send();
                $sendOk = true;
            } catch (\Exception $e) {
                $response['emailError'] = 'Erreur en envoyant le message (mailer).';
            }
        } else {
            // Fallback to mail() if available
            if (function_exists('mail')) {
                // Build safe headers
                $safeFrom = filter_var($email, FILTER_SANITIZE_EMAIL);
                $headers = 'From: ' . $safeFrom . "\r\n" . 'Reply-To: ' . $safeFrom . "\r\n" . 'X-Mailer: PHP/' . phpversion();
                $sendOk = @mail($to, $subject, $body, $headers);
                if (!$sendOk) {
                    $response['emailError'] = 'Impossible d\'envoyer le message pour le moment.';
                }
            } else {
                $response['emailError'] = 'Le serveur n\'est pas configuré pour l\'envoi d\'emails. Configurez SMTP ou installez PHPMailer.';
            }
        }

        if ($sendOk) {
            $response['isSuccess'] = true;
            // record timestamp for rate limiting
            $timestamps[] = $now;
            @file_put_contents($rateFile, implode("\n", $timestamps));
        }
    }
}

echo json_encode($response);