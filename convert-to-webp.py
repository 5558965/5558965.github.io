#!/usr/bin/env python3
"""
Script pour convertir automatiquement toutes les balises <img> en <picture> avec WebP + fallback
"""
import re
import os
from pathlib import Path

def convert_img_to_picture(html_content):
    """Convertit les balises img en picture avec WebP + fallback"""
    
    # Pattern pour matcher les balises img avec src dans images/
    pattern = r'<img\s+([^>]*?)src="images/([^"]+\.(jpg|jpeg|png))"([^>]*?)>'
    
    def replace_img(match):
        before_src = match.group(1)
        filename = match.group(2)  # Ex: CLAVER.jpg
        extension = match.group(3)
        after_src = match.group(4)
        
        # Extraire le nom sans extension
        name_without_ext = filename.rsplit('.', 1)[0]
        
        # Créer le chemin WebP
        webp_path = f"images/webp/{name_without_ext}.webp"
        original_path = f"images/{filename}"
        
        # Extraire les autres attributs (alt, class, etc.)
        all_attrs = before_src + after_src
        
        # Créer la balise picture
        picture_tag = f'''<picture>
    <source srcset="{webp_path}" type="image/webp">
    <img {all_attrs.strip()}src="{original_path}">
</picture>'''
        
        return picture_tag
    
    # Remplacer toutes les occurrences
    new_content = re.sub(pattern, replace_img, html_content, flags=re.MULTILINE)
    
    return new_content

def main():
    html_file = Path("c:/Users/abdou/Portfolio/index.html")
    backup_file = Path("c:/Users/abdou/Portfolio/index.html.backup")
    
    # Lire le fichier
    print("📖 Lecture de index.html...")
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sauvegarder une copie
    print("💾 Création d'une sauvegarde (index.html.backup)...")
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Compter les images à convertir
    img_count = len(re.findall(r'<img\s+[^>]*?src="images/[^"]+\.(jpg|jpeg|png)"', content))
    print(f"🖼️  {img_count} images trouvées dans images/...")
    
    # Convertir
    print("🔄 Conversion en cours...")
    new_content = convert_img_to_picture(content)
    
    # Compter les conversions
    picture_count = new_content.count('<picture>')
    
    # Écrire le nouveau fichier
    print("💾 Écriture du fichier mis à jour...")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ Terminé!")
    print(f"   ✓ {picture_count} balises <picture> créées")
    print(f"   ✓ WebP utilisé avec fallback PNG/JPG")
    print(f"   ✓ Sauvegarde créée: index.html.backup")
    print(f"\n🚀 Gain attendu: 81.1% plus léger (5.97 MB → 1.13 MB)")

if __name__ == "__main__":
    main()
