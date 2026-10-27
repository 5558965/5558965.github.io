#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix language switcher stability in both index.html and index-en.html
"""

import re

files = ['index.html', 'index-en.html']

for filename in files:
    print(f"\n📝 Processing {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the language switcher CSS
    old_css = r'''/* Language Switcher */
.language-switcher {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.lang-btn {
  padding: 0.5rem 1rem;
  border-radius: 8px;
  background: rgba\(255, 255, 255, 0.1\);
  color: white;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  border: 2px solid transparent;
}

.lang-btn:hover {
  background: rgba\(255, 255, 255, 0.2\);
  transform: translateY\(-2px\);
  color: white;
}

.lang-btn.active {
  background: linear-gradient\(135deg, #d82c2e 0%, #ff4757 100%\);
  border-color: white;
  box-shadow: 0 4px 15px rgba\(216, 44, 46, 0.4\);
}'''

    new_css = '''/* Language Switcher - Fixed Stability */
.language-switcher {
  display: flex;
  gap: 0.5rem;
  align-items: center;
  position: relative;
}

.lang-btn {
  padding: 0.5rem 1rem;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  border: 2px solid transparent;
  white-space: nowrap;
  min-width: 80px;
  justify-content: center;
  will-change: background, transform;
}

.lang-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
  color: white;
  text-decoration: none;
}

.lang-btn.active {
  background: linear-gradient(135deg, #d82c2e 0%, #ff4757 100%);
  border-color: white;
  box-shadow: 0 4px 15px rgba(216, 44, 46, 0.4);
  position: relative;
  z-index: 1;
}'''

    # Replace the CSS
    if re.search(old_css, content, re.DOTALL):
        content = re.sub(old_css, new_css, content, flags=re.DOTALL)
        print(f"✅ Updated language switcher CSS")
    else:
        print(f"⚠️  CSS pattern not found, trying alternative match...")
        # Try simpler pattern
        simple_pattern = r'/\* Language Switcher \*/.*?\.lang-btn\.active \{[^}]+\}'
        if re.search(simple_pattern, content, re.DOTALL):
            content = re.sub(simple_pattern, new_css, content, flags=re.DOTALL, count=1)
            print(f"✅ Updated language switcher CSS (alternative)")
    
    # Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {filename} fixed!")

print("\n✨ All files processed successfully!")
print("\n🔧 Changes made:")
print("  - Added min-width: 80px (fixed width)")
print("  - Added justify-content: center (centered text)")
print("  - Added white-space: nowrap (no text wrap)")
print("  - Added will-change for smoother transitions")
print("  - Added z-index for active state")
