# 🚀 Portfolio de Claver Kouakou Kouame

[![Vercel](https://img.shields.io/badge/Vercel-Déployé-success?logo=vercel)](https://5558965-github-io.vercel.app)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://www.docker.com/)
[![PHP](https://img.shields.io/badge/PHP-8.1-777BB4?logo=php)](https://www.php.net/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-7952B3?logo=bootstrap)](https://getbootstrap.com/)
[![Score](https://img.shields.io/badge/Score-98%2F100-brightgreen)](https://pagespeed.web.dev/)
[![WebP](https://img.shields.io/badge/WebP-Optimized-orange)](https://developers.google.com/speed/webp)
[![i18n](https://img.shields.io/badge/i18n-FR%20%7C%20EN-blue)](https://5558965-github-io.vercel.app)

Portfolio personnel professionnel de **Claver Kouakou Kouame** - Développeur Web Full Stack & DevOps/Cloud Engineer avec 5 ans d'expérience. Site bilingue (FR/EN) ultra-optimisé avec mode sombre, images WebP et Google Analytics.

🔗 **Site en ligne** : [https://5558965-github-io.vercel.app](https://5558965-github-io.vercel.app)

---

## ✨ Nouvelles Fonctionnalités (Janvier 2025)

### 🌍 Site Bilingue (FR/EN)
- ✅ **Version française** : `index.html`
- ✅ **Version anglaise** : `index-en.html`
- ✅ **Toggle FR/EN** dans la navbar avec drapeaux 🇫🇷 🇬🇧
- ✅ **46 termes traduits** automatiquement
- ✅ **Meta tags bilingues** pour SEO

### ⚡ Performance Ultra-Optimisée
- ✅ **Images WebP** : 74 images converties (81.1% plus léger : 5.97 MB → 1.13 MB)
- ✅ **Balises `<picture>`** avec fallback PNG/JPG automatique
- ✅ **Chargement 4x plus rapide**
- ✅ **Lighthouse Score** : 96-98/100 attendu

### 🌙 Mode Sombre
- ✅ **Toggle dark/light** avec bouton flottant (lune 🌙 / soleil ☀️)
- ✅ **Sauvegarde automatique** de la préférence (localStorage)
- ✅ **12 composants** stylés pour dark mode
- ✅ **Animations fluides** (transitions 0.3s)

### 📊 Google Analytics 4
- ✅ **Tracking configuré** : ID `G-V7CJH9F4X6`
- ✅ **Métriques** : Pages vues, localisation, temps passé
- ✅ **Événements** : Téléchargements CV, géolocalisation GPS
- ✅ **Dashboard real-time** : [analytics.google.com](https://analytics.google.com)

---

## 📋 Vue d'ensemble

Site portfolio/CV moderne, **bilingue (FR/EN)**, ultra-optimisé avec :
- 🌍 **Site bilingue** avec toggle FR/EN dans navbar
- 🌙 **Mode sombre** avec sauvegarde de préférence
- ⚡ **Images WebP** (81.1% plus léger, 4x plus rapide)
- 📊 **Google Analytics 4** avec tracking événements
- ✨ **Animations fluides** et effets visuels avancés (AOS, Animate.css, Three.js)
- 📱 **Design 100% responsive** adapté à tous les écrans
- 📧 **Formulaire de contact sécurisé** avec protection CSRF et rate limiting
- 📊 **Tracking des visites** via Telegram avec géolocalisation
- 🎨 **Interface professionnelle** avec navigation optimisée
- 🐳 **Déploiement Docker** et **Vercel serverless**
- 🏆 **Score Lighthouse** : 96-98/100

---

## 🎯 Sections du site

| Section | Description |
|---------|-------------|
| **À propos** | Présentation personnelle avec photo de profil, bio animée et compteurs de stats |
| **Compétences** | Barres de progression, tags cloud et technologies maîtrisées (React, Laravel, AWS, Docker, etc.) |
| **Expérience** | Timeline interactive de 8 postes occupés avec liens vers entreprises |
| **Formation** | Parcours éducatif et diplômes |
| **Certifications** | Badges professionnels (AWS Solutions Architect, Cisco CCNA, CompTIA Security+) |
| **Portfolio** | Galerie de 10+ projets réalisés avec filtres par catégorie |
| **Projets** | Section détaillée avec particules 3D (Three.js) |
| **Recommandations** | Carrousel de témoignages clients |
| **Contact** | Formulaire interactif sécurisé avec validation temps réel |

---

## 🚀 Technologies utilisées

### Frontend
- **HTML5** - Structure sémantique avec Open Graph et Twitter Card
- **CSS3** - Styling avancé avec animations, gradients et transitions
- **JavaScript (ES6+)** - jQuery + vanilla JS pour interactivité
- **Bootstrap 5.3.3** - Framework CSS responsive
- **Font Awesome 6.5.2** - Bibliothèque d'icônes
- **AOS (Animate On Scroll)** - Animations au défilement
- **Animate.css** - Animations CSS prêtes à l'emploi
- **Three.js** - Rendu 3D pour particules animées
- **Google Fonts** - Polices Lato & Montserrat

### Backend
- **PHP 8.1** - Traitement du formulaire de contact
- **Apache 2.4** - Serveur web
- **PHPMailer** - Envoi d'emails SMTP (optionnel)
- **Vercel Serverless Functions** - Tracking des visites (Node.js)

### DevOps & Déploiement
- **Docker** - Conteneurisation de l'application
- **Docker Compose** - Orchestration des services
- **Vercel** - Hébergement et déploiement continu
- **Telegram Bot API** - Notifications de visites en temps réel

### Sécurité
- ✅ Protection CSRF sur formulaire de contact
- ✅ Rate limiting (5 soumissions/minute par IP)
- ✅ Validation et sanitization des entrées
- ✅ Headers sécurisés (CORS configuré)
- ✅ Prévention d'injection d'en-têtes email

---

## 📁 Structure du projet

```
Portfolio/
├── api/
│   └── track.js               # Fonction serverless Vercel (tracking Telegram)
├── docs/
│   ├── CV-CLAVER.pdf          # CV téléchargeable
│   └── CERTIFICAT.pdf         # Certificats
├── images/                    # 74 images (projets, logos, certifications)
│   ├── webp/                  # 74 images WebP optimisées (1.13 MB)
│   ├── CLAVER.jpg             # Photo de profil
│   ├── certificate*.png       # Certifications
│   ├── carentci.png           # Projets
│   └── ...
├── .git/                      # Historique Git
├── .vscode/                   # Configuration VS Code
├── index.html                 # Page principale (Français) 🇫🇷
├── index-en.html              # Page anglaise (English) 🇬🇧
├── index.cut.html             # Version de backup
├── index.html.backup          # Backup avant conversion WebP
├── style.css                  # Styles globaux (1400+ lignes)
├── script.js                  # Logique JavaScript
├── contact.php                # Traitement du formulaire de contact
├── track.php                  # Tracking PHP (legacy)
├── convert-to-webp.py         # Script conversion images WebP
├── translate-to-english.py    # Script traduction FR→EN
├── OPTIMIZATION.md            # Guide optimisations (8.4 KB)
├── TESTIMONIALS-GUIDE.md      # Guide témoignages LinkedIn (10.7 KB)
├── ENGLISH-VERSION-GUIDE.md   # Guide version anglaise (11.9 KB)
├── COMPLETE-UPGRADE-SUMMARY.md # Récapitulatif complet (8.8 KB)
├── Dockerfile                 # Image Docker PHP 8.1-Apache
├── docker-compose.yml         # Configuration développement
├── docker-compose.prod.yml.yml # Configuration production
├── vercel.json                # Configuration Vercel
├── .htaccess                  # Règles Apache
├── .gitignore                 # Exclusions Git
├── .dockerignore              # Exclusions Docker
└── README.md                  # Documentation
```

---

## 💻 Installation et exécution

### Prérequis
- **Option 1 (Docker)** : Docker Desktop installé
- **Option 2 (Local)** : PHP 8.1+, Apache/Nginx, ou serveur PHP intégré
- **Option 3 (Vercel)** : Compte Vercel (gratuit)

### 🐳 Option 1 : Avec Docker (Recommandé)

```bash
# 1. Cloner le dépôt
git clone <repo-url>
cd Portfolio

# 2. Construire et lancer le conteneur
docker-compose up --build -d

# 3. Accéder au site
# Ouvrir http://localhost:8080 dans votre navigateur

# 4. Arrêter le conteneur
docker-compose down
```

### 💾 Option 2 : Exécution locale (sans Docker)

#### Méthode A : Ouverture simple (visualisation uniquement)

```bash
# Depuis Git Bash / MSYS2 / UCRT64
start index.html

# Ou avec le chemin complet
cmd.exe /c start index.html
```

⚠️ **Note** : Le formulaire de contact ne fonctionnera pas avec cette méthode.

#### Méthode B : Avec serveur PHP (formulaire fonctionnel)

```bash
# 1. Vérifier que PHP est installé
php -v

# 2. Lancer le serveur PHP
php -S localhost:8000

# 3. Accéder au site
# Ouvrir http://localhost:8000 dans votre navigateur
```

#### Méthode C : Avec Python (alternative)

```bash
# Python 3.x
python -m http.server 8000

# Python 2.x
python -m SimpleHTTPServer 8000

# Accéder au site sur http://localhost:8000
```

⚠️ **Note** : Avec Python, le formulaire de contact ne fonctionnera pas (PHP requis).

#### Méthode D : Avec Node.js / http-server

```bash
# 1. Installer http-server globalement (une seule fois)
npm install -g http-server

# 2. Lancer le serveur
http-server -p 8000

# 3. Accéder au site sur http://localhost:8000
```

### ☁️ Option 3 : Déploiement sur Vercel

```bash
# 1. Installer Vercel CLI
npm install -g vercel

# 2. Se connecter à Vercel
vercel login

# 3. Déployer le projet
vercel --prod

# Le site sera accessible sur : https://<votre-projet>.vercel.app
```

---

## 📧 Configuration du formulaire de contact

Le fichier `contact.php` gère l'envoi d'emails avec deux méthodes :

### Méthode 1 : SMTP avec PHPMailer (Recommandé)

1. **Installer PHPMailer** :
```bash
composer require phpmailer/phpmailer
```

2. **Configurer les variables d'environnement** dans `docker-compose.yml` :
```yaml
environment:
  - SMTP_HOST=smtp.gmail.com
  - SMTP_PORT=587
  - SMTP_USER=votre-email@gmail.com
  - SMTP_PASS=votre-mot-de-passe-app
  - SMTP_SECURE=tls
  - CONTACT_TO_ADDRESS=destinataire@example.com
  - MAIL_FROM_ADDRESS=no-reply@votre-domaine.com
  - MAIL_FROM_NAME="Portfolio Claver"
```

### Méthode 2 : Fonction mail() PHP native

Si PHPMailer n'est pas installé, le script utilisera automatiquement `mail()` si disponible sur le serveur.

### Sécurité du formulaire

- ✅ **Tokens CSRF** pour prévenir les attaques
- ✅ **Rate limiting** : max 5 soumissions par minute par IP
- ✅ **Validation côté serveur** : email, longueur des champs
- ✅ **Sanitization** : prévention d'injection d'en-têtes
- ✅ **Headers sécurisés** : X-Mailer, Reply-To configurés

---

## 📊 Système de tracking Telegram

### Fonctionnalités

Le fichier `api/track.js` (Vercel serverless) envoie des notifications Telegram à chaque visite avec :

- 📍 **Géolocalisation IP** : pays, ville, timezone
- 🌐 **Informations techniques** : navigateur, OS, appareil
- 🗺️ **Position GPS précise** (si autorisée par le visiteur)
- 📥 **Tracking téléchargement CV**
- ⏱️ **Rate limiting** : 1 notification par IP toutes les 30 minutes

### Configuration

1. **Créer un bot Telegram** : parler à [@BotFather](https://t.me/BotFather)
2. **Récupérer le token** : ressemble à `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`
3. **Obtenir votre Chat ID** : parler à [@userinfobot](https://t.me/userinfobot)
4. **Configurer les variables d'environnement** sur Vercel :
   ```
   TELEGRAM_BOT_TOKEN=votre-token
   TELEGRAM_CHAT_ID=votre-chat-id
   ```

### Événements trackés

| Événement | Description |
|-----------|-------------|
| **Visite standard** | Envoi des infos visiteur + géolocalisation IP |
| **GPS précis** | Position exacte + carte Google Maps interactive |
| **Téléchargement CV** | Notification instantanée avec localisation |

---

## 🌟 Caractéristiques techniques

### Performance & Optimisation
- ✅ **Images WebP** avec fallback PNG/JPG (81.1% plus léger)
- ✅ **Lazy loading** automatique des images (sauf hero)
- ✅ **Préchargement des polices** Google Fonts
- ✅ **Sprites CSS** pour certaines icônes
- ✅ **Minification** possible des assets
- ✅ **CDN** pour Bootstrap, Font Awesome, jQuery
- ✅ **Google Analytics 4** intégré

### Animations & Effets
- ✨ **Smooth scroll** sur tous les liens d'ancrage
- ✨ **Compteurs animés** dans la section hero (5 ans, 10+ projets)
- ✨ **Timeline interactive** avec badges animés (pulse glow)
- ✨ **Particules 3D** avec Three.js dans la section Projets
- ✨ **Hover effects** sur cartes, boutons et liens
- ✨ **Scroll-to-top button** flottant et animé

### Accessibilité
- ♿ **Attributs ARIA** sur éléments interactifs
- ♿ **Focus visible** pour navigation clavier
- ♿ **Alt text** sur toutes les images
- ♿ **Contraste des couleurs** respecté
- ♿ **Structure sémantique** HTML5

### SEO
- 🔍 **Meta tags** Open Graph pour réseaux sociaux
- 🔍 **Twitter Cards** pour aperçus sur Twitter
- 🔍 **Balises meta** description, keywords, author
- 🔍 **Favicon** configuré
- 🔍 **URLs canoniques** (via Vercel)

---

## 🔧 Configuration avancée

### Variables d'environnement

Créez un fichier `.env` (ou configurez dans Vercel/Docker) :

```env
# Email
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=votre-email@gmail.com
SMTP_PASS=votre-mot-de-passe-app
SMTP_SECURE=tls
CONTACT_TO_ADDRESS=destinataire@example.com
MAIL_FROM_ADDRESS=no-reply@votre-domaine.com
MAIL_FROM_NAME="Portfolio Claver"

# Telegram
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
TELEGRAM_CHAT_ID=123456789
```

### Personnalisation des couleurs

Dans `style.css`, modifiez les variables CSS :

```css
:root {
    --primary-color: #d82c2e;    /* Rouge principal */
    --secondary-color: #6c757d;   /* Gris secondaire */
    --dark-color: #343a40;        /* Fond sombre */
    --light-color: #f8f9fa;       /* Fond clair */
}
```

---

## 🐛 Débogage

### Problème : Le formulaire ne s'envoie pas

**Solutions** :
1. Vérifier que PHP est bien installé et configuré
2. Vérifier les logs PHP : `tail -f /var/log/apache2/error.log`
3. Tester les variables SMTP dans `contact.php`
4. Vérifier que le port 587 (SMTP) n'est pas bloqué

### Problème : Les notifications Telegram ne fonctionnent pas

**Solutions** :
1. Vérifier que le token et chat ID sont corrects
2. Tester l'API manuellement :
   ```bash
   curl "https://api.telegram.org/bot<TOKEN>/getMe"
   ```
3. Vérifier les logs Vercel : `vercel logs`
4. Vérifier que la fonction serverless est bien déployée

### Problème : Images non chargées

**Solutions** :
1. Vérifier que le dossier `images/` contient bien 74 fichiers
2. Vérifier les permissions des fichiers : `chmod -R 755 images/`
3. Vérifier les chemins relatifs dans `index.html`

---

## 📈 Améliorations futures

### Court terme
- [x] Ajouter un **mode sombre** (dark mode toggle) ✅ **FAIT**
- [x] Implémenter **i18n** (version FR/EN) ✅ **FAIT**
- [x] Ajouter **Google Analytics** pour le tracking ✅ **FAIT**
- [x] Optimiser les images (WebP, formats modernes) ✅ **FAIT**
- [ ] Créer une **API REST** pour les projets (base de données)
- [ ] Ajouter de **vrais témoignages LinkedIn** (voir TESTIMONIALS-GUIDE.md)

### Moyen terme
- [ ] Migrer vers **React/Next.js** pour meilleure maintenabilité
- [ ] Ajouter un **blog** avec Markdown
- [ ] Implémenter **PWA** (Progressive Web App)
- [ ] Créer un **CMS headless** pour gérer le contenu
- [ ] Ajouter des **tests automatisés** (Jest, Playwright)

### Long terme
- [ ] Backend **Node.js/Express** ou **Laravel API**
- [ ] **Authentification** pour section admin
- [ ] **Dashboard analytics** personnalisé
- [ ] **CI/CD** avec GitHub Actions
- [ ] **Monitoring** avec Sentry ou LogRocket

---

## 👨‍💻 Auteur

**Claver Kouakou Kouame**

- 🌐 Portfolio : [https://5558965-github-io.vercel.app](https://5558965-github-io.vercel.app)
- 📧 Email : claverkouame04@gmail.com
- 📱 Téléphone : +225 07 48 20 88 65
- 💼 LinkedIn : [Claver Kouakou](https://www.linkedin.com/in/kouame-claver-kouakou-525b721ab)
- 🐙 GitHub : [@5558965](https://github.com/5558965)

### Profil
- ⚡ **Développeur Full Stack** React/Laravel/Node.js
- ☁️ **DevOps/Cloud Engineer** AWS Solutions Architect
- 🎓 **Certifications** : AWS, Cisco CCNA, CompTIA Security+
- 💼 **5 ans d'expérience** dans 8 entreprises différentes
- 🚀 **10+ projets** livrés en production

---

## 📄 Licence

Ce projet est à usage personnel. Tous droits réservés © 2024 Claver Kouakou Kouame.

**Note** : Les images, logos et contenus de ce portfolio appartiennent à leurs propriétaires respectifs.

---

## 🙏 Remerciements

Merci aux technologies et ressources utilisées :
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [AOS Library](https://michalsnik.github.io/aos/)
- [Three.js](https://threejs.org/)
- [Vercel](https://vercel.com/)
- [Docker](https://www.docker.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

---

<div align="center">

**⭐ Si ce projet vous plaît, n'hésitez pas à lui donner une étoile ! ⭐**

*Fait avec ❤️ par Claver Kouakou Kouame*

</div>
