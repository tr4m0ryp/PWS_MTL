Hier nog even een duidelijke uitleg wat de code precies doet. Ik heb deze uitleg ff snel met chatGPT gemaakt, geen zin om het zelf helemaal uit te leggen. 


---

# Uitleg van de Code: Mann-Whitney U-toets en Visualisaties

Deze Python-code voert een **Mann-Whitney U-toets** uit om te analyseren of er een statistisch significant verschil is in de scores tussen mannen en vrouwen. Het genereert ook visualisaties en een samenvattend rapport. Hieronder wordt stap voor stap uitgelegd wat elk deel van de code doet.

---

### 1. Importeren van benodigde bibliotheken
```python
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
```
**Uitleg:** 
- Deze regels laden externe bibliotheken die de benodigde functies bevatten.
  - `pandas`: Voor het lezen en verwerken van de data.
  - `scipy.stats`: Voor het uitvoeren van de Mann-Whitney U-toets.
  - `matplotlib.pyplot` & `seaborn`: Voor het maken van grafieken.

---

### 2. Inladen van de dataset
```python
bestandspad = r"C:\Users\Surface_AppelMous\Downloads\PWSMTLangenaam.xlsx"
data = pd.read_excel(bestandspad, sheet_name='Blad1')
```
**Uitleg:** 
- De data wordt geladen vanuit een Excel-bestand dat zich op een specifiek pad bevindt. 
- De sheetnaam `Blad1` wordt specifiek gekozen om de juiste tab van de Excel te lezen.

---

### 3. Controle op benodigde kolommen
```python
if not all(col in data.columns for col in ['Geslacht', 'Goed']):
    raise ValueError("De dataset moet de kolommen 'Geslacht' en 'Goed' bevatten.")
```
**Uitleg:** 
- Hier controleren we of de dataset de kolommen `Geslacht` (om het geslacht te bepalen) en `Goed` (om scores te analyseren) bevat.
- Als deze kolommen ontbreken, geeft de code een foutmelding.

---

### 4. Filteren van data per geslacht
```python
scores_mannen = data[data['Geslacht'] == 'man']['Goed']
scores_vrouwen = data[data['Geslacht'] == 'vrouw']['Goed']
```
**Uitleg:** 
- De data wordt opgesplitst:
  - `scores_mannen`: Bevat alleen de scores van mannen.
  - `scores_vrouwen`: Bevat alleen de scores van vrouwen.

---

### 5. Uitvoeren van de Mann-Whitney U-toets
```python
u_statistiek, p_waarde = stats.mannwhitneyu(scores_mannen, scores_vrouwen, alternative='two-sided')
```
**Uitleg:** 
- De **Mann-Whitney U-toets** wordt gebruikt om te testen of de verdelingen van scores voor mannen en vrouwen verschillend zijn.
  - `u_statistiek`: De U-waarde, een maat voor het verschil tussen de twee groepen.
  - `p_waarde`: De waarschijnlijkheid dat het verschil op toeval berust. Een waarde kleiner dan 0.05 betekent een significant verschil.

---

### 6. Printen van toetsresultaten
```python
print(f"U-statistiek: {u_statistiek}")
print(f"P-waarde: {p_waarde}")
```
**Uitleg:** 
- De resultaten van de toets worden op het scherm weergegeven.

---

### 7. Maken van visualisaties
**Visualisaties helpen de resultaten begrijpelijker te maken.**

#### (a) Boxplot
```python
plt.subplot(2, 2, 1)
sns.boxplot(x='Geslacht', y='Goed', data=data)
plt.title('Boxplot van scores per geslacht')
plt.xlabel('Geslacht')
plt.ylabel('Aantal goede antwoorden')
```
**Uitleg:** 
- Een boxplot toont de spreiding van scores per geslacht, inclusief uitschieters.

#### (b) Histogram
```python
plt.subplot(2, 2, 2)
sns.histplot(scores_mannen, kde=True, color='blue', label='Mannen', bins=10, alpha=0.7)
sns.histplot(scores_vrouwen, kde=True, color='pink', label='Vrouwen', bins=10, alpha=0.7)
plt.title('Verdeling van scores per geslacht')
plt.xlabel('Aantal goede antwoorden')
plt.ylabel('Frequentie')
plt.legend()
```
**Uitleg:** 
- Histogrammen tonen de verdeling van scores voor mannen en vrouwen. De **KDE-lijn** geeft de vorm van de verdeling weer.

#### (c) Gemiddelde scores
```python
gemiddelden = data.groupby('Geslacht')['Goed'].mean().reset_index()
plt.subplot(2, 2, 3)
sns.barplot(x='Geslacht', y='Goed', data=gemiddelden, palette='pastel')
plt.title('Gemiddelde scores per geslacht')
plt.xlabel('Geslacht')
plt.ylabel('Gemiddelde aantal goede antwoorden')
```
**Uitleg:** 
- Deze staafdiagram toont het gemiddelde aantal goede antwoorden per geslacht.

#### (d) Cumulatieve verdeling
```python
plt.subplot(2, 2, 4)
sns.ecdfplot(scores_mannen, color='blue', label='Mannen')
sns.ecdfplot(scores_vrouwen, color='pink', label='Vrouwen')
plt.title('Cumulatieve distributie van scores')
plt.xlabel('Aantal goede antwoorden')
plt.ylabel('Cumulatieve frequentie')
plt.legend()
```
**Uitleg:** 
- De cumulatieve distributie toont hoe de scores zich opstapelen, wat inzicht geeft in verschillen tussen de twee groepen.

#### (e) Opslaan en tonen van grafieken
```python
plt.tight_layout()
plt.show()
plt.savefig('mann_whitney_u_visualisaties.png')
```
**Uitleg:** 
- Alle grafieken worden netjes weergegeven en opgeslagen als afbeelding.

---

### 8. Genereren van een samenvattingsrapport
```python
def genereer_samenvattingsrapport():
    with open('mann_whitney_u_rapport.txt', 'w') as rapport:
        rapport.write("Resultaten Mann-Whitney U-toets\n")
        rapport.write("================================\n")
        rapport.write(f"U-statistiek: {u_statistiek}\n")
        rapport.write(f"P-waarde: {p_waarde}\n")
        rapport.write("\n")
        if p_waarde < 0.05:
            rapport.write("Conclusie: Er is een statistisch significant verschil tussen de twee groepen.\n")
        else:
            rapport.write("Conclusie: Er is geen statistisch significant verschil tussen de twee groepen.\n")

genereer_samenvattingsrapport()
```
**Uitleg:** 
- Deze functie schrijft de resultaten van de toets naar een tekstbestand.
  - Als de `p-waarde` kleiner is dan 0.05, concludeert het rapport dat er een significant verschil is tussen mannen en vrouwen.
  - Anders is er geen significant verschil.

---

### 9. Uitvoeren van de functie
```python
genereer_samenvattingsrapport()
```
**Uitleg:** 
- De functie wordt uitgevoerd, waardoor het rapport wordt aangemaakt.

---
