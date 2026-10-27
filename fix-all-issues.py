#!/usr/bin/env python3
"""
Script pour corriger TOUS les problèmes d'index-en.html
1. Ajouter espaces manquants dans src
2. Corriger les noms de fichiers d'images
3. Traduire tous les textes restants
"""
import re

def fix_images_spacing(content):
    """Ajouter espace avant src= si manquant"""
    # Pattern: title="..."src= → title="..." src=
    content = re.sub(r'title="([^"]*)"src=', r'title="\1" src=', content)
    # Pattern: alt="..."src= → alt="..." src=
    content = re.sub(r'alt="([^"]*)"src=', r'alt="\1" src=', content)
    return content

def fix_image_paths(content):
    """Corriger les chemins d'images traduits vers les fichiers français originaux"""
    replacements = {
        'images/IT Security.jpg': 'images/Sécurité informatique.jpg',
        'images/webp/IT Security.webp': 'images/webp/Sécurité informatique.webp',
        'images/Infrastructure Management.jpeg': 'images/Gestion des infrastructures.jpeg',
        'images/webp/Infrastructure Management.webp': 'images/webp/Gestion des infrastructures.webp',
        'images/Development & Projects.png': 'images/Développement & Projets.png',
        'images/webp/Development & Projects.webp': 'images/webp/Développement & Projets.webp',
        'images/Monitoring & Continuous Improvement.png': 'images/Veille & Amélioration continue.png',
        'images/webp/Monitoring & Continuous Improvement.webp': 'images/webp/Veille & Amélioration continue.webp',
    }
    
    for wrong, correct in replacements.items():
        content = content.replace(wrong, correct)
    
    return content

def translate_remaining_text(content):
    """Traduire tous les textes restants"""
    translations = {
        # Textes détaillés des expériences
        "Diagnostic et résolution des incidents techniques": "Diagnosis and resolution of technical incidents",
        "assistance de proximité aux utilisateurs": "user support and assistance",
        "Mise en œuvre des politiques de sécurité": "Implementation of security policies",
        "gestion des accès et protection des données sensibles": "access management and protection of sensitive data",
        "Administration du parc informatique": "IT infrastructure administration",
        "maintenance préventive et curative des équipements réseau": "preventive and corrective maintenance of network equipment",
        "Conception et déploiement d'outils internes": "Design and deployment of internal tools",
        "pour optimiser les processus métiers": "to optimize business processes",
        "Suivi des évolutions technologiques": "Monitoring technological developments",
        "et proposition de solutions pour moderniser le SI": "and proposing solutions to modernize the IS",
        
        # Projets
        "Developed CÔTIÈRE MEDIA GROUP, first official platform": "Developed CÔTIÈRE MEDIA GROUP, first official platform",
        "des villes et villages du littoral ivoirien": "of coastal towns and villages in Ivory Coast",
        "un site de location et vente de véhicules": "a vehicle rental and sales website",
        "en Côte d'Ivoire": "in Ivory Coast",
        "gestion des contenus, utilisateurs et statistiques": "content, user and statistics management",
        "du Festival National de l'Attiéké de Côte d'Ivoire": "of the National Attiéké Festival of Ivory Coast",
        "avec observabilité 3-piliers": "with 3-pillar observability",
        "CI/CD GitLab et alerting SRE": "GitLab CI/CD and SRE alerting",
        "jusqu'à la production": "to production",
        
        # Sections
        "Mes compétences": "My Skills",
        "Mon parcours": "My Experience",
        "Ma formation": "My Education",
        "Mes projets": "My Projects",
        
        # Actions/Verbes
        "Developed": "Developed",
        "Administrateur": "Administrator",
        "Fonctionnel": "Functional",
        "Configuration et": "Configuration and",
        "Assistance des clients": "Customer assistance",
        
        # Pays/Lieux
        "Ivory Coast": "Ivory Coast",
        "Abidjan": "Abidjan",
        
        # Dates supplémentaires
        "De Nov. 2025 - May 2026": "From Nov. 2025 - May 2026",
        "De Jan. 2025 – Sept. 2025": "From Jan. 2025 – Sept. 2025",
        "De Feb. 2024 – Aug. 2024": "From Feb. 2024 – Aug. 2024",
        "De Jul. 2023 – Jan. 2024": "From July 2023 – Jan. 2024",
        "De July 2023 – Jan. 2024": "From July 2023 – Jan. 2024",
    }
    
    for fr, en in translations.items():
        content = content.replace(fr, en)
    
    return content

def main():
    file_path = "c:/Users/abdou/Portfolio/index-en.html"
    
    print("📖 Lecture de index-en.html...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("\n🔧 Correction des problèmes...")
    
    # 1. Corriger les espaces manquants
    print("  1️⃣  Ajout espaces avant src= ...")
    content = fix_images_spacing(content)
    
    # 2. Corriger les chemins d'images
    print("  2️⃣  Correction chemins d'images ...")
    content = fix_image_paths(content)
    
    # 3. Traduire textes restants
    print("  3️⃣  Traduction textes restants ...")
    content = translate_remaining_text(content)
    
    print("\n💾 Écriture du fichier corrigé...")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n✅ Toutes les corrections appliquées!")
    print("   • Espaces ajoutés dans balises img")
    print("   • Chemins d'images corrigés")
    print("   • Traductions complétées")

if __name__ == "__main__":
    main()
