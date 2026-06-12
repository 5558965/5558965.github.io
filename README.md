# Portfolio de Claver Kouakou Kouame

Portfolio personnel de Claver Kouakou Kouame - Développeur Web Full Stack & DevOps/Cloud Engineer.

## 📋 À propos

Ce projet est un site de portfolio/CV personnel moderne et professionnel construit avec HTML, CSS et JavaScript. Le site inclut :
- Animations fluides et effets visuels
- Design responsive adapté à tous les écrans
- Formulaire de contact interactif
- Sections complètes (À propos, Compétences, Expérience, Formation, Certifications, Portfolio, Services, Recommandations, Contact)
- Configuration Docker pour un déploiement rapide

## 🚀 Technologies utilisées

### Frontend
- **HTML5** - Structure du site
- **CSS3** - Styling et animations
- **JavaScript** - Interactivité
- **Bootstrap 5.3.3** - Framework CSS responsive
- **Font Awesome 6.5.2** - Icônes
- **AOS (Animate On Scroll)** - Animations au scroll
- **Google Fonts** - Polices Lato & Montserrat

### Backend
- **PHP 8.1** - Traitement du formulaire de contact
- **Apache** - Serveur web

### DevOps
- **Docker** - Conteneurisation
- **Docker Compose** - Orchestration

## 📁 Structure du projet

```
Portfolio/
├── docs/                  # Documents (CV-CLAVER.pdf)
├── images/                # Images et assets (58 fichiers)
├── index.html             # Page principale
├── style.css              # Styles globaux
├── script.js              # Logique JavaScript
├── contact.php            # Traitement du formulaire de contact
├── Dockerfile             # Build Docker (PHP 8.1 + Apache)
├── docker-compose.yml     # Configuration développement
├── docker-compose.prod.yml # Configuration production
├── .gitignore
├── .dockerignore
├── .htaccess
└── README.md              # Ce fichier
```

## 🎯 Sections du site

1. **À propos** - Présentation personnelle avec photo et texte animé
2. **Compétences** - Barres de progression et technologies maîtrisées
3. **Expérience Professionnelle** - Timeline des expériences
4. **Formation** - Parcours éducatif
5. **Certifications** - Badges Cisco, CompTIA Security+, etc.
6. **Portfolio** - Projets réalisés (CARENTCI, CÔTIÈRE MEDIA, FENACI, etc.)
7. **Services** - Ce que je propose (création sites, apps, intégrations, etc.)
8. **Recommandations** - Carrousel avec témoignages
9. **Contact** - Formulaire interactif avec validation AJAX

## 💻 Installation et exécution

### Option 1 : Exécution locale (sans Docker)

1. Clonez ou téléchargez le projet
2. Ouvrez `index.html` dans votre navigateur préféré
3. Pour le formulaire de contact, vous avez besoin d'un serveur PHP (XAMPP, WAMP, MAMP, etc.)

### Option 2 : Avec Docker (recommandée)

1. Assurez-vous d'avoir Docker et Docker Compose installés
2. Construisez et lancez le conteneur :

```bash
docker-compose up --build -d
```

3. Ouvrez votre navigateur et allez sur : `http://localhost:8080`

4. Pour arrêter le conteneur :
```bash
docker-compose down
```

## 📧 Configuration du formulaire de contact

Le fichier `contact.php` nécessite une configuration pour envoyer des emails. Deux options :

### Option 1 : Utiliser PHPMailer (recommandée)

1. Installez PHPMailer via Composer :
```bash
composer require phpmailer/phpmailer
```

2. Configurez les variables d'environnement dans `docker-compose.yml` :
```yaml
environment:
  - SMTP_HOST=smtp.example.com
  - SMTP_PORT=587
  - SMTP_USER=user@example.com
  - SMTP_PASS=secret
  - SMTP_SECURE=tls
  - CONTACT_TO_ADDRESS=destinataire@example.com
  - MAIL_FROM_ADDRESS=no-reply@example.com
  - MAIL_FROM_NAME="Portfolio Claver"
```

### Option 2 : Fonction mail() de PHP

Si PHPMailer n'est pas installé, le script utilisera la fonction `mail()` native de PHP si elle est disponible sur le serveur.

## 🌟 Caractéristiques

✅ **Design Responsive** - Adapté à mobile, tablette et desktop  
✅ **Animations fluides** - Effets de scroll, hover, pulse, etc.  
✅ **Interactivité** - Filtres portfolio, carrousel recommandations, menu mobile  
✅ **Formulaire AJAX** - Validation et envoi sans rechargement de page  
✅ **Dockerisé** - Environnement de développement prêt à l'emploi  
✅ **Optimisé** - Images et assets bien organisés  

## 🔧 Améliorations possibles

- Séparer `index.html` en plusieurs fichiers (header, footer, sections) pour la maintenabilité
- Configurer un vrai service d'envoi d'emails (SMTP)
- Ajouter des métadonnées SEO améliorées
- Mettre en place un système de déploiement continu (CI/CD)
- Ajouter une version anglaise du site

## 👨‍💻 Auteur

**Claver Kouakou Kouame**  
- Développeur Web Full Stack
- DevOps/Cloud Engineer
- Certifié AWS Solutions Architect

---

*Merci de visiter mon portfolio !* 🚀
