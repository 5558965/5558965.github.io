# Étape 0: Image de base avec arguments
ARG PHP_VERSION=8.2
FROM php:${PHP_VERSION}-apache

# Étape 1: Configuration système
ENV APACHE_DOCUMENT_ROOT=/var/www/html/public \
    DEBIAN_FRONTEND=noninteractive

# Étape 2: Configuration Apache
RUN { \
    echo 'ServerName localhost'; \
    echo 'ServerTokens Prod'; \
    echo 'TraceEnable Off'; \
} >> /etc/apache2/apache2.conf && \
    a2enmod rewrite headers ssl && \
    a2dismod status -f

# Étape 3: Configuration des dépôts (optimisé)
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends apt-transport-https; \
    echo "deb https://deb.debian.org/debian bookworm main contrib non-free" > /etc/apt/sources.list; \
    echo "deb https://deb.debian.org/debian-security bookworm-security main" >> /etc/apt/sources.list; \
    echo "deb https://deb.debian.org/debian bookworm-updates main" >> /etc/apt/sources.list

# Étape 4: Installation des dépendances (optimisé)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libzip-dev \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    libwebp-dev \
    libicu-dev \
    zip \
    unzip \
    git \
    curl \
    && docker-php-ext-configure gd --with-freetype --with-jpeg --with-webp \
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

# Étape 7: Configuration finale
WORKDIR /var/www/html
COPY . .
RUN chown -R www-data:www-data /var/www/html && \
    a2ensite 000-default.conf && \
    service apache2 restart

EXPOSE 80 443
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost/ || exit 1