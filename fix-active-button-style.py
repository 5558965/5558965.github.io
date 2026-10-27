#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix the active language button to be more visible
"""

# Read the file
with open('index-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the active button CSS to make it more prominent
old_css = """.lang-btn.active {
  background: linear-gradient(135deg, #d82c2e 0%, #ff4757 100%);
  border-color: white;
  box-shadow: 0 4px 15px rgba(216, 44, 46, 0.4);
  position: relative;
  z-index: 1;
}"""

new_css = """.lang-btn.active {
  background: linear-gradient(135deg, #d82c2e 0%, #ff4757 100%) !important;
  border-color: white !important;
  box-shadow: 0 4px 20px rgba(216, 44, 46, 0.6) !important;
  position: relative;
  z-index: 2;
  transform: scale(1.05);
  font-weight: 700 !important;
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    print("✅ Active button CSS enhanced (more visible)")
else:
    # Try simpler pattern
    import re
    pattern = r'\.lang-btn\.active \{[^}]+\}'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_css, content, flags=re.DOTALL)
        print("✅ Active button CSS enhanced (pattern match)")
    else:
        print("⚠️  Pattern not found")

# Write back
with open('index-en.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ index-en.html updated!")
