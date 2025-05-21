import os
from PIL import Image

def get_image_files(folder):
    # Haal alle afbeeldingsbestanden op (jpg, jpeg, png)
    allowed_ext = ('.jpg', '.jpeg', '.png')
    files = [f for f in os.listdir(folder) if f.lower().endswith(allowed_ext)]
    files.sort()
    return [os.path.join(folder, f) for f in files]

def images_to_pdf(image_paths, output_pdf):
    if not image_paths:
        print("Geen afbeeldingen gevonden.")
        return

    # Open de eerste afbeelding
    with Image.open(image_paths[0]) as img:
        # Zorg dat alle afbeeldingen in RGB staan
        img_list = []
        for path in image_paths[1:]:
            with Image.open(path) as im:
                img_list.append(im.convert('RGB'))
        img.convert('RGB').save(output_pdf, save_all=True, append_images=img_list)
    print(f"PDF succesvol opgeslagen als: {output_pdf}")

def main():
    print("Afbeeldingen naar PDF converteren")
    folder = input("Geef het pad naar de map met afbeeldingen: ").strip()
    if not os.path.isdir(folder):
        print("Ongeldige map.")
        return

    image_paths = get_image_files(folder)
    if not image_paths:
        print("Geen afbeeldingen gevonden in de opgegeven map.")
        return

    output_pdf = input("Geef de naam voor het PDF-bestand (bijv. output.pdf): ").strip()
    if not output_pdf.lower().endswith('.pdf'):
        output_pdf += '.pdf'

    images_to_pdf(image_paths, os.path.join(folder, output_pdf))

if __name__ == "__main__":
    main()