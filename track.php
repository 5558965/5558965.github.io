<?php
/**
 * track.php — Notification Telegram à chaque visite du portfolio
 * 
 * Configuration :
 *   TELEGRAM_BOT_TOKEN  → token du bot (via env ou constante ci-dessous)
 *   TELEGRAM_CHAT_ID    → ton chat ID personnel
 */

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');

// ─── CONFIGURATION ──────────────────────────────────────────────
// Préférence : variables d'environnement (plus sécurisé)
// Sinon, remplace les chaînes vides par tes valeurs directement.
$botToken = getenv('TELEGRAM_BOT_TOKEN') ?: '8729026440:AAEgfIN9kUH-W8pEWlXJfXFj306a8g-CQMo';
$chatId   = getenv('TELEGRAM_CHAT_ID')   ?: '6103078174';
// ────────────────────────────────────────────────────────────────

// Vérification de configuration
if ($botToken === 'REMPLACE_PAR_TON_TOKEN' || $chatId === 'REMPLACE_PAR_TON_CHAT_ID') {
    http_response_code(503);
    echo json_encode(['error' => 'Bot non configuré']);
    exit;
}

// ─── RATE LIMITING ──────────────────────────────────────────────
// Max 1 notification par IP toutes les 30 minutes (évite le spam)
$rateLimitDir = sys_get_temp_dir() . '/portfolio_track';
if (!is_dir($rateLimitDir)) {
    @mkdir($rateLimitDir, 0700, true);
}

$clientIp  = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
// Ignore les pings internes (localhost)
if (in_array($clientIp, ['127.0.0.1', '::1'])) {
    echo json_encode(['status' => 'ignored', 'reason' => 'localhost']);
    exit;
}

$safeIp    = preg_replace('/[^a-z0-9_\-\.]/i', '_', $clientIp);
$rateFile  = $rateLimitDir . '/' . $safeIp . '.visit';
$cooldown  = 1800; // 30 minutes en secondes

if (file_exists($rateFile)) {
    $lastVisit = (int) @file_get_contents($rateFile);
    if ((time() - $lastVisit) < $cooldown) {
        echo json_encode(['status' => 'throttled']);
        exit;
    }
}
@file_put_contents($rateFile, time());

// ─── COLLECTE DES INFOS VISITEUR ────────────────────────────────
$userAgent = $_SERVER['HTTP_USER_AGENT'] ?? 'Inconnu';
$referer   = $_SERVER['HTTP_REFERER']    ?? 'Accès direct';
$language  = $_SERVER['HTTP_ACCEPT_LANGUAGE'] ?? 'Inconnu';
$page      = $_POST['page'] ?? $_GET['page'] ?? '/';
$date      = date('d/m/Y à H:i:s', time());

// Détection simple du type d'appareil
$device = 'Ordinateur 🖥️';
if (preg_match('/Mobile|Android|iPhone|iPad/i', $userAgent)) {
    $device = 'Mobile 📱';
} elseif (preg_match('/Tablet|iPad/i', $userAgent)) {
    $device = 'Tablette 📲';
}

// Détection du navigateur
$browser = 'Inconnu';
if (preg_match('/Chrome\/(\d+)/i', $userAgent, $m))      $browser = 'Chrome ' . $m[1];
elseif (preg_match('/Firefox\/(\d+)/i', $userAgent, $m)) $browser = 'Firefox ' . $m[1];
elseif (preg_match('/Safari\/(\d+)/i', $userAgent, $m))  $browser = 'Safari';
elseif (preg_match('/Edge\/(\d+)/i', $userAgent, $m))    $browser = 'Edge ' . $m[1];

// Géolocalisation IP (service gratuit, sans clé API)
$country = 'Inconnu';
$city    = 'Inconnu';
$geo = @file_get_contents("https://ipapi.co/{$clientIp}/json/");
if ($geo) {
    $geoData = json_decode($geo, true);
    if (isset($geoData['country_name'])) $country = $geoData['country_name'];
    if (isset($geoData['city']))         $city    = $geoData['city'];
}

// ─── CONSTRUCTION DU MESSAGE ─────────────────────────────────────
$message = "👀 *Nouvelle visite sur ton portfolio !*\n\n"
         . "📅 *Date :* {$date}\n"
         . "🌍 *Localisation :* {$city}, {$country}\n"
         . "🌐 *IP :* `{$clientIp}`\n"
         . "📲 *Appareil :* {$device}\n"
         . "🔍 *Navigateur :* {$browser}\n"
         . "🗣️ *Langue :* {$language}\n"
         . "🔗 *Référent :* {$referer}\n"
         . "📄 *Page :* {$page}";

// ─── ENVOI TELEGRAM ──────────────────────────────────────────────
$url     = "https://api.telegram.org/bot{$botToken}/sendMessage";
$payload = json_encode([
    'chat_id'    => $chatId,
    'text'       => $message,
    'parse_mode' => 'Markdown',
]);

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => $payload,
    CURLOPT_HTTPHEADER     => ['Content-Type: application/json'],
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 5,
]);
$result = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$response = json_decode($result, true);

if ($httpCode === 200 && isset($response['ok']) && $response['ok']) {
    echo json_encode(['status' => 'ok', 'message' => 'Notification envoyée']);
} else {
    http_response_code(500);
    echo json_encode(['status' => 'error', 'detail' => $response['description'] ?? 'Erreur inconnue']);
}
