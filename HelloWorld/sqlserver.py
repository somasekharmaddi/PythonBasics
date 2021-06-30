import pandas as pd
from sqlalchemy import create_engine
# import pyodbc

#mssql+pyodbc://user:password@host:port/databasename?driver=ODBC+Driver+17+for+SQL+Server
#engine = sa.create_engine('mssql+pyodbc://server/database')
server = 'TES-SOMASEKHAR-\SQLEXPRESS'
Database = 'NORTHWND'
Driver = 'ODBC Driver 17 for SQL Server'
database_conn = f'mssql://@{server}/{Database}?driver={Driver}'

engine = create_engine(database_conn)

con = engine.connect()
df = pd.read_sql_query("select top 10 * from Products",con)
print(df)
#rows = con.execut('SELECT TOP 10 * FROM SalesLT.ProductCategory')

#print((row) for row in rows)

