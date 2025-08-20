# Étape 1 : Utiliser une image Node.js légère comme builder
FROM node:18-alpine AS builder

# Étape 2 : Définir le répertoire de travail
WORKDIR /app

# Étape 3 : Copier les fichiers du projet
COPY . .

# Étape 4 : Installer un serveur HTTP simple
RUN npm install -g http-server

# Étape 5 : Exposer le port 8080
EXPOSE 8080

# Étape 6 : Démarrer le serveur HTTP
CMD ["http-server", "-p", "8080", "-a", "0.0.0.0", "-c-1"]