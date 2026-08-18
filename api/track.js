// api/track.js — Vercel Serverless Function
// Envoie une notification Telegram à chaque visite du portfolio

const BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN || '8729026440:AAEgfIN9kUH-W8pEWlXJfXFj306a8g-CQMo';
const CHAT_ID   = process.env.TELEGRAM_CHAT_ID   || '6103078174';

// Rate limiting simple en mémoire
const visited = new Map();
const COOLDOWN_MS = 30 * 60 * 1000; // 30 minutes

export default async function handler(req, res) {
    // CORS
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, GET, OPTIONS');
    if (req.method === 'OPTIONS') return res.status(200).end();

    // Récupérer l'IP du visiteur
    const ip = req.headers['x-forwarded-for']?.split(',')[0]?.trim()
             || req.socket?.remoteAddress
             || 'inconnue';

    // Ignorer localhost
    if (ip === '127.0.0.1' || ip === '::1') {
        return res.status(200).json({ status: 'ignored', reason: 'localhost' });
    }

    const now = Date.now();

    // ─── MODE GPS PRÉCIS (envoyé depuis le navigateur) ───────────
    // Si le corps contient lat/lng, c'est une notification GPS précise
    let body = {};
    try {
        body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
    } catch (_) {}

    // ─── MODE CV DOWNLOAD ────────────────────────────────────────
    if (body.event === 'cv_download') {
        const country   = req.headers['x-vercel-ip-country']        || null;
        const city      = req.headers['x-vercel-ip-city']
                            ? decodeURIComponent(req.headers['x-vercel-ip-city'])
                            : null;
        const timezone  = req.headers['x-vercel-ip-timezone']       || null;
        const countryNames = new Intl.DisplayNames(['fr'], { type: 'region' });
        const countryName  = country ? countryNames.of(country) : 'Inconnu';
        const locationLine = [city, countryName].filter(Boolean).join(', ') || 'Inconnue';

        const date = new Date().toLocaleString('fr-FR', {
            timeZone: timezone || 'Africa/Abidjan',
            dateStyle: 'short',
            timeStyle: 'medium'
        });

        const userAgent = req.headers['user-agent'] || 'Inconnu';
        let device = 'Ordinateur 🖥️';
        if (/Mobile|Android|iPhone/i.test(userAgent)) device = 'Mobile 📱';

        const cvMessage = `📥 *Ton CV vient d'être téléchargé !*\n\n`
                        + `📅 *Date :* ${date}\n`
                        + `🌍 *Localisation :* ${locationLine}\n`
                        + `🌐 *IP :* \`${ip}\`\n`
                        + `📲 *Appareil :* ${device}`;

        try {
            await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    chat_id:    CHAT_ID,
                    text:       cvMessage,
                    parse_mode: 'Markdown'
                })
            });
        } catch (_) {}

        return res.status(200).json({ status: 'ok', type: 'cv_download' });
    }

    if (body.lat && body.lng) {        const lat = parseFloat(body.lat);
        const lng = parseFloat(body.lng);
        const acc = body.accuracy ? `~${Math.round(body.accuracy)}m` : '?';

        const gpsMessage = `📍 *Position GPS exacte du visiteur !*\n\n`
                         + `🌐 *IP :* \`${ip}\`\n`
                         + `📏 *Précision :* ${acc}\n`
                         + `🗺️ *Carte exacte :* [Ouvrir Google Maps](https://maps.google.com/?q=${lat},${lng})\n`
                         + `🛰️ *Coordonnées :* \`${lat}, ${lng}\``;

        try {
            // Envoyer aussi la localisation Telegram native (carte interactive)
            await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendLocation`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    chat_id:   CHAT_ID,
                    latitude:  lat,
                    longitude: lng
                })
            });

            // Envoyer le message texte avec les détails
            await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    chat_id:                  CHAT_ID,
                    text:                     gpsMessage,
                    parse_mode:               'Markdown',
                    disable_web_page_preview: true
                })
            });
        } catch (_) {}

        return res.status(200).json({ status: 'ok', type: 'gps' });
    }

    // ─── MODE STANDARD (visite initiale) ─────────────────────────
    // Rate limiting
    const lastVisit = visited.get(ip);
    if (lastVisit && (now - lastVisit) < COOLDOWN_MS) {
        return res.status(200).json({ status: 'throttled' });
    }
    visited.set(ip, now);

    // Géolocalisation via headers natifs Vercel
    const country   = req.headers['x-vercel-ip-country']        || null;
    const region    = req.headers['x-vercel-ip-country-region'] || null;
    const city      = req.headers['x-vercel-ip-city']
                        ? decodeURIComponent(req.headers['x-vercel-ip-city'])
                        : null;
    const latitude  = req.headers['x-vercel-ip-latitude']       || null;
    const longitude = req.headers['x-vercel-ip-longitude']      || null;
    const timezone  = req.headers['x-vercel-ip-timezone']       || null;

    const countryNames = new Intl.DisplayNames(['fr'], { type: 'region' });
    const countryName  = country ? countryNames.of(country) : 'Inconnu';
    const locationLine = [city, region, countryName].filter(Boolean).join(', ') || 'Inconnue';

    const mapsLink = (latitude && longitude)
        ? `\n🗺️ *Carte IP :* [Voir sur Maps](https://maps.google.com/?q=${latitude},${longitude})`
        : '';

    // Infos visiteur
    const userAgent = req.headers['user-agent'] || 'Inconnu';
    const referer   = req.headers['referer'] || 'Accès direct';
    const language  = req.headers['accept-language']?.split(',')[0] || 'Inconnu';
    const page      = body?.page || req.query?.page || '/';

    const date = new Date().toLocaleString('fr-FR', {
        timeZone: timezone || 'Africa/Abidjan',
        dateStyle: 'short',
        timeStyle: 'medium'
    });

    // Détection appareil
    let device = 'Ordinateur 🖥️';
    if (/Mobile|Android|iPhone/i.test(userAgent)) device = 'Mobile 📱';
    else if (/Tablet|iPad/i.test(userAgent)) device = 'Tablette 📲';

    // Détection navigateur
    let browser = 'Inconnu';
    const edgeMatch    = userAgent.match(/Edg\/(\d+)/);
    const chromeMatch  = userAgent.match(/Chrome\/(\d+)/);
    const firefoxMatch = userAgent.match(/Firefox\/(\d+)/);
    if (edgeMatch)         browser = `Edge ${edgeMatch[1]}`;
    else if (chromeMatch)  browser = `Chrome ${chromeMatch[1]}`;
    else if (firefoxMatch) browser = `Firefox ${firefoxMatch[1]}`;
    else if (/Safari/i.test(userAgent)) browser = 'Safari';

    const message = `👀 *Nouvelle visite sur ton portfolio !*\n\n`
                  + `📅 *Date :* ${date}\n`
                  + `🌍 *Localisation :* ${locationLine}\n`
                  + `🌐 *IP :* \`${ip}\`\n`
                  + `🏳️ *Pays :* ${countryName} (${country || '?'})\n`
                  + (timezone ? `⏰ *Fuseau :* ${timezone}\n` : '')
                  + `📲 *Appareil :* ${device}\n`
                  + `🔍 *Navigateur :* ${browser}\n`
                  + `🗣️ *Langue :* ${language}\n`
                  + `🔗 *Référent :* ${referer}\n`
                  + `📄 *Page :* ${page}`
                  + mapsLink
                  + `\n\n📍 _Position GPS en attente..._`;

    try {
        const tgRes = await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                chat_id:                  CHAT_ID,
                text:                     message,
                parse_mode:               'Markdown',
                disable_web_page_preview: true
            })
        });

        const tgData = await tgRes.json();

        if (tgData.ok) {
            return res.status(200).json({ status: 'ok', type: 'standard' });
        } else {
            return res.status(500).json({ status: 'error', detail: tgData.description });
        }
    } catch (err) {
        return res.status(500).json({ status: 'error', detail: err.message });
    }
}
