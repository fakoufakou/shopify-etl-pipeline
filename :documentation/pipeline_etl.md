Pipeline ETL Shopify – Documentation technique

#Extraction des données
produits.csv
customers_export.csv
discounts_export.csv
Shopify_Marketing.xlsx
Shopify_Finance.xlsx

#Nettoyage des données
suppression des colonnes inutiles
normalisation des noms de colonnes
nettoyage des valeurs manquantes
conversion des dates
harmonisation des types

#Chargement dans PostgreSQL

| Fichier source         | Table PostgreSQL |
| ---------------------- | ---------------- |
| produits.csv           | produits         |
| customers_export.csv   | clients          |
| discounts_export.csv   | reductions       |
| Shopify_Marketing.xlsx | marketing        |
| Shopify_Finance.xlsx   | finances         |

#Création des vues SQL
vue_produits
vue_clients
vue_reductions
vue_marketing
vue_finances

#Connexion à Power BI
import automatique des vues
relations entre tables
modèles prêts pour dashboards

#Automatisation (fichier principal etl_main.py)
extraction
nettoyage
insertions dans PostgreSQL
création des vues
génération d’un journal d’exécution (log).
Le pipeline complet se lance avec une seule commande Python.








