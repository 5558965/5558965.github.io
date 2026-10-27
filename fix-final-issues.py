#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix final issues in index-en.html:
1. Image path: "Management des infrastructures" → "Gestion des infrastructures"
2. Button text: "Nous écrire" → "Write to us"
3. Button text: "Voir la carte" → "View map"
"""

import re

# Read the file
with open('index-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Count changes
changes = 0

# 1. Fix image paths: "Management des infrastructures" → "Gestion des infrastructures"
old_patterns = [
    'images/webp/Management des infrastructures.webp',
    'images/Management des infrastructures.jpeg',
]
new_patterns = [
    'images/webp/Gestion des infrastructures.webp',
    'images/Gestion des infrastructures.jpeg',
]

for old, new in zip(old_patterns, new_patterns):
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        changes += count
        print(f"✅ Fixed {count}x: {old} → {new}")

# 2. Fix button text: "Nous écrire" → "Write to us"
old_text = 'Nous écrire'
new_text = 'Write to us'
count = content.count(old_text)
if count > 0:
    content = content.replace(old_text, new_text)
    changes += count
    print(f"✅ Fixed {count}x: '{old_text}' → '{new_text}'")

# 3. Fix button text: "Voir la carte" → "View map"
old_text = 'Voir la carte'
new_text = 'View map'
count = content.count(old_text)
if count > 0:
    content = content.replace(old_text, new_text)
    changes += count
    print(f"✅ Fixed {count}x: '{old_text}' → '{new_text}'")

# Write back
with open('index-en.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✨ Total changes: {changes}")
print("✅ index-en.html fixed successfully!")
