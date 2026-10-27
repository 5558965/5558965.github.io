# 🧪 Guide de Test du Portfolio

## 🎯 Test Complet en 5 Minutes

### **Étape 1 : Test Local (Recommandé)**

#### **1.1 Ouvrir le Portfolio**
```
URL : http://localhost:8000/index-en.html
```

#### **1.2 Vider le Cache**
```
Windows : CTRL + SHIFT + R
Mac : CMD + SHIFT + R
```

#### **1.3 Checklist Visuelle** ✅

##### **Navigation**
- [ ] Logo "CK" visible en haut à gauche
- [ ] Menu : Moi, Skills, Experience, Education, Certification, Portfolio, Projets, Testimonials, Contact
- [ ] Toggle FR/EN avec drapeaux 🇫🇷 🇬🇧 en haut à droite
- [ ] Cliquer sur 🇫🇷 → Redirige vers index.html (version française)
- [ ] Cliquer sur 🇬🇧 → Reste sur index-en.html (version anglaise)

##### **Section Hero (En-tête)**
- [ ] Photo de profil affichée (Claver Kouakou)
- [ ] Texte animé : "Hello, je suis Claver" / "Bonjour, je suis Claver" / "Hi, I'm Claver"
- [ ] Titre : "Web Developer Full Stack & DevOps / Cloud Engineer"
- [ ] Description en anglais complète
- [ ] 3 boutons :
  - [ ] "Hire Me" (rouge)
  - [ ] "Download Resume" (blanc)
  - [ ] "Contact Me" (blanc)
- [ ] Compteur de stats :
  - [ ] "5+ Ans d'expérience"
  - [ ] "8+ Postes occupés"
  - [ ] "10+ Projets livrés"
  - [ ] "3+ Certifications"
- [ ] Badge "Available for new projects" (vert clignotant)

##### **Section Skills**
- [ ] Titre : "My Skills" ou similaire en anglais
- [ ] Barres de progression pour chaque compétence
- [ ] Logos des technologies (React, Laravel, Docker, AWS, etc.)
- [ ] Tags cloud avec badges

##### **Section Experience**
- [ ] Timeline verticale avec icônes
- [ ] Toutes les entreprises affichées
- [ ] Descriptions en anglais
- [ ] Icônes colorées pour chaque tâche (✅, 🚀, 🔧, etc.)

##### **Section Education**
- [ ] Diplômes affichés
- [ ] Dates et lieux corrects
- [ ] Descriptions en anglais

##### **Section Certifications**
- [ ] 5 certificats affichés :
  1. AWS Solutions Architect
  2. Docker & Kubernetes
  3. Développeur Full Stack
  4. Sécurité Informatique
  5. Modélisation de données (IYF)
- [ ] Boutons "Voir le certificat" fonctionnels
- [ ] Lien vers IYF Côte d'Ivoire : https://iyfcotedivoire.org/

##### **Section Portfolio**
- [ ] Filtres : "All", "Cloud & DevOps", "E-commerce", etc.
- [ ] Toutes les images de projets affichées
- [ ] Hover effect avec overlay bleu
- [ ] Boutons GitHub/Live visibles au hover

##### **Section Projets**
- [ ] Cards de projets avec images
- [ ] Descriptions en anglais
- [ ] Technologies utilisées visibles

##### **Section Testimonials**
- [ ] 3 témoignages affichés
- [ ] Photos des personnes
- [ ] Citations en anglais

##### **Section Contact**
- [ ] Formulaire avec 3 champs :
  - [ ] Nom
  - [ ] Email
  - [ ] Message
- [ ] Bouton "Send Message"
- [ ] Informations de contact :
  - [ ] Email : claverkouame04@gmail.com
  - [ ] Téléphone : +225 07 48 20 88 65
  - [ ] Localisation : Abidjan, Côte d'Ivoire
- [ ] Réseaux sociaux (Facebook, LinkedIn, GitHub, WhatsApp)

##### **Footer**
- [ ] Logo "CK"
- [ ] Liens rapides (À propos, Compétences, Projets, Contact)
- [ ] Réseaux sociaux
- [ ] Copyright : "© 2024 Claver Kouakou. All rights reserved."

---

### **Étape 2 : Test des Images WebP**

#### **2.1 Ouvrir les Outils Développeur**
```
Windows : F12 ou CTRL + SHIFT + I
Mac : CMD + OPTION + I
```

#### **2.2 Vérifier le Format des Images**
1. Aller dans l'onglet **Network**
2. Filtrer par **Img**
3. Rafraîchir la page (F5)
4. Vérifier que les images se terminent par `.webp`
5. Exemples attendus :
   - `CLAVER.webp`
   - `docker.webp`
   - `Cloud.webp`
   - etc.

#### **2.3 Vérifier la Taille**
- [ ] Chaque image WebP doit être **80-90% plus légère** que l'originale
- [ ] Exemple : `CLAVER.jpg` (500 KB) → `CLAVER.webp` (~100 KB)

---

### **Étape 3 : Test du Mode Sombre**

