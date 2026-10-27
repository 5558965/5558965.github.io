#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync all JavaScript animations from French version to English version
"""

print("🔄 Synchronizing animations from index.html to index-en.html...")

# Read both files
with open('index.html', 'r', encoding='utf-8') as f:
    fr_content = f.read()

with open('index-en.html', 'r', encoding='utf-8') as f:
    en_content = f.read()

# Find all <script> blocks in French version (after </body> tag usually)
import re

# Extract all script blocks from French version
fr_scripts = re.findall(r'(<script>.*?</script>)', fr_content, re.DOTALL)
en_scripts = re.findall(r'(<script>.*?</script>)', en_content, re.DOTALL)

print(f"📊 Found {len(fr_scripts)} scripts in French version")
print(f"📊 Found {len(en_scripts)} scripts in English version")

# Check if English version is missing the progress bar animation
if 'IntersectionObserver' in fr_content and 'IntersectionObserver' not in en_content:
    print("⚠️  English version is missing IntersectionObserver animation!")
    print("✅ Adding animation scripts...")
    
    # Find the closing </body> tag
    body_close_pos = en_content.rfind('</body>')
    
    if body_close_pos > 0:
        # Extract animation scripts from French version
        # Find the skills animation script
        skills_script_start = fr_content.find('// Observer pour déclencher l\'animation')
        if skills_script_start > 0:
            # Find the <script> tag before
            script_start = fr_content.rfind('<script>', 0, skills_script_start)
            script_end = fr_content.find('</script>', skills_script_start) + len('</script>')
            
            skills_animation = fr_content[script_start:script_end]
            
            # Insert before </body>
            en_content = en_content[:body_close_pos] + '\n' + skills_animation + '\n' + en_content[body_close_pos:]
            
            print("✅ Added skills animation script")
        
        # Save updated English version
        with open('index-en.html', 'w', encoding='utf-8') as f:
            f.write(en_content)
        
        print("✅ index-en.html updated with animations!")
    else:
        print("❌ Could not find </body> tag")
else:
    print("ℹ️  Animations already synchronized or not found")

print("\n✨ Done!")
