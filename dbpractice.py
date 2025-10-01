# Database practice :)
import sqlite3

# connection allows us to connect 
# python to a SQL databse :)
connection = sqlite3.connect("./database.db") # . :relative to current file location
# cursor allows interaction with SQL DB
cursor = connection.cursor() #creates cursor from connection

query = """ 
SELECT AVG(stock_quantity) AS averageQuantity
FROM Products;
""" # multi-line string which is why we use 3 """
result = cursor.execute(query).fetchall()
print(f"OUR SQL RESULT: {result}")


# BOTTOM/END OF OUR CODE
connection.commit() # commits changes
connection.close() # disconnects the connection 