import os
import shutil

# Definiere den aktuellen Ordner, in dem sich das Skript befindet, als Downloads-Ordner
current_folder = os.path.dirname(os.path.abspath(__file__))

# Erstelle eine Liste aller Dateien und Ordner im Downloads-Ordner
folder_contents = os.listdir(current_folder)

# Dateiendungen
picture_extensions = ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".ico"
video_extensions = ".mp4", ".mkv", ".avi", ".mov", ".wmv"
document_extensions = ".doc", ".docx", ".pdf", ".xlsx", ".pptx", ".txt"
arhcive_extensions = ".zip", ".tar", ".tar.gz", ".gz", ".rar"

# Erstelle die Ordner für die verschiedenen Kategorien, falls mindestens eine entsprechende Datei gefunden wurde
picture_folder = os.path.join(current_folder, "Bilder")
if any(item.lower().endswith(picture_extensions) for item in folder_contents):
    if not os.path.exists(picture_folder):
        os.mkdir(picture_folder)

video_folder = os.path.join(current_folder, "Videos")
if any(item.lower().endswith(video_extensions) for item in folder_contents):
    if not os.path.exists(video_folder):
        os.mkdir(video_folder)

document_folder = os.path.join(current_folder, "Dokumente")
if any(item.lower().endswith(document_extensions) for item in folder_contents):
    if not os.path.exists(document_folder):
        os.mkdir(document_folder)

archive_folder = os.path.join(current_folder, "Archive")
if any(item.lower().endswith(arhcive_extensions) for item in folder_contents):
    if not os.path.exists(archive_folder):
        os.mkdir(archive_folder)

folders_folder = os.path.join(current_folder, "Ordner")
if any(os.path.isdir(os.path.join(current_folder, item)) for item in folder_contents) and "Ordner" not in folder_contents:
    if not os.path.exists(folders_folder):
        os.mkdir(folders_folder)

other_folder = os.path.join(current_folder, "Andere")
if any(not os.path.isdir(os.path.join(current_folder, item)) and not os.path.islink(os.path.join(current_folder, item)) and not item.lower().endswith(".lnk") for item in folder_contents):
    if not os.path.exists(other_folder):
        os.mkdir(other_folder)

# Gehe durch alle Dateien und Ordner im Downloads-Ordner
for item in folder_contents:

    item_path = os.path.join(current_folder, item)

    # Überspringe das Skript selbst
    if item == os.path.basename(__file__):
        continue
    
    # Überspringe Verknüpfungen
    if os.path.islink(item_path):
        continue

    # Überspringe Ordner, die gerade erstellt wurden
    if os.path.isdir(item_path) and item in ["Bilder", "Videos", "Dokumente", "Archive", "Ordner", "Andere"]:
        continue
    
    # Sortiere die Dateien nach Kategorie
    if item.lower().endswith((picture_extensions)):
        shutil.move(item_path, os.path.join(picture_folder, item))
        
    elif item.lower().endswith((video_extensions)):
        shutil.move(item_path, os.path.join(video_folder, item))
        
    elif item.lower().endswith((document_extensions)):
        shutil.move(item_path, os.path.join(document_folder, item))
        
    elif item.lower().endswith((arhcive_extensions)):
        shutil.move(item_path, os.path.join(archive_folder, item))
        
    elif os.path.isdir(item_path):
        shutil.move(item_path, os.path.join(folders_folder, item))
        
    else:
        shutil.move(item_path, os.path.join(other_folder, item))
        
print("Sortierung abgeschlossen!")