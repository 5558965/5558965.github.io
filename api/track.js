// api/track.js — Vercel Serverless Function
// Envoie une notification Telegram à chaque visite du portfolio

const BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN || '8729026440:AAEgfIN9kUH-W8pEWlXJfXFj306a8g-CQMo';
const CHAT_ID   = process.env.TELEGRAM_CHAT_ID   || '6103078174';

// Rate limiting simple en mémoire (reset à chaque cold start Vercel)
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

    // Rate limiting
    const now = Date.now();
    const lastVisit = visited.get(ip);
    if (lastVisit && (now - lastVisit) < COOLDOWN_MS) {
        return res.status(200).json({ status: 'throttled' });
    }
    visited.set(ip, now);

    // Infos visiteur
    const userAgent = req.headers['user-agent'] || 'Inconnu';
    const referer   = req.headers['referer'] || 'Accès direct';
    const language  = req.headers['accept-language']?.split(',')[0] || 'Inconnu';
    const page      = req.body?.page || req.query?.page || '/';

    const date = new Date().toLocaleString('fr-FR', {
        timeZone: 'Africa/Abidjan',
        dateStyle: 'short',
        timeStyle: 'medium'
    });

    // Détection appareil
    let device = 'Ordinateur 🖥️';
    if (/Mobile|Android|iPhone/i.test(userAgent)) device = 'Mobile 📱';
    else if (/Tablet|iPad/i.test(userAgent)) device = 'Tablette 📲';

    // Détection navigateur
    let browser = 'Inconnu';
    const chromeMatch  = userAgent.match(/Chrome\/(\d+)/);
    const firefoxMatch = userAgent.match(/Firefox\/(\d+)/);
    const edgeMatch    = userAgent.match(/Edg\/(\d+)/);
    if (edgeMatch)    browser = `Edge ${edgeMatch[1]}`;
    else if (chromeMatch)  browser = `Chrome ${chromeMatch[1]}`;
    else if (firefoxMatch) browser = `Firefox ${firefoxMatch[1]}`;
    else if (/Safari/i.test(userAgent)) browser = 'Safari';

    // Géolocalisation (service gratuit, sans clé)
    let country = 'Inconnu', city = 'Inconnu';
    try {
        const geoRes = await fetch(`https://ipapi.co/${ip}/json/`);
        if (geoRes.ok) {
            const geo = await geoRes.json();
            country = geo.country_name || 'Inconnu';
            city    = geo.city || 'Inconnu';
        }
    } catch (_) { /* silencieux */ }

    // Message Telegram
    const message = `👀 *Nouvelle visite sur ton portfolio !*\n\n`
                  + `📅 *Date :* ${date}\n`
                  + `🌍 *Localisation :* ${city}, ${country}\n`
                  + `🌐 *IP :* \`${ip}\`\n`
                  + `📲 *Appareil :* ${device}\n`
                  + `🔍 *Navigateur :* ${browser}\n`
                  + `🗣️ *Langue :* ${language}\n`
                  + `🔗 *Référent :* ${referer}\n`
                  + `📄 *Page :* ${page}`;

    // Envoi Telegram
    try {
        const tgRes = await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                chat_id:    CHAT_ID,
                text:       message,
                parse_mode: 'Markdown'
            })
        });

        const tgData = await tgRes.json();

        if (tgData.ok) {
            return res.status(200).json({ status: 'ok', message: 'Notification envoyée' });
        } else {
            return res.status(500).json({ status: 'error', detail: tgData.description });
        }
    } catch (err) {
        return res.status(500).json({ status: 'error', detail: err.message });
    }
}
