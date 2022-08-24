import pandas as pd
import numpy as np
import psycopg2

#conexion BBDD -emt
conexion=psycopg2.connect(user='postgres',
                          password='934m$b&QnCrk',
                          host='db-v2-360fi-instance-1-cluster.cdv9yi5xuzxq.eu-west-3.rds.amazonaws.com',
                          port='5432',
                          database='emt_dev')

cursor=conexion.cursor()

### select test
"""
#sql="Select * from public.clients_emt;"
cursor.execute("Select * from public.clients_emt where client = 'test1';")
# mostrar resultado
registro=cursor.fetchall()

for cliente in registro:
    print(cliente)
"""

# indicate client
client = 'test1'
# get the select from the table CLIENTS_EMP
cursor.execute(f"""select *
               from public.clients_emt
               where client = '{client}'""")

columns1 = [col[0] for col in cursor.description]
rows1 = cursor.fetchall()
value_list1 = [dict(zip(columns1, row1)) for row1 in rows1]

# output
"""
[{'client': 'test1',
  'ofem000020': True,
  'ofem000030': False,
  'ofst020000': None,
  ....
  ....
  }]
"""

# values_list1 is a list and we need a dict, then...
tmp = []
tmp_values = value_list1[0]
for i in tmp_values.keys():
    if tmp_values[i] ==True:
        tmp.append(i)
        
# show the data add to a new list
print(tmp)

client_ofst=','.join(tmp)
print(client_ofst)
print(type(client_ofst))

#----------------------------

#cursor=conexion.cursor()
## indicate client
#ofst = 'ofem000700'
## get the select from the table CLIENTS_EMP
#cursor.execute(f"""select {ofst}
#               from public.emt """)
#registro=cursor.fetchall()
#
#for cliente in registro:
#    print(cliente)