import pandas as pd
import psycopg2
from psycopg2 import sql

# Connexion à PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="shopify",
    user="postgres",
    password="mot_de_passe"
)
cursor = conn.cursor()

print("Connexion postgresql oK.")

# Fonction de nettoyage
def nettoyer_dataframe(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df = df.drop_duplicates()
    df = df.fillna(value={"": None})
    return df

# Chargement dans PostgreSQL

def insert_into_table(df, table_name):
    cols = list(df.columns)
    insert_query = sql.SQL(
        "INSERT INTO {} ({}) VALUES ({})"
    ).format(
        sql.Identifier(table_name),
        sql.SQL(', ').join(map(sql.Identifier, cols)),
        sql.SQL(', ').join(sql.Placeholder() * len(cols))
    )

    for row in df.itertuples(index=False, name=None):
        cursor.execute(insert_query, row)

    conn.commit()
    print(f"➡️ Table '{table_name}' chargée ({len(df)} lignes).")

# ETL pour chaque dataset
datasets = {
    "produits.csv": "produits",
    "clients_export.csv": "clients",
    "discounts_export.csv": "reductions",
    "Shopify_Marketing.xlsx": "marketing",
    "Shopify_Finance.xlsx": "finances"
}

for fichier, table in datasets.items():
    print(f"\n--- Traitement de {fichier} ---")

    if fichier.endswith(".csv"):
        df = pd.read_csv(f"../data_raw/{fichier}")
    else:
        df = pd.read_excel(f"../data_raw/{fichier}")

    df = nettoyer_dataframe(df)
    insert_into_table(df, table)

cursor.close()
conn.close()
print("\n✅ ETL terminé avec succes") 
