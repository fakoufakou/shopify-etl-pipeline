
#produits
| Colonne    | Type    | Description                   |
| ---------- | ------- | ----------------------------- |
| product_id | INTEGER | Identifiant unique du produit |
| title      | TEXT    | Nom du produit                |
| status     | TEXT    | Actif / brouillon / archivé   |
| stock      | INTEGER | Quantité en stock             |
| category   | TEXT    | Catégorie du produit          |

#clients
| Colonne     | Type    | Description        |
| ----------- | ------- | ------------------ |
| customer_id | INTEGER | Identifiant client |
| first_name  | TEXT    | Prénom             |
| last_name   | TEXT    | Nom                |
| email       | TEXT    | Email du client    |
| country     | TEXT    | Pays du client     |

#reductions
| Colonne     | Type    | Description                 |
| ----------- | ------- | --------------------------- |
| discount_id | INTEGER | Identifiant de la réduction |
| code        | TEXT    | Code promo                  |
| value       | FLOAT   | Valeur de la réduction      |
| type        | TEXT    | Pourcentage / montant       |
| usage_count | INTEGER | Nombre d’utilisations       |

#marketing
| Colonne     | Type    | Description             |
| ----------- | ------- | ----------------------- |
| campaign_id | INTEGER | Identifiant campagne    |
| channel     | TEXT    | Email / Ads / Influence |
| budget      | FLOAT   | Budget investi          |
| impressions | INTEGER | Nombre d’affichages     |
| clicks      | INTEGER | Clics                   |

#finances
| Colonne      | Type    | Description            |
| ------------ | ------- | ---------------------- |
| order_id     | INTEGER | Identifiant commande   |
| total_amount | FLOAT   | Montant total          |
| taxes        | FLOAT   | Taxes appliquées       |
| net_revenue  | FLOAT   | Revenu net             |
| date         | TEXT    | Date de la transaction |
