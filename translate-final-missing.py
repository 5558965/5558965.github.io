#!/usr/bin/env python3
"""
Script FINAL pour traduire TOUS les textes manquants identifiés par l'utilisateur
"""

FINAL_TRANSLATIONS = {
    # ========== SECTIONS PRINCIPALES ==========
    "Ce que je peux faire pour vous": "What I Can Do For You",
    "Mes réalisations récentes": "My Recent Achievements",
    "Mes Projets": "My Projects",
    "Contactez-nous": "Contact Us",
    "Contactez-moi": "Contact Me",
    
    # ========== FOOTER & CONTACT ==========
    "N'hésitez pas à me contacter pour toute opportunité de collaboration": 
        "Feel free to contact me for any collaboration opportunity",
    
    "Suivez-nous sur les réseaux sociaux": "Follow us on social media",
    "Suivez-moi sur les réseaux sociaux": "Follow me on social media",
    
    "Téléphone": "Phone",
    "Localisation": "Location",
    "Liens rapides": "Quick Links",
    "Accueil": "Home",
    
    # ========== PORTFOLIO FILTERS ==========
    "Tous": "All",
    "Tous Web Mobile Design": "All Web Mobile Design",
    "Cloud & DevOps": "Cloud & DevOps",
    
    # ========== CTAs & BADGES ==========
    "Disponible pour nouvelles missions": "Available for new projects",
    "Disponible pour mission": "Available for hire",
    "Engagez-moi": "Hire Me",
    "Me contacter": "Contact Me",
    
    # ========== FORMULAIRE CONTACT ==========
    "Nom complet": "Full Name",
    "Votre nom": "Your name",
    "Votre email": "Your email",
    "Votre message": "Your message",
    "Envoyer le message": "Send message",
    "Envoi en cours...": "Sending...",
    "Message envoyé avec succès": "Message sent successfully",
    "Erreur lors de l'envoi": "Error sending message",
    
    # ========== NAVIGATION SUPPLÉMENTAIRE ==========
    "Retour en haut": "Back to top",
    "Voir plus": "See more",
    "Voir le projet": "View project",
    "Voir le certificat": "View certificate",
    "Télécharger CV": "Download Resume",
    "Télécharger le CV": "Download Resume",
    
    # ========== PROJETS & PORTFOLIO ==========
    "Projets récents": "Recent Projects",
    "Filtrer par": "Filter by",
    "Voir tous les projets": "View all projects",
    "Technologies utilisées": "Technologies used",
    "Date de réalisation": "Completion date",
    "Client": "Client",
    "Durée": "Duration",
    
    # ========== TÉMOIGNAGES ==========
    "Témoignages clients": "Client Testimonials",
    "Ce qu'ils disent": "What they say",
    "Avis": "Reviews",
    
    # ========== SERVICES ==========
    "Services proposés": "Services Offered",
    "Tarifs": "Pricing",
    "Demander un devis": "Request a quote",
    
    # ========== STATS & CHIFFRES ==========
    "ans d'expérience": "years of experience",
    "projets réalisés": "completed projects",
    "clients satisfaits": "satisfied clients",
    "lignes de code": "lines of code",
    
    # ========== DATES & TEMPS ==========
    "Actuellement": "Currently",
    "Présent": "Present",
    "En cours": "Ongoing",
    "Terminé": "Completed",
    
    # ========== DIVERS ==========
    "Découvrir": "Discover",
    "En savoir plus": "Learn more",
    "Plus d'informations": "More information",
    "Fermer": "Close",
    "Ouvrir": "Open",
    "Retour": "Back",
    "Suivant": "Next",
    "Précédent": "Previous",
}

def translate_file():
    file_path = "c:/Users/abdou/Portfolio/index-en.html"
    
    print("📖 Lecture de index-en.html...\n")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"🔄 Application des {len(FINAL_TRANSLATIONS)} traductions finales...\n")
    
    count = 0
    translated = []
    
    for fr_text, en_text in FINAL_TRANSLATIONS.items():
        if fr_text in content:
            content = content.replace(fr_text, en_text)
            count += 1
            translated.append(f"  ✓ '{fr_text}' → '{en_text}'")
    
    # Afficher toutes les traductions appliquées
    for t in translated:
        print(t)
    
    print(f"\n💾 Écriture du fichier mis à jour...")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Traductions finales appliquées!")
    print(f"   📊 {count}/{len(FINAL_TRANSLATIONS)} termes traduits")
    print(f"   📄 Fichier: {file_path}")
    
    if count == 0:
        print("\n⚠️  Aucune traduction appliquée - tous les textes sont déjà traduits!")
    else:
        print(f"\n🎉 {count} nouveaux textes traduits en anglais!")

if __name__ == "__main__":
    translate_file()
