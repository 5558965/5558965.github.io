<?php 
$firstname = $name = $email = $phone = $message = "";
$firstnameError = $nameError = $emailError = $phoneError = $messageError = "";
$isSuccess = false;
$emailTo = "abdoulrazakkouame@gmail.com";


if ($_SERVER["REQUEST_METHOD"] == "POST") 
{
    $firstname = verifyInput($_POST["firstname"]);
    $name = verifyInput($_POST["name"]);
    $email = verifyInput($_POST["email"]);
    $phone = verifyInput($_POST["phone"]);
    $message = verifyInput($_POST["message"]);
    $isSuccess = true;
    $emailText = "";

    if (empty($firstname)) {
        $firstnameError = "Je veux connaitre ton prénom !";
        $isSuccess = false;
    } else {
        $emailText .= "Firstname: $firstname\n";
    }
    
    if (empty($name)) {
        $nameError = "Et oui je veux tout savoir. Même ton nom !";
        $isSuccess = false;
    } else { 
        $emailText .= "Name: $name\n";
    }
    
    if (!isEmail($email)) {
        $emailError = "T'essaies de me rouler ? C'est pas un email ça !";
        $isSuccess = false;
    } else {
        $emailText .= "Email: $email\n";
    }
    
    if (!isPhone($phone)) {
        $phoneError = "Que des chiffres et des espaces, stp...";
        $isSuccess = false;
    } else { 
        $emailText .= "Phone: $phone\n";
    }
    
    if (empty($message)) {
        $messageError = "Qu'est-ce que tu veux me dire ?";
        $isSuccess = false;
    } else { 
        $emailText .= "Message: $message\n";
    }
    
    if ($isSuccess) {
        $headers = "From: $firstname $name <$email>\r\nReply-To: $email";
        mail($emailTo, "Un message de votre site", $emailText, $headers);
        $firstname = $name = $email = $phone = $message = "";
    }
}

function isPhone($var) {
    return preg_match("/^[0-9 ]*$/", $var);
}

function isEmail($var) {
    return filter_var($var, FILTER_VALIDATE_EMAIL);
}

