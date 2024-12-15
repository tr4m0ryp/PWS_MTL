
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

bestandspad = r"C:\Users\Surface_AppelMous\Downloads\PWSMTLangenaam.xlsx"
data = pd.read_excel(bestandspad, sheet_name='Blad1')
if not all(col in data.columns for col in ['Geslacht', 'Goed']):
    raise ValueError("De dataset moet de kolommen 'Geslacht' en 'Goed' bevatten.")

scores_mannen = data[data['Geslacht'] == 'man']['Goed']
scores_vrouwen = data[data['Geslacht'] == 'vrouw']['Goed']


#stats functie fucking lucky dat er gwoon een lib voor is, leven zit toch mee
u_statistiek, p_waarde = stats.mannwhitneyu(scores_mannen, scores_vrouwen, alternative='two-sided')

print(f"U-statistiek: {u_statistiek}")
print(f"P-waarde: {p_waarde}")
plt.figure(figsize=(18, 10))

plt.subplot(2, 2, 1)
sns.boxplot(x='Geslacht', y='Goed', data=data)
plt.title('Boxplot van scores per geslacht')
plt.xlabel('Geslacht')
plt.ylabel('Aantal goede antwoorden')

plt.subplot(2, 2, 2)
sns.histplot(scores_mannen, kde=True, color='blue', label='Mannen', bins=10, alpha=0.7)
sns.histplot(scores_vrouwen, kde=True, color='pink', label='Vrouwen', bins=10, alpha=0.7)
plt.title('Verdeling van scores per geslacht')
plt.xlabel('Aantal goede antwoorden')
plt.ylabel('Frequentie')
plt.legend()

gemiddelden = data.groupby('Geslacht')['Goed'].mean().reset_index()
plt.subplot(2, 2, 3)
sns.barplot(x='Geslacht', y='Goed', data=gemiddelden, palette='pastel')
plt.title('Gemiddelde scores per geslacht')
plt.xlabel('Geslacht')
plt.ylabel('Gemiddelde aantal goede antwoorden')

plt.subplot(2, 2, 4)
sns.ecdfplot(scores_mannen, color='blue', label='Mannen')
sns.ecdfplot(scores_vrouwen, color='pink', label='Vrouwen')
plt.title('Cumulatieve distributie van scores')
plt.xlabel('Aantal goede antwoorden')
plt.ylabel('Cumulatieve frequentie')
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('mann_whitney_u_visualisaties.png')
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
