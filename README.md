
# Mann-Whitney U Analysis Tool

## Overzicht

Deze tool voert een **Mann-Whitney U-toets** uit om te bepalen of er een statistisch significant verschil is tussen de prestaties van twee groepen, gegroepeerd op geslacht. De resultaten worden visueel weergegeven met behulp van boxplots, histogrammen, gemiddelde scores en cumulatieve distributiefuncties (CDF). Er wordt ook een samenvattingsrapport gegenereerd.

## Functionaliteiten

1. **Statistische Analyse**:
   - Voert een Mann-Whitney U-toets uit op de scores van mannen en vrouwen.
   - Genereert U-statistiek en p-waarde.

2. **Visualisaties**:
   - Boxplot van scores per geslacht.
   - Histogram van de scoreverdeling per geslacht.
   - Barplot van gemiddelde scores per geslacht.
   - Cumulatieve distributie van scores per geslacht.

3. **Rapportage**:
   - Automatisch gegenereerd rapport met de resultaten van de toets.

## Vereisten

### Software
- Python 3.x

### Bibliotheken
- `pandas`
- `scipy`
- `matplotlib`
- `seaborn`

Installeer de benodigde bibliotheken met:

```bash
pip install pandas scipy matplotlib seaborn
```

### Inputbestand
- Een Excel-bestand (`.xlsx`) met ten minste de volgende kolommen:
  - `Geslacht`: Beschrijft het geslacht van de deelnemer (bijv. "man" of "vrouw").
  - `Goed`: Het aantal goede antwoorden per deelnemer.

## Gebruik

1. **Inputbestand instellen**:
   - Pas de variabele `bestandspad` aan naar het pad van jouw Excel-bestand.

2. **Script uitvoeren**:
   - Start het script via de terminal:
     ```bash
     python Score_Analyse.py
     ```

3. **Uitvoer bekijken**:
   - Grafieken: Worden weergegeven en opgeslagen als `mann_whitney_u_visualisaties.png`.
   - Rapport: Wordt opgeslagen als `mann_whitney_u_rapport.txt`.

## Outputbestand

### Visualisaties
De gegenereerde visualisaties bevatten:
- Boxplots en histogrammen voor de scoreverdelingen.
- Barplot van gemiddelde scores.
- Cumulatieve distributie van scores.

### Rapport
Een tekstbestand met:
- De U-statistiek.
- De p-waarde.
- Een conclusie over significantie.

## Aandachtspunten

- Zorg ervoor dat het Excel-bestand de kolommen `Geslacht` en `Goed` bevat. Het script zal een foutmelding geven als deze ontbreken.
- Controleer dat de waarden in `Geslacht` overeenkomen met "man" en "vrouw".

