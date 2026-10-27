#!/usr/bin/env python3
"""
Script EXHAUSTIF de traduction FR → EN
Analyse complète et traduction de TOUS les textes français restants
"""
import re

# Dictionnaire EXHAUSTIF de traductions
TRANSLATIONS = {
    # ========== HERO / DESCRIPTION ==========
    "Developer Fullstack avec 5 ans d'Expérience en conception et développement de site web et application": 
        "Fullstack Developer with 5 years of experience in website and application design and development",
    
    "Spécialisé React.js / TypeScript côté front et Laravel / Node.js côté back": 
        "Specialized in React.js / TypeScript on the frontend and Laravel / Node.js on the backend",
    
    "Je conçois et déploie des sites et applications fiables en production": 
        "I design and deploy reliable websites and applications in production",
    
    "conteneurisation Docker, pipelines CI/CD automatisés": 
        "Docker containerization, automated CI/CD pipelines",
    
    "observabilité 3-piliers": "3-pillar observability",
    
    # ========== EXPÉRIENCES - DÉTAILS ==========
    # AELITE
    "Implementation des politiques de sécurité": "Implementation of security policies",
    "access management and protection of sensitive data": "access management and protection of sensitive data",
    
    # Tâches détaillées
    "Functional Odoo": "Odoo Functional",
    "Configuration and analyse des modules": "Configuration and analysis of modules",
    "Assistance aux utilisateurs": "User assistance",
    "Customer assistance": "Customer assistance",
    
    "Developed la documentation technique en ligne de l'ensemble des produits de l'entreprise, avec système de commentaires et partage intégré":
        "Developed the online technical documentation for all company products, with integrated comment and sharing system",
    
    "assistés": "assisted",
    "configurés et déployés": "configured and deployed",
    
    # GoMyCode
    "Animation d'ateliers Coding, Robotique, 3D et Intelligence Artificielle pour les enfants":
        "Facilitation of Coding, Robotics, 3D and Artificial Intelligence workshops for children",
    
    "Développement et maintenance de sites web":
        "Website development and maintenance",
    
    "Apprentissage des technologies web (Développement frontend en HTML, CSS et JS)":
        "Learning web technologies (Frontend development in HTML, CSS and JS)",
    
    "Analyse des besoins utilisateurs et création d'un cahier des charges technique":
        "Analysis of user needs and creation of technical specifications",
    
    # ========== EDUCATION / FORMATION ==========
    "Management des menaces, attaques et vulnérabilités":
        "Threat, attack and vulnerability management",
    
    "Conception et mise en œuvre d'un code sécurisé":
        "Design and implementation of secure code",
    
    "Conception et mise en œuvre de la cryptographie":
        "Design and implementation of cryptography",
    
    "Management des identités et des accès et la sécurité des réseaux":
        "Identity and access management and network security",
    
    "Conception et mise en œuvre de la sécurité physique et du cloud":
        "Design and implementation of physical and cloud security",
    
    "Conception et mise en œuvre des terminaux":
        "Endpoint design and implementation",
    
    "Opérations et réponse aux incidents":
        "Operations and incident response",
    
    "Gouvernance, risques et conformité":
        "Governance, risk and compliance",
    
    # ========== SERVICES ==========
    "Applications web sur mesure": "Custom web applications",
    
    "Conception et développement d'applications web personnalisées adaptées à vos besoins métiers : gestion, e-commerce, tableaux de bord":
        "Design and development of custom web applications tailored to your business needs: management, e-commerce, dashboards",
    
    "déploiement & mise en ligne": "Deployment & go-live",
    
    "Server configuration, déploiement sur hébergement mutualisé ou VPS, Conteneurisation Docker, CI/CD automatisé (GitLab / GitHub Actions), observabilité 3-piliers (logs, métriques, traces), alerting SRE et tests de charge — pour des applications fiables en production et gestion de domaines":
        "Server configuration, deployment on shared hosting or VPS, Docker containerization, automated CI/CD (GitLab / GitHub Actions), 3-pillar observability (logs, metrics, traces), SRE alerting and load testing — for reliable production applications and domain management",
    
    # ========== PROJETS ==========
    "Administration Dashboard de CÔTIÈRE MEDIA GROUP — content management, users and statistics":
        "CÔTIÈRE MEDIA GROUP Administration Dashboard — content management, users and statistics",
    
    "de CÔTIÈRE MEDIA GROUP — gestion des contenus":
        "of CÔTIÈRE MEDIA GROUP — content",
    
    # ========== MOTS ISOLÉS FRÉQUENTS ==========
    "Développé": "Developed",
    "développement": "development",
    "Conception": "Design",
    "conception": "design",
    "déploiement": "deployment",
    "Assistance": "Assistance",
    "assistance": "assistance",
    "Gestion": "Management",
    "gestion": "management",
    "Administration": "Administration",
    "administration": "administration",
    "maintenance": "maintenance",
    "Diagnostic": "Diagnosis",
    "résolution": "resolution",
    "Suivi": "Monitoring",
    "proposition": "proposing",
    "moderniser": "modernize",
    "analyse": "analysis",
    "assistés": "assisted",
    "configurés": "configured",
    "déployés": "deployed",
    "avec système de": "with a",
    "mise en œuvre": "implementation",
    "cahier des charges": "specifications",
    "besoins métiers": "business needs",
    "tableaux de bord": "dashboards",
    "hébergement mutualisé": "shared hosting",
    "tests de charge": "load testing",
    "fiables en production": "reliable in production",
}

def clean_extra_spaces(text):
    """Nettoyer les espaces multiples"""
    return re.sub(r'\s+', ' ', text)

def translate_content(content):
    """Traduire le contenu avec toutes les traductions"""
    
    print(f"🔄 Application de {len(TRANSLATIONS)} traductions...\n")
    
    count = 0
    for fr_text, en_text in TRANSLATIONS.items():
        if fr_text in content:
            content = content.replace(fr_text, en_text)
            count += 1
            # Afficher seulement les premières traductions pour ne pas surcharger
            if count <= 20:
                preview_fr = fr_text[:60] + "..." if len(fr_text) > 60 else fr_text
                preview_en = en_text[:60] + "..." if len(en_text) > 60 else en_text
                print(f"  ✓ '{preview_fr}' → '{preview_en}'")
    
    if count > 20:
        print(f"  ... et {count - 20} autres traductions")
    
    return content, count

def main():
    file_path = "c:/Users/abdou/Portfolio/index-en.html"
    
    print("📖 Lecture de index-en.html...\n")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Traduire
    content, count = translate_content(content)
    
    # Nettoyer les espaces
    content = clean_extra_spaces(content)
    
    print(f"\n💾 Écriture du fichier traduit...")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Traduction exhaustive terminée!")
    print(f"   📊 {count}/{len(TRANSLATIONS)} termes traduits")
    print(f"   📄 Fichier: {file_path}")
    print(f"\n🎯 Tous les textes français devraient maintenant être en anglais!")

if __name__ == "__main__":
    main()
