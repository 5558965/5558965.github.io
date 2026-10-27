#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix ALL remaining French texts in index-en.html:
1. Stats counters in hero section
2. Footer text
"""

# Read the file
with open('index-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define all translations
translations = [
    # Stats counters in hero section
    ("Ans d'expérience", "Years of experience"),
    ("ANS D'EXPÉRIENCE", "YEARS OF EXPERIENCE"),
    ("Postes occupés", "Positions held"),
    ("POSTES OCCUPÉS", "POSITIONS HELD"),
    ("Projets livrés", "Projects delivered"),
    ("PROJETS LIVRÉS", "PROJECTS DELIVERED"),
    ("Certifications", "Certifications"),  # Same in both languages
    ("CERTIFICATIONS", "CERTIFICATIONS"),
    
    # Footer
    ("Conçu avec", "Crafted with"),
    ("et beaucoup de café", "and lots of coffee"),
    
    # Additional potential French texts
    ("Développeur Web Full Stack passionné", "Passionate Full Stack Web Developer"),
    ("Web Developer Full Stack passionné", "Passionate Full Stack Web Developer"),
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
print("✅ All remaining French texts fixed!")
