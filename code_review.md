# Kodgranskning av order_report.py

## Utgångsläge
Scriptet körs och skapar rapporter över försäljning, returer och en översikt över total försäljning, antal beställningar och antalet returer.

## Granskningsfynd

### Fynd 1 - Koden körs vid import
**Observation** Koden körs direkt när filen körs eller importeras.

**Konsekvens** Det för det svårt att återanvända funktionerna och skriva tester. Importerar man en modul kan hela programmet börja läsa filer och skapa rapporter direkt. 

**Förslag** Skapa en `main()`-funktion som ansvarar för programmets start och använd `if __name__ == "__main__":` som startpunkt.

### Fynd 2 - Programmet använder flera print()

**Observation** `print()` används för att meddela att programmet läser data och att körningen är klar.

**Konsekvens** Det finns ingen nivåindelning mellan information, varningar och fel. 

**Förslag** Använd pythons logging för körinformation.

### Fynd 3 - För bred felhantering

**Observation** Hela programmet ligger inom ett `try:  except`, och gör en `Exception` med meddelandet `Något gick fel`.

**Konsekvens** Alla typer av fel fångas på samma sätt, vilket försvårar vart och varför ett fel uppstått. 

**Förslag** Hantera specifika fel som exempelvis `ValueError` vid valideringsproblem. 

### Fynd 4 - För begränsad validering

**Observation** Programmet kontrollerar endast att de obligatoriska kolumnerna finns, men inte de innehåller orimliga värden.

**Konsekvens** Ett negativt antal eller rabatt större än 100% kan påverka rapporten utan att man får en tydlig varning. 

**Förslag** Skapa en separat valideringsfunktion som kontrollerar kolumner, se till att fel och varningar är tydligt kommunicerade.

### Fynd 5 - duplicerad logik

**Observation** Rapporten för produktkategori och region innehåller liknande kod.

**Konsekvens** Det gör programmet svårare att underhålla. Ändras beräkningen på ett ställe måste den ändras på flera ställen. Det ökar risken för fel.

**Förslag** Skapa en funktion som kan skapa en rapport baserat på den kolumn som ska grupperas.

### Fynd 6 - Hårdkodade sökvägar och filnamn

**Observation** Sökvägarna ligger direkt i programflödet, samt att filnamnen är hårdkodade.

**Konsekvens** Det gör det svårare att använda programmet med andra filer eller mappar. Behöver projektets struktur förändras behöver även koden ändras på flera ställen.

**Förslag** Samla programemts konfiguration på ett tydligt ställe, som exemplevis i `config.py`, även genom en `dataclass` som innehåller in och utdata.

### Fynd 7 - Allt i en enda fil

**Observation** Nästan hela projektet ligger i samma kodblock, som ansvarar för att läsa CSV-filen, validera kolumner, bearbeta data, beräkna värden och skapa rapporter.

**Konsekvens** Det blir svårt att förstå och underhålla programmet. Vill man göra en ändring behöver man leta igenom hela koden. Sne blir det svårt att testa enskilda delar.

**Förslag** Dela upp programmet i funktioner med tydliga ansvarsområden. 

### Fynd 8 - Namnen beskriver objektet dåligt

**Observation** Namn som `result1` och `data` är för allmänna och beskriver inte innehållet tillräckligt.

**Konsekvens** Det gör dataflödet svårt att följa, framförallt om programmet utvecklas och växer.

**Förslag** Använd mer beskrivande namn.

### Fynd 9 - Användning av `os.path` över `patlib`

**Observation** Programmet använder `os.path.join`.

**Konsekvens** Det fungerar men koden kan bli tydligare genom att använda `pathlib.Path`, vilket är användbart när sökvägar hanteras på flera ställen i programmet.

**Förslag** Använd `pathlib.Path` för att göra sökvägarna mer lättlästa.