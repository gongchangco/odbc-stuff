import pyodbc
import pandas as pd

# Check available drivers
for dr in pyodbc.drivers():
  if 'MAS' in dr:
    driver = dr

# Create the query
pvx = f'''
  SELECT "SO_InvoiceHeader"."SalesOrderNo"
  FROM "SO_InvoiceHeader" "SO_InvoiceHeader"
'''

# Create the connection
conn = pyodbc.connect(r'DSN=#########;Driver={' + driver + '}', autocommit=True)

try:
  # Read the data
  df = pd.read_sql(pvx, conn)
  
  print(df)
except pyodbc.Error as e:
  print("Error while connecting to driver: ", e)

# Close connection
conn.close()
  
