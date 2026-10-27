# 🚀 Guide d'installation - Portfolio

Ce guide vous accompagne pas à pas pour installer et lancer votre portfolio en local.

---

## 📋 Prérequis vérifiés

✅ **Docker** : Version 29.5.3 installée  
✅ **Node.js** : Version 24.19.0 installée  
✅ **PHP** : Version 8.0.30 installée  
✅ **Python** : Version 3.14.7 installée  
✅ **npm** : Version 11.17.0 installée  

---

## 🎯 Méthode recommandée selon votre cas

### Cas 1 : Je veux juste visualiser le site
👉 **Utilisez l'ouverture directe**

```bash
# Dans Git Bash
start index.html
```

### Cas 2 : Je veux tester le formulaire de contact
👉 **Utilisez PHP**

```bash
php -S localhost:8000
```

### Cas 3 : Je veux un environnement complet
👉 **Utilisez Docker**

```bash
docker-compose up --build -d
```

---

## 📦 Installation complète (recommandée)

### Étape 1 : Cloner le projet (si ce n'est pas déjà fait)

```bash
cd ~
git clone <votre-repo-url> Portfolio
cd Portfolio
```

### Étape 2 : Installer les dépendances PHP (optionnel)

Si vous voulez utiliser PHPMailer pour l'envoi d'emails :

```bash
# Vérifier si Composer est installé
composer --version

# Si pas installé, télécharger depuis https://getcomposer.org

# Installer les dépendances
composer install
```

### Étape 3 : Configurer les variables d'environnement

```bash
# Copier le fichier exemple
cp .env.example .env

# Éditer le fichier .env avec vos credentials
notepad .env
```

**Exemple de configuration Gmail** :
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=votre-email@gmail.com
SMTP_PASS=votre-mot-de-passe-application
SMTP_SECURE=tls
CONTACT_TO_ADDRESS=votre-email@gmail.com
MAIL_FROM_ADDRESS=no-reply@votre-domaine.com
MAIL_FROM_NAME="Portfolio Claver"
```

💡 **Pour Gmail** : Créez un "Mot de passe d'application" dans les paramètres de sécurité Google.

### Étape 4 : Choisir votre méthode de lancement

#### Option A : Docker (Production-ready)

```bash
# Construire et lancer
docker-compose up --build -d

# Vérifier que ça tourne
docker ps

# Voir les logs
docker logs portfolio-app

# Accéder au site
# Ouvrir http://localhost:8080

# Arrêter
docker-compose down
```

#### Option B : PHP Built-in Server (Simple et rapide)

```bash
# Lancer le serveur
php -S localhost:8000

# Accéder au site
# Ouvrir http://localhost:8000

# Arrêter : Ctrl+C dans le terminal
```

#### Option C : Python (Visualisation uniquement)

```bash
# Lancer le serveur
python -m http.server 8000

# Accéder au site
# Ouvrir http://localhost:8000

# Arrêter : Ctrl+C dans le terminal
```

#### Option D : Node.js http-server

```bash
# Installer (une seule fois)
npm install -g http-server

# Lancer le serveur
http-server -p 8000

# Accéder au site
# Ouvrir http://localhost:8000

# Arrêter : Ctrl+C dans le terminal
```

---

## ✅ Vérification de l'installation

### Test 1 : Page principale
1. Ouvrir http://localhost:8080 (ou 8000)
2. Vérifier que la page s'affiche correctement
3. Tester la navigation entre les sections

### Test 2 : Formulaire de contact
1. Aller à la section "Contact"
2. Remplir tous les champs
3. Cliquer sur "Envoyer"
4. Vérifier le message de confirmation

### Test 3 : Téléchargement CV
1. Cliquer sur "Télécharger CV"
2. Vérifier que le fichier PDF se télécharge

### Test 4 : Responsive design
1. Ouvrir les DevTools (F12)
2. Activer le mode responsive
3. Tester différentes tailles d'écran

---

## 🐛 Résolution de problèmes

### Problème : Port déjà utilisé

```bash
# Windows : Trouver quel processus utilise le port 8080
netstat -ano | findstr :8080

# Tuer le processus (remplacer PID par le numéro trouvé)
taskkill /PID <PID> /F

# Ou utiliser un autre port
php -S localhost:8001
```

### Problème : Docker ne démarre pas

```bash
# Vérifier que Docker Desktop est lancé
docker info

# Relancer Docker Desktop
# Réessayer
docker-compose up --build -d
```

### Problème : Formulaire ne fonctionne pas

**Vérifications** :
1. PHP est-il installé ? `php -v`
2. Le serveur est-il lancé avec PHP ? (pas Python)
3. Les variables d'environnement sont-elles configurées ?

**Solution temporaire** :
Le formulaire ouvrira votre client mail par défaut si l'envoi SMTP échoue.

### Problème : Images ne s'affichent pas

```bash
# Vérifier que le dossier images existe
ls -la images/

# Vérifier les permissions (Linux/Mac)
chmod -R 755 images/
```

---

## 🌐 Déploiement en ligne

### Déploiement sur Vercel

```bash
# Installer Vercel CLI
npm install -g vercel

# Se connecter
vercel login

# Déployer
vercel --prod

# Configurer les variables d'environnement
vercel env add TELEGRAM_BOT_TOKEN
vercel env add TELEGRAM_CHAT_ID
```

### Déploiement sur Netlify

```bash
# Installer Netlify CLI
npm install -g netlify-cli

# Se connecter
netlify login

# Déployer
netlify deploy --prod
```

---

## 📚 Commandes utiles

```bash
# Vérifier les versions installées
docker --version
php -v
python --version
node --version
npm --version

# Lister les containers Docker
docker ps -a

# Voir les logs Docker
docker logs portfolio-app

# Nettoyer Docker
docker system prune -a

# Mettre à jour les dépendances PHP
composer update

# Mettre à jour les dépendances Node
npm update
```

---

## 🎓 Ressources supplémentaires

- [Documentation PHP](https://www.php.net/docs.php)
- [Documentation Docker](https://docs.docker.com/)
- [Documentation Vercel](https://vercel.com/docs)
- [PHPMailer GitHub](https://github.com/PHPMailer/PHPMailer)

---

## 📞 Support

En cas de problème :
1. Vérifier ce guide
2. Consulter les logs : `docker logs portfolio-app`
3. Vérifier le README.md du projet
4. Ouvrir une issue sur GitHub

---

**Dernière mise à jour** : Janvier 2025  
**Version** : 1.0.0
