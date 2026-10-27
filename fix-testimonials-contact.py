#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix testimonials and contact texts still in French
"""

# Read the file
with open('index-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define all translations
translations = [
    # Contact - Phone section
    ("Du lundi au vendredi", "Monday to Friday"),
    ("08h00 - 18h00", "8:00 AM - 6:00 PM"),
    
    # Contact - Location
    ("Rue 170, Cocody Riviera-Bonoumin", "170 Street, Cocody Riviera-Bonoumin"),
    
    # Experience - IT Specialist stats
    ("utilisateurs gérés", "managed users"),
    ("équipements dans le parc informatique", "equipment in IT fleet"),
    
    # Testimonials - Jack Dorsey (Twitter)
    ("L'esprit le plus créatif que j'ai rencontré. Le Retweet qu'il a développé est devenu une Fonctionnalité centrale de Twitter. Un génie du code.",
     "The most creative mind I've ever met. The Retweet feature he developed became a core part of Twitter. A coding genius."),
    
    # Testimonials - Mark Zuckerberg (Facebook)
    ("Travailler avec Claver a été une révélation. Son implémentation du bouton Share a considérablement augmenté notre engagement. Un professionnel hors pair.",
     "Working with Claver was a revelation. His implementation of the Share button significantly increased our engagement. An outstanding professional."),
    
    # Additional potential texts
    ("hors pair", "outstanding"),
    ("considérablement augmenté", "significantly increased"),
    ("a été une révélation", "was a revelation"),
]

changes = 0
for old_text, new_text in translations:
    count = content.count(old_text)
    if count > 0:
        content = content.replace(old_text, new_text)
        changes += count
        print(f"✅ Fixed {count}x: '{old_text[:50]}...' → '{new_text[:50]}...'")

# Write back
with open('index-en.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✨ Total changes: {changes}")
if changes > 0:
    print("✅ Testimonials and contact texts fixed!")
else:
    print("ℹ️  No French texts found")
