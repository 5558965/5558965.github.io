FROM php:8.1-apache

# Copier les sources dans le répertoire web d'Apache
WORKDIR /var/www/html
COPY . /var/www/html/

# Activer rewrite si nécessaire
RUN a2enmod rewrite || true

# Exposer le port HTTP standard (mappé par docker-compose)
EXPOSE 80

# Démarrage par défaut (Apache déjà configuré dans l'image officielle)
CMD ["apache2-foreground"]