function verifyInput($var) {
    $var = trim($var);
    $var = stripslashes($var);
    $var = htmlspecialchars($var);
    return $var; 
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>CV Claver </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link href='http://fonts.googleapis.com/css?family=Lato' rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="./style.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="js/script.js"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body data-spy="scroll" data-target="navbar" data-offset="60px">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container">
            <a class="navbar-brand" href="#"></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="">
                <div class="navbar-nav">
                    <a class="nav-link" href="#about">Moi</a>
                    <a class="nav-link" href="#skills">Competences</a>
                    <a class="nav-link" href="#experience">Experiences</a>
                    <a class="nav-link" href="#education">Education</a>
                    <a class="nav-link" href="#portfolio">Portfolio</a>
                    <a class="nav-link" href="#projects">Projects</a>
                    <a class="nav-link" href="#recommendations">Recommendations</a>
                    <a class="nav-link" href="#contact">Contact</a>
                </div>
            </div>
        </div>
    </nav>
    <section id="about" class="container-fluid">
        <div class="col-xs-8 col-md-4 profile-picture">
            <img src="images/CLAVER.jpg" alt="CLAVER" class="img-circle">
        </div>
        <div class="heading">
            <h1>Hello, c'est moi Claver</h1>
            <h3>Développeur Web</h3>
            <a href="docs/CLAVER-CV.pdf" class="button1">Télécharger CV</a>
        </div>
    </section>
    <section id="skills">
       <div class="red-divider"></div>
       <div class="heading">
           <h2>Competences</h2>
    </div>
    <div class="container">
         <div class="row">
            <div class="col-md-6">
                 <div class="progress">
                      <div class="progress-bar"
role="progressbar" aria-valuenow="85" aria-aria-valuemin="0"aria-
valuemax="100" style="width: 85%">
                                 <h5>PYTHON & SQL 70%</h5>          
                            </div>
                        </div>
                        <div class="progress">
                             <div class="progress-bar"
role="progressbar" aria-valuenow="85" aria-valuemin="0" aria-
valuemax="100" style="width: 85%">
                                 <h5>HTML & CSS 85%</h5>          
                            </div>
                       </div>
                       <div class="progress">
                          <div class="progress-bar"
role="progressbar" aria-valuenow="90" aria-aria-valuemin="0" aria-
valuemax="100" style="width: 90%">
                                 <h5>JAVASCRIPT 70%</h5>        
                            </div>
                         </div>
                    </div>
                    <div class="col-md-6">
                       <div class="progress">
                          <div class="progress-bar"
role="progressbar" aria-valuenow="85" aria-aria-valuemin="0" aria-
valuemax="100" style="width: 85%">
                                 <h5>REACT & JQUERY 70%</h5> 
                            </div>
                       </div>
                       <div class="progress">
                          <div class="progress-bar"
role="progressbar" aria-valuenow="80" aria-aria-valuemin="0" aria-
valuemax="100" style="width: 80%">
                                 <h5>BOOTSTRAP 750%</h5> 
                        </div>
                        </div> 
                        <div class="progress">
                         <div class="progress-bar"
role="progressbar" aria-valuenow="70" aria-aria-valuemin="0" aria-
valuemax="100" style="width: 70%">
                               <h5>PHP 80%</h5>  
                          </div>      
                       </div>
                 </div>
            </div>  
      </div>                                  
</section>
<section id="experience">
    <div class="container">
        <div class="white-divider"></div>
        <div class="heading">
            <h2>Experience Professionelle</h2>
        </div>
        <ul class="timeline">
        <li>
            <div class="timeline-badge"><span class="fa-solid fa-briefcase"></span></div>
            <div class="timeline-panel-container">
            <div class="timeline-panel">
            <div class="timeline-heading">
                 <h3>GOOGLE</h3>
                 <h4>Développeur Web Sénior</h4>
                 <p class="text-muted"><small class="fa-solid fa-bell"></small> 2020-2021</p>
            </div> 
            <div class="timeline-body">
                 <p>Ajout de la possibilité d'écouter une traduction dans Google Translate</p>
                 <p>Développement de Google Suggest en mode Offline</p>
                 <p>Nouveau design du player de Youtube adapté au mobile</p>
            </div> 

            
        </div>
    </div>
</li>
<li>
    <div class="timeline-badge"><i class="fa-solid fa-briefcase"></i></div>
    <div class="timeline-panel-container-inverted">
    <div class="timeline-panel">
    <div class="timeline-heading">
         <h3>FACEBOOK</h3>
         <h4>Développeur Web</h4>
         <p class="text-muted"><small class="fa-solid fa-bell"></small> 2021-2022</p>
    </div> 
    <div class="timeline-body">
         <p>Développement du bouton Share pour les applis Web mobile</p>
         <p>Lancement automatique des vidéos en mode mute depuis la Timeline</p>
    </div> 
</div>
</div>
</li>
<li>
    <div class="timeline-badge"><span class="fa-solid fa-briefcase"></span></div>
    <div class="timeline-panel-container">
    <div class="timeline-panel">
    <div class="timeline-heading">
         <h3>TWITTER</h3>
         <h4>Développeur Web Junior</h4>
         <p class="text-muted"><small class="fa-solid fa-bell"></small> 2022-2023</p>
    </div> 
    <div class="timeline-body">
         <p>Création et Développement du Retweet pour l'appli Web</p>
         <p>Intégration des vidéos sur les applis web mobile</p>
    </div> 
    
</div>
</div>
</li>
    </ul>
</div>


</section>
<section id="education">
   <div class="container">
     <div class="red-divider"></div>
     <div class="heading">
          <h2>Education</h2>
     </div>
     </div>
     <div class="row">
     <div class="col-4">
               <div class="education-block">
                   <h5>2020-2021</h5>
                   <span class="fa-solid fa-graduation-cap"></span>
                   <h3>Institut de Formation Sainte Marie - Abidjan</h3>
                   <h4>Brevet de Technicien Superieur</h4>
                   <div class="red-divider"></div>
                   <p>Réseaux Informatiques et Telecommunications</p>
                   <p>Système d'informations</p>
               </div>
          </div>
          <div class="col-4">
               <div class="education-block">
                    <h5>2024</h5>
                    <span class="fa-solid fa-graduation-cap"></span>
                    <h3>Happy Coders Academy</h3>
                    <h4>Formation "Développeur Web"</h4>
                    <div class="red-divider"></div>
                    <p>HTML/CSS & Javascript</p>
                    <P>JQuery & Bootstrap</p>
                    <P>Php & MySQL</p>
                    <p>Responsive Design</p>
          </div> 
          </div>  
          <div class="col-4">
               <div class="education-block">
                    <h5>2025</h5>
                    <span class="fa-solid fa-graduation-cap"></span>
                    <h3>Hall  Tech Africa</h3>
                    <h4>Formation "Data Analyse"</h4>
                    <div class="red-divider"></div>
                    <p> Python & R </p>
                    <P>Java & Scala</p>
                    <P>SQL</p>
                    <P>JavaScript</p>
          </div> 
          </div>
     </div>
   </div>
</section>
<section id="portfolio">
     <div class="container">
          <div class="white-divider"></div>
          <div class="heading">
               <h2>PORTFOLIO</h2>
          </div>
          <div class="row">
          <div class="col-sm-4"> 
               <a class="thumbnail" href="http://www.facebook.com" target="_blank">
                  <img src="images/facebook_share.png.png" alt=" facebook_share"></a>
          </div>
          <div class="col-sm-4"> 
               <a class="thumbnail" href="http://www.google.com" target="_blank">
                    <img src="images/google_translate.png.png" alt=" google_translate"></a>
          </div>
          <div class="col-sm-4"> 
               <a class="thumbnail" href="http://www.twitter.com" target="_blank">
                    <img src="images/twitter_video.png.png" alt=" twitter_video"></a>
          </div>
         </div>
     <div class="row">
          <div class="col-sm-4"> 
               <a class="thumbnail" href="http://www.youtube.com" target="_blank">
                  <img src="images/youtube.png.png" alt=" youtube"></a>
          </div>
          <div class="col-sm-4"> 
               <a class="thumbnail" href="http://www.twitter.com" target="_blank">
                    <img src="images/twitter_retweet.png.png" alt=" twitter_retweet"></a>
          </div>
          <div class="col-sm-4"> 
               <a class="thumbnail" href="http://www.facebook.com" target="_blank">
                    <img src="images/facebook_video.png.png" alt=" facebook_video"></a>
     </div>
     </div>
      <section id="projects">
          <div class="container">
               <div class="white-divider"></div>
               <div class="heading">
                    <h2>PROJECTS</h2>
               </div>
               <div class="row">
               <div class="col-sm-4"> 
                    <a class="thumbnail" href="http://www.html.com" target="_blank">
                        <img src="images/png-clipart-html-logo-html.png" alt="html"></a>
               </div>
               <div class="col-sm-4"> 
                    <a class="thumbnail" href="http://www.Javascript.com" target="_blank">
                          <img src="images/js.png.png" alt=" Javascript"></a>
               </div>
               <div class="col-sm-4"> 
                    <a class="thumbnail" href="http://www.css.com" target="_blank">
                          <img src="images/css.png.png" alt=" css"></a>
               </div>
               <div class="separator"></div>
               <div class="row">
               <div class="col-sm-4"> 
                    <a class="thumbnail" href="http://www.react.com" target="_blank">
                        <img src="images/react.png" alt="react"></a>
               </div>
               <div class="col-sm-4"> 
                    <a class="thumbnail" href="http://www.python.com" target="_blank">
                          <img src="images/python.png" alt=" python"></a>
               </div>
               <div class="col-sm-4"> 
                    <a class="thumbnail" href="http://www.jQuery.com" target="_blank">
                          <img src="images/jQuery.png" alt="jQuery"></a>
               </div>
              <div class="separator"></div>

             <div class="row">
               <div class="col-sm-4"> 
                    <a class="thumbnail" href="http://www.sQL.com" target="_blank">
                        <img src="images/sQL.png" alt="sQL"></a>
               </div>
               <div class="col-sm-4"> 
                    <a class="thumbnail" href="http://www.Bootstrap.com" target="_blank">
                          <img src="images/bootstrap-original-wordmark-8x.png" alt="Bootstrap"></a>
               </div>
               <div class="col-sm-4"> 
                    <a class="thumbnail" href="http://www.php.com" target="_blank">
                          <img src="images/php.png" alt="php"></a>
               </div>

              </div>
          </div>
</section>
<section id="recommandations">
     <div class="container">
        <div class="white-divider"></div>
      <div class="heading">
          <h2>RECOMMENDATIONS</h2>
<div class="carousel slide text-center" data-bs-ride="carousel">
     <div class="carousel-indicators">
       <button type="button" data-bs-target="#myCarousel" data-bs-ride-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
       <button type="button" data-bs-target="#myCarousel" data-bs-ride-to="1" aria-label="Slide 2"></button>
       <button type="button" data-bs-target="#myCarousel" data-bs-ride-to="2" aria-label="Slide 3"></button>
     </div>
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="images/facebook_video.png.png " class="d-block w-100" alt="facebook_share">
         <h3>"Claver t'es le meilleur! Merci pour tout..."</h3>
         <h4>Larry Page, Google Co-Founder</h4>
       </div>
       <div class="carousel-item">
         <img src="images/google_translate.png.png" class="d-block w-100" alt="google_translate">
         <h3>"Merci Claver de m'avoir appris à coder... Tout ça c'est grâce à toi!"</h3>
         <h4>Mark Zuckerberg,Facebook Founder and CEO</h4>
       </div>
       <div class="carousel-item">
         <img src="images/twitter_video.png.png" class="d-block w-100" alt="twitter_video">
         <h3>"L'esprit le plus créatif que j'ai vu de toute ma vie..."</h3>
         <h4>Jack Dorsey,Twitter Founder and CEO</h4>
       </div>
     </div>
     <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-ride="prev">
       <span class="carousel-control-prev-icon" aria-visible="true"></span>
       <span class="visually-visible"></span>
     </button>
     <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-ride="next">
       <span class="carousel-control-next-icon" aria-visible="true"></span>
       <span class="visually-visible"></span>
     </button>
   </div>
   </sectio>
    <section id="contact">
        <div class="container">
            <div class="white-divider"></div>
            <div class="heading">
                <h2>CONTACT</h2>
            </div>
            <div class="row">
                <form id="contact-form" method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" role="form">
                    <div class="row">
                        <div class="col-md-6">
                            <label for="firstname">Prénom *</label>
                            <input type="text" id="firstname" name="firstname" class="form-control" placeholder="Votre prénom" value="<?php echo htmlspecialchars($firstname); ?>">
                            <p class="comments"><?php echo $firstnameError; ?></p>
                        </div> 
                        <div class="col-md-6">
                            <label for="name">Nom * </label>
                            <input type="text" id="name" name="name" class="form-control" placeholder="Votre nom" value="<?php echo htmlspecialchars($name); ?>">
                            <p class="comments"><?php echo $nameError; ?></p>  
                        </div>
                        <div class="col-md-6">           
                            <label for="email">Email * </label>
                            <input type="email" id="email" name="email" class="form-control" placeholder="Votre email" value="<?php echo htmlspecialchars($email); ?>">
                            <p class="comments"><?php echo $emailError; ?></p>  
                        </div>
                        <div class="col-md-6">
                            <label for="phone">Téléphone </label>
                            <input type="tel" id="phone" name="phone" class="form-control" placeholder="Votre téléphone" value="<?php echo htmlspecialchars($phone); ?>">
                            <p class="comments"><?php echo $phoneError; ?></p> 
                        </div> 
                        <div class="col-md-12">
                            <label for="message">Message * </label>
                            <textarea id="message" name="message" class="form-control" placeholder="Votre message" rows="4"><?php echo htmlspecialchars($message); ?></textarea>
                            <p class="comments"><?php echo $messageError; ?></p> 
                        </div>
                        <div class="col-md-12">
                            <p><strong>* Ces informations sont requises</strong></p> 
                        </div>
                        <div class="col-md-12">
                            <input type="submit" class="button2" value="Envoyer">
                        </div>    
                    </div>
                    <p class="thank-you" style="display:<?php echo $isSuccess ? 'block' : 'none'; ?>">Votre message a bien été envoyé. Merci de m'avoir contacté :)</p>
                </form>
            </div>
        </div>
    </section>
    <footer class="text-center">
     <a href="#about">
     <span class="fa-solid fa-chevron-up"></span>
     </a>
     <h5>@ 2025 Claver Kouakou Kouame</h5>
    </footer>
</body>
</html>
