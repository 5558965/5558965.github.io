#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply same active button style to French version
"""

import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New CSS for active button
new_css = """.lang-btn.active {
  background: linear-gradient(135deg, #d82c2e 0%, #ff4757 100%) !important;
  border-color: white !important;
  box-shadow: 0 4px 20px rgba(216, 44, 46, 0.6) !important;
  position: relative;
  z-index: 2;
  transform: scale(1.05);
  font-weight: 700 !important;
}"""

# Find and replace active button CSS
pattern = r'\.lang-btn\.active \{[^}]+\}'
if re.search(pattern, content, re.DOTALL):
    content = re.sub(pattern, new_css, content, flags=re.DOTALL)
    print("✅ French version active button CSS enhanced")
    
    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ index.html updated!")
else:
    print("⚠️  Pattern not found in French version")