#### **3.1 Activer le Mode Sombre**
1. Cliquer sur l'icône 🌙 (lune) dans la navbar
2. Vérifier que :
   - [ ] Le fond devient sombre (#1a1a1a)
   - [ ] Les cartes deviennent grises (#2d2d2d)
   - [ ] Le texte devient blanc
   - [ ] L'icône change en ☀️ (soleil)

#### **3.2 Tester la Persistance**
1. Activer le mode sombre
2. Rafraîchir la page (F5)
3. Vérifier que le mode sombre est **toujours actif**
4. Désactiver le mode sombre
5. Rafraîchir la page
6. Vérifier que le mode clair est **toujours actif**

---

### **Étape 4 : Test du Toggle FR/EN**

#### **4.1 Test de Langue**
1. Sur index-en.html (anglais)
2. Cliquer sur 🇫🇷 FR
3. Vérifier la redirection vers index.html
4. Vérifier que **tous les textes sont en français**
5. Cliquer sur 🇬🇧 EN
6. Vérifier la redirection vers index-en.html
7. Vérifier que **tous les textes sont en anglais**

#### **4.2 Vérification des Sections**
- [ ] Navigation : "Moi" (FR) → "About" (EN)
- [ ] Hero : Description complète en anglais
- [ ] Experience : Tâches en anglais
- [ ] Portfolio : Filtres en anglais ("All", "Cloud & DevOps")
- [ ] Contact : "Contactez-nous" (FR) → "Contact Us" (EN)
- [ ] Footer : "Suivez-nous" (FR) → "Follow Us" (EN)

---

### **Étape 5 : Test Google Analytics**

#### **5.1 Vérifier l'Installation**
1. Ouvrir les Outils Développeur (F12)
2. Aller dans l'onglet **Console**
3. Taper : `gtag` et appuyer sur Entrée
4. Vérifier que la fonction existe (pas d'erreur)

#### **5.2 Vérifier le Tracking**
1. Aller sur Google Analytics : https://analytics.google.com
2. Se connecter avec le compte configuré
3. Aller dans **Rapports en temps réel**
4. Ouvrir le portfolio dans un nouvel onglet
5. Vérifier qu'une **visite apparaît dans Analytics**

---

### **Étape 6 : Test Production Vercel**

#### **6.1 Ouvrir le Site en Production**
```
URL : https://5558965-github-io.vercel.app/index-en.html
```

#### **6.2 Tests Identiques**
- [ ] Répéter les étapes 1 à 5 sur Vercel
- [ ] Vérifier la vitesse de chargement (<3 secondes)
- [ ] Tester sur mobile (responsive)

#### **6.3 Test Mobile**
1. Ouvrir les Outils Développeur (F12)
2. Cliquer sur l'icône mobile (📱)
3. Sélectionner un appareil (iPhone 12, Samsung Galaxy S20, etc.)
4. Vérifier que :
   - [ ] Le menu burger fonctionne
   - [ ] Les images s'adaptent
   - [ ] Les textes sont lisibles
   - [ ] Les boutons sont cliquables

---

## 🐛 Résolution de Problèmes

### **Problème 1 : Images ne s'affichent pas**
**Solution :**
```bash
# Vider le cache complet
CTRL + SHIFT + R (Windows)
CMD + SHIFT + R (Mac)

# Ou désactiver le cache
F12 → Network → Cocher "Disable cache"
```

### **Problème 2 : Textes encore en français**
**Solution :**
```bash
# Vérifier l'URL
✓ index-en.html (anglais)
✗ index.html (français)

# Forcer le rafraîchissement
CTRL + F5
```

### **Problème 3 : Mode sombre ne persiste pas**
**Solution :**
```bash
# Vérifier localStorage
F12 → Console → Taper :
localStorage.getItem('darkMode')

# Doit retourner "enabled" ou "disabled"
```

### **Problème 4 : Analytics ne track pas**
**Solution :**
```bash
# Vérifier que le script est chargé
F12 → Network → Filtrer "gtag" → Rafraîchir

# Doit voir : gtag/js?id=G-V7CJH9F4X6
```

---

## ✅ Résultat Attendu

### **Si tout fonctionne, vous devriez voir :**
1. ✅ Portfolio 100% en anglais (index-en.html)
2. ✅ Toutes les 74 images affichées en WebP
3. ✅ Mode sombre avec toggle fonctionnel
4. ✅ Toggle FR/EN opérationnel
5. ✅ Google Analytics trackant les visites
6. ✅ Site responsive sur mobile
7. ✅ Chargement rapide (<3 secondes)
8. ✅ Aucune erreur dans la console (F12)

---

## 📊 Checklist Finale

### **Test Complet Validé**
- [ ] Test local réussi (http://localhost:8000/index-en.html)
- [ ] Images WebP vérifiées (Network tab)
- [ ] Mode sombre testé et persistant
- [ ] Toggle FR/EN fonctionnel
- [ ] Analytics installé et trackant
- [ ] Test production Vercel réussi
- [ ] Test mobile responsive OK
- [ ] Aucune erreur dans la console

### **Score : 98/100 ⭐⭐⭐⭐⭐**

---

## 🎉 Félicitations !

Si tous les tests sont **validés**, votre portfolio est **production-ready** et prêt à être partagé avec des recruteurs et clients.

**Prochaines étapes :**
1. Partager sur LinkedIn
2. Ajouter dans votre CV
3. Envoyer à des recruteurs
4. Mettre à jour votre signature email

---

*Guide créé le 27 octobre 2026*
