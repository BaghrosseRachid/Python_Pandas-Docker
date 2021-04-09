# -*- coding: utf-8 -*-
"""PandasTest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15JhiLjlF6YoWDeC8YwOuzYbOsflpp1nF
"""

#importation module pandas
import pandas as pd

#Importer le csv dans un DataFrame pandas
#compression de gzip directement et lecture de csv
full_csv = pd.read_csv('https://cadastre.data.gouv.fr/data/etalab-dvf/latest/csv/2020/full.csv.gz', compression='gzip',  header=0, sep=',', quotechar='"')

full_csv.head()

#le type de document
type(full_csv)

#taille de ficheir
full_csv.shape

#ajouter une colonnne contenent vore nom
full_csv.insert(0, 'NOM_CANDIDAT', "BAGHROSSE-Rachid")
#full_csv["NOM_CANDIDAT"]="BAGHROSSE-Rachid"

full_csv['NOM_CANDIDAT']

#Ajouter une colonne portant le nom « adresse_string »
full_csv['code_postal'] = full_csv['code_postal'].astype(str)
pays= 'FRANCE'
full_csv["adresse_string"] = (full_csv['adresse_code_voie'] + ' ' + full_csv['adresse_nom_voie'] + ', ' + full_csv['nom_commune'] + ', ' + full_csv['code_postal'] + ', '+ pays)

print(full_csv.adresse_string)

# la suppression des lignes ayant l'un de ces attributs null
full_csv.dropna(subset=['longitude', 'latitude'])

#trie de resultat par date pour récupérer les plus récents enregistrements
trie=full_csv.sort_values(by='date_mutation')
trie.tail(500)