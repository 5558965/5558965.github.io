#!/usr/bin/env python3
"""
Script pour traduire automatiquement index-en.html en anglais
"""
import re

# Dictionnaire de traductions FR → EN
translations = {
    # Navigation
    "À propos": "About",
    "Compétences": "Skills",
    "Expériences": "Experience",
    "Formation": "Education",
    "Recommandations": "Testimonials",
    "Contact": "Contact",
    
    # Hero section
    "Développeur Full Stack & DevOps Engineer": "Full Stack Developer & DevOps Engineer",
    "5 ans d'expérience en développement web": "5 years of experience in web development",
    "Spécialisé en React, Laravel, Node.js, Docker et AWS": "Specialized in React, Laravel, Node.js, Docker, and AWS",
    "Engagez-moi": "Hire Me",
    "Télécharger CV": "Download Resume",
    "Me contacter": "Contact Me",
    "Disponible pour mission": "Available for hire",
    
    # Section headers
    "À propos de moi": "About Me",
    "Mes compétences": "My Skills",
    "Mon parcours": "My Journey",
    "Ma formation": "My Education",
    "Mes projets": "My Projects",
    "Ce qu'ils disent de moi": "What They Say About Me",
    "Contactez-moi": "Contact Me",
    
    # About section
    "Passionné par la technologie": "Passionate about technology",
    "je suis développeur Full Stack": "I am a Full Stack Developer",
    "avec 5 ans d'expérience": "with 5 years of experience",
    "dans la création de solutions web innovantes": "in building innovative web solutions",
    "Je combine expertise technique et créativité": "I combine technical expertise and creativity",
    "pour transformer des idées en applications performantes": "to transform ideas into high-performance applications",
    
    # Skills
    "Développement Front-End": "Front-End Development",
    "Développement Back-End": "Back-End Development",
    "Bases de données": "Databases",
    "Outils & Méthodologies": "Tools & Methodologies",
    
    # Experience
    "Développeur Full Stack & Instructeur": "Full Stack Developer & Instructor",
    "Développeur Full Stack": "Full Stack Developer",
    "Développeur Web": "Web Developer",
    "Formateur en développement web": "Web Development Trainer",
    "Formation de": "Trained",
    "étudiants en développement web": "students in web development",
    "Développement de projets e-learning": "Development of e-learning projects",
    "Création de contenus pédagogiques": "Creation of educational content",
    "Support technique aux étudiants": "Technical support for students",
    "Administration système Linux": "Linux system administration",
    "Configuration de serveurs": "Server configuration",
    "Gestion des bases de données": "Database management",
    "Maintenance du réseau local": "Local network maintenance",
    "Support utilisateur": "User support",
    "Développé": "Developed",
    "Gestion": "Management",
    "Configuration": "Configuration",
    "Déploiement": "Deployment",
    "Mise en place": "Implementation",
    
    # Education
    "Licence en Informatique": "Bachelor's Degree in Computer Science",
    "Certification": "Certification",
    "Formation Intense En Cybersécurité": "Intensive Cybersecurity Training",
    "Principes de base de la mise en réseau": "Networking Basics",
    "Introduction à la cybersécurité": "Introduction to Cybersecurity",
    "Sécurité des terminaux": "Endpoint Security",
    "Modélisation de données": "Data Modeling",
    
    # Portfolio
    "Voir le projet": "View Project",
    "première plateforme officielle": "first official platform",
    "site de location et vente de véhicules": "vehicle rental and sales website",
    "Dashboard d'administration": "Administration Dashboard",
    "gestion des contenus": "content management",
    "utilisateurs et statistiques": "users and statistics",
    "Plateforme institutionnelle et événementielle": "Institutional and event platform",
    "Site conteneurisée": "Containerized website",
    "avec observabilité": "with observability",
    "Le Processing du deploiement": "Deployment processing",
    "jusqu'à la production": "to production",
    
    # Testimonials
    "Développeur web exceptionnel": "Exceptional web developer",
    "Son expertise technique": "His technical expertise",
    "sa capacité à livrer": "his ability to deliver",
    "des projets de haute qualité": "high-quality projects",
    "dans les délais": "on time",
    "sont remarquables": "are remarkable",
    "Co-Fondateur": "Co-Founder",
    "Fondateur": "Founder",
    "Directeur": "Director",
    
    # Contact
    "Envoyez-nous un message": "Send me a message",
    "Nom complet": "Full Name",
    "Votre nom": "Your name",
    "Email": "Email",
    "votre.email@exemple.com": "your.email@example.com",
    "Message": "Message",
    "Votre message...": "Your message...",
    "Je ne suis pas un robot": "I'm not a robot",
    "Envoyer": "Send",
    "Envoi...": "Sending...",
    
    # Footer
    "Tous droits réservés": "All rights reserved",
    "Suivez-moi": "Follow me",
    "Liens rapides": "Quick Links",
    "Accueil": "Home",
    
    # Dates/Locations
    "Abidjan, Côte d'Ivoire": "Abidjan, Ivory Coast",
    "Présent": "Present",
    "Actuellement": "Currently",
    "Septembre": "September",
    "Octobre": "October",
    "Novembre": "November",
    "Décembre": "December",
    "Janvier": "January",
    "Février": "February",
    "Mars": "March",
    "Avril": "April",
    "Mai": "May",
    "Juin": "June",
    "Juillet": "July",
    "Août": "August",
}

def translate_file():
    input_file = "c:/Users/abdou/Portfolio/index-en.html"
    
    print("📖 Reading index-en.html...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"🔄 Translating {len(translations)} terms...")
    
    # Count replacements
    count = 0
    for fr, en in translations.items():
        if fr in content:
            content = content.replace(fr, en)
            count += 1
            print(f"  ✓ '{fr}' → '{en}'")
    
    print(f"\n💾 Writing translated file...")
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Translation complete!")
    print(f"   {count}/{len(translations)} terms translated")
    print(f"   File: {input_file}")

if __name__ == "__main__":
    translate_file()
