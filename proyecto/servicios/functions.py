import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def loadData():
    """     try:
            conex= sqlite3.connect('./proyecto/main.db')
        except Exception as f:
            print('error en bd',f) """

    files=os.listdir('./proyecto/data')
    for file in files:
        print(file)
        df=pd.read_csv(f"./proyecto/data/{file}")
        namefile=file.split('.')[0]
        with sqlite3.connect('./proyecto/database.db') as conn:
            df.to_sql(f'{namefile}',con=conn, index=False, if_exists='replace')
            print(f'data carga {namefile}')
        return namefile
    
def filter_by_price(price):
     return price>20

def filter_by_price(row):
    return row['price'] > 20

def generateReport():
        with sqlite3.connect('./proyecto/database.db') as conn:
           query='select * from amazon'
           df=pd.read_sql(query,conn)
           # Aplicar filtro
           df_filtered = df[df.apply(filter_by_price, axis=1)]
           # Guardar informe en archivo CSV
           df_filtered.to_csv('./proyecto/reports/amazon-report.csv', index=False)
           # Imprimir las primeras filas del DataFrame
           print(df_filtered.head())


def showData():
      with sqlite3.connect('./proyecto/database.db') as conn:
           query='select * from amazon'
           df = pd.read_sql(query, conn)
           fig, ax = plt.subplots(figsize=(10, 6))
           ax.scatter(df['category'], df['actual_price'], alpha=0.7)
           plt.xlabel('Categoría')
           plt.ylabel('Precio Actual')
           plt.title('Gráfico de Dispersión')
           plt.show()