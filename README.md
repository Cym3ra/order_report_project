# Fördjupning i Pythonprogrammering - Order report 
- **Inlämningsuppgift 1** - Refaktorera ett pythonprogram för orderrapportering

Programmet läser orderdata från en CSV-fil, bearbetar datan och skapar rapporter över bland annat försäljning och returer.
Den originella filen order_report.py har refaktorerats till ett mindre program, så att det får en tydligare struktur, bättre felhantering, testbarhet och mer separata ansvarsområden.


## Vad projektet gör:

1. läser orderdata från `data/orders.csv`.
2. kontrollerar att nödvändiga kolumner finns och att datan inte är tom.
3. beräknar ordervärde och rabatterat värde per order.
4. sammanställer försäljning och returer per produktkategori och
   region, samt en övergripande sammanfattning.
5. sparar resultaten som CSV-filer i `output/`.

## Installation

Kräver Python 3.10 eller senare.

```bash
# skapa och aktivera en virtuell miljö (valfritt men rekommenderas)
python -m venv .venv

 # Windows: 
.venv\Scripts\activate

# installera projektet och dess beroenden (pandas + pytest)
pip install -e ".[dev]"
```

Beroenden: se `pyproject.toml`

## Köra programmet:

```
python -m src.order_report
```

Programmet loggar sin körning (inläsning, validering, vilka rapporter som skapats och var de sparades), och resultatfilerna hamnar i `output`.

## Köra testerna 

```
pytest
```
För att köra varje test-fil individuellt:
```
python -m pytest tests/test_validation.py -v
python -m pytest tests/test_processing.py -v
```

## Projektstruktur

```
order_report/
├── README.md
├── code_review.md          # Granskning av originalkoden
├── reflection.md           # Reflektion kring refaktoreringen
├── pyproject.toml          # Beroenden, pytest-konfig
├── data/
│   └── orders.csv          # Dataset
├── src/
│   └── order_report/
│       ├── __init__.py
│       ├── __main__.py     # Startpunkt: python -m src.order_report
│       ├── config.py       # ReportConfig + logg-konfiguration
│       ├── loading.py      # Läser in CSV-filen
│       ├── validation.py   # Validering av data
│       ├── processing.py   # Städar data och beräknar ordervärden
│       └── reporting.py    # Bygger rapporter och sparar dem
├── tests/
│   ├── test_processing.py  # tester av programmets logik
│   └── test_validation.py  # ^
└── output/                 # Genererade rapporter (skapas vid körning)
```

