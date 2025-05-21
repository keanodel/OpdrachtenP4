# Woordenboek Nederlands -> Engels
import pyttsx3

woordenboek = {
    "hallo": "hello",
    "wereld": "world",
    "hoe": "how",
    "gaat": "are",
    "het": "it",
    "met": "with",
    "jou": "you",
    "ik": "I",
    "ben": "am",
    "goed": "good",
    "dankje": "thanks"
}

def vertaal_zin(zin):
    woorden = zin.lower().split()
    vertaalde_woorden = []
    for woord in woorden:
        vertaalde_woorden.append(woordenboek.get(woord, woord))
    return " ".join(vertaalde_woorden)

def spreek_tekst(tekst):
    engine = pyttsx3.init()
    engine.say(tekst)
    engine.runAndWait()

def main():
    print("Welkom bij de Nederlandse -> Engelse vertaler!")
    zin = input("Voer een Nederlandse zin in: ")
    vertaling = vertaal_zin(zin)
    print("Vertaling:", vertaling)
    spreek_tekst(vertaling)

if __name__ == "__main__":
    main()