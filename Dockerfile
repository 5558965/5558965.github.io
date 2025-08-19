# Étape 0: Image de base avec arguments
ARG PHP_VERSION=8.2
FROM php:${PHP_VERSION}-apache-bookworm

# Étape 1: Configuration système
ENV APACHE_DOCUMENT_ROOT=/var/www/html/public \
    DEBIAN_FRONTEND=noninteractive

# Étape 2: Configuration Apache
RUN { \
    echo 'ServerName localhost'; \
    echo 'ServerTokens Prod'; \
    echo 'TraceEnable Off'; \
} >> /etc/apache2/apache2.conf && \
    a2enmod rewrite headers && \
    a2dismod status -f

# Étape 3: Mise à jour des dépôts (optimisé)
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-transport-https ca-certificates

# Étape 4: Installation des dépendances (CORRIGÉE)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libzip-dev \
    libpng-dev \
    libjpeg-dev \
    libwebp-dev \
    libicu-dev \
    zip \
    unzip \
    git \
    curl \
    && docker-php-ext-configure gd --with-jpeg --with-webp \
    && docker-php-ext-install -j$(nproc) \
    pdo \
    pdo_mysql \
    zip \
    gd \
    intl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Étape 5: Configuration PHP avancée
RUN { \
    echo 'expose_php = Off'; \
    echo 'upload_max_filesize = 128M'; \
    echo 'post_max_size = 128M'; \
    echo 'memory_limit = 256M'; \
    echo 'opcache.enable=1'; \
    echo 'opcache.memory_consumption=128'; \
    echo 'error_log = /var/log/php_errors.log'; \
} > /usr/local/etc/php/conf.d/prod.ini && \
    touch /var/log/php_errors.log && \
    chmod 666 /var/log/php_errors.log

# Étape 6: Installation de Composer
COPY --from=composer:2 /usr/bin/composer /usr/local/bin/composer

# Étape 7: Configuration des permissions et finalisation
WORKDIR /var/www/html
COPY . .
RUN chown -R www-data:www-data /var/www/html && \
    find /var/www/html -type d -exec chmod 755 {} \; && \
    find /var/www/html -type f -exec chmod 644 {} \; && \
    a2enmod rewrite && \
    a2dissite 000-default && \
    a2ensite 000-default

EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost/ || exit 1

# Étape 8: Commande de démarrage
CMD ["apache2-foreground"]