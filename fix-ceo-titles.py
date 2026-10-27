#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix CEO titles from French to English
"""

# Read the file
with open('index-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix CEO titles
translations = [
    ("PDG de Twitter", "CEO of Twitter"),
    ("PDG de Facebook", "CEO of Facebook"),
    ("PDG de Google", "CEO of Google"),
    ("PDG de", "CEO of"),  # Catch-all for any other PDG
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
    print("✅ CEO titles fixed!")
else:
    print("ℹ️  No PDG titles found")
