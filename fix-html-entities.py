#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix HTML entities and JS comments in French
"""

# Read the file
with open('index-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define translations (including HTML entities)
translations = [
    # HTML entities version
    ("Outils &amp; méthodologies", "Tools &amp; Methodologies"),
    
    # JS comments
    ("// Close le menu mobile après clic", "// Close mobile menu after click"),
    ("// Flèche scroll — après les stats, centrée", "// Scroll arrow — after stats, centered"),
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
    print("✅ HTML entities and comments fixed!")
else:
    print("ℹ️  No issues found")
