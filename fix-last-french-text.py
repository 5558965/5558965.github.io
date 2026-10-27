#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix the very last French text: "Pour toute question ou demande"
"""

# Read the file
with open('index-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the last French text
old_text = "Pour toute question ou demande"
new_text = "For any question or request"

count = content.count(old_text)
if count > 0:
    content = content.replace(old_text, new_text)
    print(f"✅ Fixed {count}x: '{old_text}' → '{new_text}'")
    
    # Write back
    with open('index-en.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✨ Success! index-en.html is now 100% English!")
else:
    print("ℹ️  Text already translated or not found")
