import os
import json

def verander_naar_movie_poster(map_pad, uitvoer_bestand, backup_bestand):
    try:
        # Controleer of de map bestaat
        if not os.path.exists(map_pad):
            print(f"De map '{map_pad}' bestaat niet.")
            return

        # Lees de bestandsnamen in de map
        bestanden = os.listdir(map_pad)
        gewijzigde_bestanden = []
        originele_bestanden = {}

        # Sorteer bestanden voor consistente nummering
        bestanden.sort()

        for index, bestand in enumerate(bestanden, start=1):
            # Controleer of het een bestand is (geen map)
            volledig_pad = os.path.join(map_pad, bestand)
            if os.path.isfile(volledig_pad):
                # Maak de nieuwe bestandsnaam aan
                extensie = os.path.splitext(bestand)[1]  # Behoud de originele extensie
                nieuwe_naam = f"movie_poster_{index:02}{extensie}"
                nieuw_pad = os.path.join(map_pad, nieuwe_naam)

                # Sla de originele naam op voor herstel
                originele_bestanden[nieuwe_naam] = bestand

                # Hernoem het bestand
                os.rename(volledig_pad, nieuw_pad)
                gewijzigde_bestanden.append(nieuwe_naam)

        # Schrijf de gewijzigde bestandsnamen naar een uitvoerbestand
        with open(uitvoer_bestand, 'w') as f:
            for naam in gewijzigde_bestanden:
                f.write(naam + '\n')

        # Sla de originele bestandsnamen op in een backupbestand
        with open(backup_bestand, 'w') as f:
            json.dump(originele_bestanden, f)

        print(f"De bestandsnamen zijn aangepast en opgeslagen in '{uitvoer_bestand}'.")
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

def herstel_naar_origineel(map_pad, backup_bestand):
    try:
        # Controleer of het backupbestand bestaat
        if not os.path.exists(backup_bestand):
            print(f"Het backupbestand '{backup_bestand}' bestaat niet.")
            return

        # Lees de originele bestandsnamen uit het backupbestand
        with open(backup_bestand, 'r') as f:
            originele_bestanden = json.load(f)

        for nieuwe_naam, originele_naam in originele_bestanden.items():
            volledig_pad_nieuw = os.path.join(map_pad, nieuwe_naam)
            volledig_pad_origineel = os.path.join(map_pad, originele_naam)

            # Hernoem het bestand terug naar de originele naam
            if os.path.exists(volledig_pad_nieuw):
                os.rename(volledig_pad_nieuw, volledig_pad_origineel)

        print("De bestandsnamen zijn hersteld naar de originele namen.")
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

def main():
    map_pad = "C:\\Git\\OpdrachtenP4\\Bestandsnamen\\movie_posters\\movie_posters"  # Map met afbeeldingen
    uitvoer_bestand = "C:\\Git\\OpdrachtenP4\\Bestandsnamen\\gewijzigde_bestanden.txt"
    backup_bestand = "C:\\Git\\OpdrachtenP4\\Bestandsnamen\\backup_bestanden.json"

    print("Kies een optie:")
    print("1. Verander bestandsnamen naar 'movie_poster_xx'")
    print("2. Herstel bestandsnamen naar origineel")
    keuze = input("Voer je keuze in (1 of 2): ")

    if keuze == "1":
        verander_naar_movie_poster(map_pad, uitvoer_bestand, backup_bestand)
    elif keuze == "2":
        herstel_naar_origineel(map_pad, backup_bestand)
    else:
        print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == "__main__":
    main()