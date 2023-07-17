import os
import shutil

#############################################################################
# 🇩🇪 Hier kannst du Dateiendungen anpassen
# 🇺🇸 Customize file extensions here
picture_extensions = ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".ico"
video_extensions = ".mp4", ".mkv", ".avi", ".mov", ".wmv"
audio_extensions = ".mp3", ".wav", ".wma", ".aac", ".ogg", ".m4a"
document_extensions = ".doc", ".docx", ".pdf", ".xlsx", ".pptx", ".txt"
archive_extensions = ".zip", ".tar", ".tar.gz", ".gz", ".rar"

# Bezeichnungen der erstellten Ordner
# Names of the created folders
pictures = "Bilder"
videos = "Videos"
audios = "Audios"
documents = "Dokumente"
archives = "Archive"
folders = "Ordner"
other = "Andere"
#############################################################################

# 🇩🇪 Definiere den aktuellen Ordner, in dem sich das Skript befindet
# 🇺🇸 Define the current folder where the script is located
current_path = os.path.dirname(os.path.abspath(__file__))

# 🇩🇪 Erstelle eine Liste aller Dateien und Ordner im aktuellen Ordner
# 🇺🇸 Create a list of all files and folders in the current folder
current_path_contents = os.listdir(current_path)

# 🇩🇪 Erstelle die Ordner für die verschiedenen Kategorien, falls mindestens eine entsprechende Datei gefunden wurde
# 🇺🇸 Create folders for different categories if at least one corresponding file is found
picture_folder = os.path.join(current_path, pictures)
if any(item.lower().endswith(picture_extensions) for item in current_path_contents):
    if not os.path.exists(picture_folder):
        os.mkdir(picture_folder)

video_folder = os.path.join(current_path, videos)
if any(item.lower().endswith(video_extensions) for item in current_path_contents):
    if not os.path.exists(video_folder):
        os.mkdir(video_folder)

audio_folder = os.path.join(current_path, audios)
if any(item.lower().endswith(audio_extensions) for item in current_path_contents):
    if not os.path.exists(video_folder):
        os.mkdir(audio_folder)        

document_folder = os.path.join(current_path, documents)
if any(item.lower().endswith(document_extensions) for item in current_path_contents):
    if not os.path.exists(document_folder):
        os.mkdir(document_folder)

archive_folder = os.path.join(current_path, archives)
if any(item.lower().endswith(archive_extensions) for item in current_path_contents):
    if not os.path.exists(archive_folder):
        os.mkdir(archive_folder)

folders_folder = os.path.join(current_path, folders)
if any(os.path.isdir(os.path.join(current_path, item)) for item in current_path_contents) and folders not in current_path_contents:
    if not os.path.exists(folders_folder):
        os.mkdir(folders_folder)

other_folder = os.path.join(current_path, other)
if any(not os.path.isdir(os.path.join(current_path, item)) and not os.path.islink(os.path.join(current_path, item)) and not item.lower().endswith(".lnk") for item in current_path_contents):
    if not os.path.exists(other_folder):
        os.mkdir(other_folder)

# 🇩🇪 Gehe durch alle Dateien und Ordner im aktuellen Pfad
# 🇺🇸 Iterate through all files and folders in current path
for item in current_path_contents:

    item_path = os.path.join(current_path, item)

    # 🇩🇪 Überspringe das Skript selbst
    # 🇺🇸 Skip the script itself
    if item == os.path.basename(__file__):
        continue
    
    # 🇩🇪 Überspringe Verknüpfungen
    # 🇺🇸 Skip symbolic links
    if os.path.islink(item_path):
        continue

    # 🇩🇪 Überspringe Ordner, die gerade erstellt wurden
    # 🇺🇸 Skip folders that were just created
    if os.path.isdir(item_path) and item in [pictures, videos, audios, documents, archives, folders, other]:
        continue
    
    # 🇩🇪 Sortiere die Dateien nach Kategorie und verschiebe sie 
    # 🇺🇸 Sort files into categories and move them
    if item.lower().endswith((picture_extensions)):
        shutil.move(item_path, os.path.join(picture_folder, item))
        
    elif item.lower().endswith((video_extensions)):
        shutil.move(item_path, os.path.join(video_folder, item))

    elif item.lower().endswith((audio_extensions)):
        shutil.move(item_path, os.path.join(audio_folder, item))
        
    elif item.lower().endswith((document_extensions)):
        shutil.move(item_path, os.path.join(document_folder, item))
        
    elif item.lower().endswith((archive_extensions)):
        shutil.move(item_path, os.path.join(archive_folder, item))
        
    elif os.path.isdir(item_path):
        shutil.move(item_path, os.path.join(folders_folder, item))
        
    else:
        shutil.move(item_path, os.path.join(other_folder, item))
        
print("Sortierung abgeschlossen!")
print("Sorting completed!")