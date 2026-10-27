#!/usr/bin/env python3
"""
Script complet de traduction FR → EN pour index-en.html
"""

# Dictionnaire exhaustif de traductions
translations = {
    # Titres de poste
    "Informaticien": "IT Specialist",
    "Développeur Fullstack React.Js / Node.js": "Fullstack Developer React.js / Node.js",
    "Développeur Fullstack Next.js / Laravel": "Fullstack Developer Next.js / Laravel",
    "Développeur Full Stack & Instructeur": "Full Stack Developer & Instructor",
    "Développeur Full Stack": "Full Stack Developer",
    "Développeur Web": "Web Developer",
    
    # Dates et périodes
    "De Juil. 2026 – Aujourd'hui": "From Jul. 2026 – Present",
    "Aujourd'hui": "Present",
    "De novembre 2025 - mai 2026": "From November 2025 - May 2026",
    "De janvier 2025 – septembre 2025": "From January 2025 – September 2025",
    "De février 2024 – août 2024": "From February 2024 – August 2024",
    "De juillet 2023 – janvier 2024": "From July 2023 – January 2024",
    
    # Sections d'expérience
    "Expérience Professionnelle": "Professional Experience",
    
    # Compétences et domaines
    "Support & Assistance": "Support & Assistance",
    "Sécurité informatique": "IT Security",
    "Management des infrastructures": "Infrastructure Management",
    "Développement & Projets": "Development & Projects",
    "Veille & Amélioration continue": "Monitoring & Continuous Improvement",
    
    # Textes de témoignages
    "Claver est tout simplement exceptionnel": "Claver is simply exceptional",
    "Son travail sur Google Translate a révolutionné notre approche des langues": "His work on Google Translate revolutionized our approach to languages",
    "Un Développeur talentueux et visionnaire": "A talented and visionary developer",
    "Co-fondateur de Google": "Co-founder of Google",
    
    # Autres termes
    "Côte d'Ivoire": "Ivory Coast",
    "Abidjan": "Abidjan",
}

def translate_file():
    input_file = "c:/Users/abdou/Portfolio/index-en.html"
    
    print("📖 Lecture de index-en.html...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"🔄 Traduction de {len(translations)} termes supplémentaires...\n")
    
    count = 0
    for fr, en in translations.items():
        if fr in content:
            content = content.replace(fr, en)
            count += 1
            print(f"  ✓ '{fr}' → '{en}'")
    
    print(f"\n💾 Écriture du fichier mis à jour...")
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Traduction terminée!")
    print(f"   {count}/{len(translations)} termes traduits")

if __name__ == "__main__":
    translate_file()
