#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix ALL remaining French texts in index-en.html - Complete cleanup
"""

# Read the file
with open('index-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define ALL remaining translations
translations = [
    # Skills section
    ("Technologies que je maîtrise", "Technologies I master"),
    
    # Education - Data Science section
    ("Définition du besoin et collecte des données", "Requirements definition and data collection"),
    ("Nettoyage et préparation des données", "Data cleaning and preparation"),
    ("Analyse exploratoire (EDA)", "Exploratory Data Analysis (EDA)"),
    ("Création d'indicateurs / métiers (KPI)", "Business indicators / KPIs creation"),
    ("Modélisation (optionnelle – selon besoin)", "Modeling (optional – as needed)"),
    ("Visualisation et storytelling", "Visualization and storytelling"),
    ("Automatisation et partage", "Automation and sharing"),
    
    # Education - Network & Telecom section
    ("Réseaux Informatiques", "Computer Networks"),
    ("Télécommunications", "Telecommunications"),
    ("Systèmes d'information", "Information Systems"),
    
    # Tags section
    ("Base de données", "Databases"),
    ("Outils & méthodologies", "Tools & Methodologies"),
    ("Outils et méthodologies", "Tools & Methodologies"),
    
    # Additional potential texts
    ("Mes compétences", "My skills"),
    ("Mes projets", "My projects"),
    ("Mon parcours", "My background"),
    ("Formation", "Education"),
    ("Expérience professionnelle", "Professional experience"),
]

changes = 0
for old_text, new_text in translations:
    count = content.count(old_text)
    if count > 0:
        content = content.replace(old_text, new_text)
        changes += count
        print(f"✅ Fixed {count}x: '{old_text}' → '{new_text}'")

# Write back
with open('index-en.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✨ Total changes: {changes}")
if changes > 0:
    print("✅ All remaining French texts fixed!")
else:
    print("ℹ️  No French texts found (already clean)")
