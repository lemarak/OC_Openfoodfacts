# Utilisez les données publiques de l'OpenFoodFacts

Programme qui interagit avec la base Open Food Facts pour en récupérer les aliments, les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.

## Installation

* clone the project from [GitHub](https://github.com/lemarak/OC_Projet5)
* install requirements
```
pip install -r requirements.txt
```
* to run the program
```
python main.py
```

## Prerequisites


## Develop with
- mysql
- python
- OpenFoodFact's api


## User guide
- Authentication
You must first identify yourself
```
Login : ___
Password : ___
```

- Main Menu
Choose from the two options :
```
    1 - Quel aliment souhaitez-vous remplacer ?
    2 - Retrouver mes aliments substitués
    Votre choix : _
```

- Quel aliment souhaitez-vous remplacer ?
The program displays the list of categories :
```
    1 - Produits à tartiner
    2 - Biscuits et gâteaux
    3 - Epicerie
    ...
    Saisir votre choix : _1_
```

The program displays sub-categories in this category
```
    1 - Miels
    2 - Crèmes de citron
    3 - Confitures de lait
    4 - Pâtes à tartiner
    ...
    Saisir votre choix : _4_
```

Then choose the food for which you want to know a substitute
```
    1 - Pâte à tartiner - Carrefour Bio - 350 g
    2 - Pâte à tartiner bio - Auchan - 400 g
    3 - Pâte à tartiner bio - Lucien Georgelin - 600 g
    ...
    Saisir votre choix : _3_
```


The program will then display the product details.  
You can register the product if you wish.

```
    ** Pâte à tartiner bio - Lucien Georgelin - 600 g **
    Påte à tartiner noisette cacao issus de l'agriculture biologique.
    Magasins : Biocoop, Naturalia
    Lien OpenFoodFacts : https://fr.openfoodfacts.org/produit/3330720237798/pate-a-tartiner-bio-lucien-georgelin
    
    Enregistrer produit (o/n) : _

```

- Retrouver mes aliments substitués
The program displays the list of foods that you have already saved.
Choose one to view details
```
    1 - Pâte à tartiner bio - Lucien Georgelin - 600 g
    2 - Yaourt à la vanille bio - Malo - 125 g
    3 - Confiture de fraises au sucre de canne Bio
    ...
    Saisir votre choix : _1_
```

