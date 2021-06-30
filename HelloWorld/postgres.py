import pandas as pd
import psycopg2
from sqlalchemy import create_engine

#load csv in to data frame
#df = pd.read_csv('D:/Data/For_DC/events_2021060307h.csv')
df = pd.read_csv('D:/Data/For_DC/events_2021060307h.csv',doublequote=True, escapechar='\\')

engine = create_engine('postgresql://postgres:soma1234@localhost/soma_dev')
conn = engine.connect()
#print(df)
# Below code will load into to_sql_test table
df.to_sql('to_sql_test', con=conn, if_exists='replace', index=False)

#region psycopg2
#df.to_sql('pandas_db', engine)
DB_Host = "localhost"
DB_Name = "soma_dev"
DB_User = "postgres"
DB_Pass = "soma1234"

#conn = psycopg2.connect("dbname=soma user=postgres password=soma1234")

conn = psycopg2.connect(dbname = DB_Name,user=DB_User,password=DB_Pass,host=DB_Host)

#d6tstack.utils.pd_to_psql(df, uri_psql, 'table')
cur = conn.cursor()
cur.execute('select version()')
db_version = cur.fetchone()
print(db_version)

#cur.copy_from(df, 'public.events_test_01', sep=',')

conn.close()
#endregion