import pandas as pd
import matplotlib.pyplot as plt
import os

def lees_data():
    base_path = r'C:\Git\OpdrachtenP4\PythonOntwerp'
    bedrijven = pd.read_csv(os.path.join(base_path, 'bedrijven.csv'))
    branches = pd.read_csv(os.path.join(base_path, 'branches.csv'))
    return bedrijven, branches

def menu():
    print("\nKies een grafiek:")
    print("1. Staafdiagram: aantal bedrijven per branche")
    print("2. Taartdiagram: top 5 bedrijven hoogste omzet")
    print("3. Taartdiagram: top 5 bedrijven hoogste winst uit een stad")
    print("4. Lijngrafiek: winstontwikkeling van een bedrijf")
    print("5. Taartdiagram: top 5 omzet t.o.v. rest")
    print("6. Taartdiagram: top 10 branches hoogste omzet in een jaar")
    print("7. Taartdiagram: top 10 branches hoogste gemiddelde winst over 5 jaar")
    print("0. Stoppen")
    keuze = input("Maak een keuze: ")
    return keuze

def staafdiagram_branche(bedrijven, branches):
    branche_counts = bedrijven['idbranch'].value_counts().reset_index()
    branche_counts.columns = ['idbranch', 'aantal_bedrijven']
    branche_counts = branche_counts.merge(branches, left_on='idbranch', right_on='idbranche')
    plt.figure(figsize=(10,6))
    plt.bar(branche_counts['omschrijving'], branche_counts['aantal_bedrijven'])
    plt.xlabel('Branche')
    plt.ylabel('Aantal bedrijven')
    plt.title('Aantal bedrijven per branche')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('staafdiagram_branche.png')
    plt.show()

def taartdiagram_top5_omzet(bedrijven):
    top5 = bedrijven.sort_values('omzet', ascending=False).head(5)
    plt.figure(figsize=(8,8))
    plt.pie(top5['omzet'], labels=top5['naam'], autopct='%1.1f%%', startangle=140)
    plt.title('Top 5 bedrijven met hoogste omzet')
    plt.savefig('taartdiagram_top5_omzet.png')
    plt.show()

def taartdiagram_top5_winst_stad(bedrijven, stad):
    bedrijven_stad = bedrijven[bedrijven['plaats'].str.lower() == stad.lower()]
    top5 = bedrijven_stad.sort_values('winst', ascending=False).head(5)
    if top5.empty:
        print("Geen bedrijven gevonden in deze stad.")
        return
    plt.figure(figsize=(8,8))
    plt.pie(top5['winst'], labels=top5['naam'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Top 5 bedrijven met hoogste winst uit {stad}')
    plt.savefig(f'taartdiagram_top5_winst_{stad}.png')
    plt.show()

def lijngrafiek_winstontwikkeling(bedrijven, bedrijf):
    bedrijf_data = bedrijven[bedrijven['naam'].str.lower() == bedrijf.lower()]
    if bedrijf_data.empty:
        print("Bedrijf niet gevonden.")
        return
    bedrijf_data = bedrijf_data.sort_values('jaar')
    plt.figure(figsize=(10,6))
    plt.plot(bedrijf_data['jaar'], bedrijf_data['winst'], marker='o')
    plt.xlabel('Jaar')
    plt.ylabel('Winst')
    plt.title(f'Winstontwikkeling van {bedrijf}')
    plt.grid(True)
    plt.savefig(f'lijngrafiek_winst_{bedrijf}.png')
    plt.show()

def taartdiagram_top5_omzet_rest(bedrijven):
    top5 = bedrijven.sort_values('omzet', ascending=False).head(5)
    rest = bedrijven.sort_values('omzet', ascending=False).iloc[5:]
    labels = list(top5['naam']) + ['Rest']
    sizes = list(top5['omzet']) + [rest['omzet'].sum()]
    plt.figure(figsize=(8,8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Top 5 bedrijven omzet t.o.v. rest')
    plt.savefig('taartdiagram_top5_omzet_rest.png')
    plt.show()

def taartdiagram_top10_branches_omzet_jaar(bedrijven, branches, jaar):
    bedrijven_jaar = bedrijven[bedrijven['jaar'] == int(jaar)]
    omzet_per_branche = bedrijven_jaar.groupby('idbranch')['omzet'].sum().reset_index()
    omzet_per_branche = omzet_per_branche.merge(branches, left_on='idbranch', right_on='idbranche')
    top10 = omzet_per_branche.sort_values('omzet', ascending=False).head(10)
    plt.figure(figsize=(8,8))
    plt.pie(top10['omzet'], labels=top10['omschrijving'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Top 10 branches hoogste omzet in {jaar}')
    plt.savefig(f'taartdiagram_top10_branches_omzet_{jaar}.png')
    plt.show()

def taartdiagram_top10_branches_gem_winst(bedrijven, branches):
    laatste_jaar = bedrijven['jaar'].max()
    vijfjaar = bedrijven[bedrijven['jaar'] >= laatste_jaar - 4]
    gem_winst_per_branche = vijfjaar.groupby('idbranch')['winst'].mean().reset_index()
    gem_winst_per_branche = gem_winst_per_branche.merge(branches, left_on='idbranch', right_on='idbranche')
    top10 = gem_winst_per_branche.sort_values('winst', ascending=False).head(10)
    plt.figure(figsize=(8,8))
    plt.pie(top10['winst'], labels=top10['omschrijving'], autopct='%1.1f%%', startangle=140)
    plt.title('Top 10 branches hoogste gemiddelde winst (laatste 5 jaar)')
    plt.savefig('taartdiagram_top10_branches_gem_winst.png')
    plt.show()

def main():
    bedrijven, branches = lees_data()
    while True:
        keuze = menu()
        if keuze == "1":
            staafdiagram_branche(bedrijven, branches)
        elif keuze == "2":
            taartdiagram_top5_omzet(bedrijven)
        elif keuze == "3":
            stad = input("Uit welke stad? ")
            taartdiagram_top5_winst_stad(bedrijven, stad)
        elif keuze == "4":
            print("Beschikbare bedrijven:")
            for naam in bedrijven['naam'].unique():
                print("-", naam)
            bedrijf = input("Van welk bedrijf? ")
            lijngrafiek_winstontwikkeling(bedrijven, bedrijf)
        elif keuze == "5":
            taartdiagram_top5_omzet_rest(bedrijven)
        elif keuze == "6":
            jaar = input("Voor welk jaar? ")
            taartdiagram_top10_branches_omzet_jaar(bedrijven, branches, jaar)
        elif keuze == "7":
            taartdiagram_top10_branches_gem_winst(bedrijven, branches)
        elif keuze == "0":
            print("Programma gestopt.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main()