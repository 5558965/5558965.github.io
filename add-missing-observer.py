#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add the missing IntersectionObserver from French to English version
"""

import re

print("🔍 Finding missing IntersectionObserver...")

# Read both files
with open('index.html', 'r', encoding='utf-8') as f:
    fr_content = f.read()

with open('index-en.html', 'r', encoding='utf-8') as f:
    en_content = f.read()

# Find all IntersectionObserver blocks in French version
fr_observers = re.findall(r'(const observer = new IntersectionObserver.*?}\);)', fr_content, re.DOTALL)

print(f"📊 Found {len(fr_observers)} observers in French version")

# Find which observer is missing by checking for specific patterns
for i, observer in enumerate(fr_observers):
    print(f"\n🔍 Observer {i+1}:")
    if 'animateSkills' in observer:
        print("   → Skills animation observer")
        if 'animateSkills' not in en_content:
            print("   ❌ MISSING in English version!")
            # Add it before </body>
            body_pos = en_content.rfind('</body>')
            script_block = f"\n<script>\n    document.addEventListener('DOMContentLoaded', function() {{\n        {observer}\n        observer.observe(document.getElementById('skills'));\n    }});\n</script>\n"
            en_content = en_content[:body_pos] + script_block + en_content[body_pos:]
            print("   ✅ Added to English version")
    
    elif 'new-item' in observer or 'timeline' in observer.lower():
        print("   → Timeline/Experience animation observer")
        if 'new-item' not in en_content and 'timeline' not in en_content.lower():
            print("   ❌ MISSING in English version!")
            # Add it
            body_pos = en_content.rfind('</body>')
            script_block = f"\n<script>\n    document.addEventListener('DOMContentLoaded', function() {{\n        {observer}\n        const items = document.querySelectorAll('.new-item:not(.new-item-empty)');\n        items.forEach(item => observer.observe(item));\n    }});\n</script>\n"
            en_content = en_content[:body_pos] + script_block + en_content[body_pos:]
            print("   ✅ Added to English version")
        else:
            print("   ✅ Already present in English version")

# Save updated file
with open('index-en.html', 'w', encoding='utf-8') as f:
    f.write(en_content)

print("\n✨ Done! English version updated.")
