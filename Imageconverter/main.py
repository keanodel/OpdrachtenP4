import os
from PIL import Image

def get_directory_path(prompt):
    """Vraag de gebruiker om een geldig pad."""
    while True:
        path = input(prompt)
        if os.path.exists(path):
            return path
        print("Pad bestaat niet. Probeer opnieuw.")

def get_max_size():
    """Vraag de gebruiker om een maximaal formaat (max 2000 pixels)."""
    while True:
        try:
            size = int(input("Geef het maximale formaat (max 2000 pixels): "))
            if 1 <= size <= 2000:
                return size
            print("Formaat moet tussen 1 en 2000 pixels liggen.")
        except ValueError:
            print("Ongeldige invoer. Voer een getal in.")

def resize_images(source_dir, dest_dir, max_size):
    """Pas de grootte van afbeeldingen aan en sla ze op in de uitvoermap."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    files = os.listdir(source_dir)
    image_count = 0
    skipped_files = 0

    print(f"Aantal bestanden gevonden: {len(files)}")

    for file_name in files:
        source_path = os.path.join(source_dir, file_name)
        dest_path = os.path.join(dest_dir, file_name)

        if not os.path.isfile(source_path):
            skipped_files += 1
            continue

        try:
            with Image.open(source_path) as img:
                print(f"Bezig met aanpassen: {file_name}")
                img.thumbnail((max_size, max_size))
                img.save(dest_path)
                image_count += 1
        except (OSError, IOError):
            print(f"Bestand overgeslagen (geen afbeelding): {file_name}")
            skipped_files += 1

    print(f"Aantal aangepaste afbeeldingen: {image_count}")
    print(f"Aantal overgeslagen bestanden: {skipped_files}")

def main():
    print("Welkom bij de Image Converter!")
    source_dir = get_directory_path("Geef het pad naar de map met afbeeldingen: ")
    dest_dir = get_directory_path("Geef het pad naar de uitvoermap: ")
    max_size = get_max_size()

    resize_images(source_dir, dest_dir, max_size)
    print("Afbeeldingen zijn succesvol aangepast en opgeslagen.")

if __name__ == "__main__":
    main()