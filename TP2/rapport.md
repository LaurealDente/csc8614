# 2026-csc8614-language-models

## Exercice 1 

### Question 1 

```text
Lauret Alexandre
Commande d'installation : mamba env create -f csc8614/TP1/requirements.txt -n csc8614
Version Python/Librairie : Python 3.12.3
torch 2.9.1
transformers 4.57.3
plotly 6.5.1
sklearn 1.8.0
```

### Question 2 & 3

Settings et params sont en forme de dictionnaire. Ils sont composés de 5 clefs.

### Question 5.1

Avec cette ligne de code, nous mélangeons les données du dataframe avec une seed qui permet de rendre ce mélange déterministe.

### Question 5.2 

Label
ham     86.60534
spam    13.39466

Le dataset est grandement déséquilibré, il y a beaucoup moins de modèle concernant les spam.

### Question 8.3

On gèle les paramètres avec cette ligne de code car nous souhaitons finetuner le modèle à notre tâche sans modifier la capacité de généralisation du modèle original. 

### Question 10

On observe la loss qui descend au début, cependant elle se stabilise rapidement. La précision est haute (84%) pour les deux premières époques mais le taux de spam reste à 0% pour les deux premières epochs. Pour la dernière epochs le modèle change totalement de fonctionnement et prédit 100% des spams mais garde une accuracy de 16%. Cela indique que le modèle prédisait seulement les ham puis seulement les spams, il n'a pas réellement apprit. 

ham     86.60534
spam    13.39466

L'accuracy obtenu correspond aux proportions que nous avions trouver. Cela rejoint le fait que le modèle n'a pas réellement apprit.