import json
import mysql.connector

host = input("hostname: ")
user = input("username: ")
password = input("password: ")
database = input("db name: ")

filepath = input("file path: ")

# Connect to MySQL database
conn = mysql.connector.connect(
    host=host, user=user, password=password, database=database
)
cursor = conn.cursor()

# Read JSON file
with open(filepath, "r") as file:
    data = json.load(file)

# Insert data into MySQL database
for product in data:
    url = product.get("url", "")
    category = product.get("category", "")
    brand = product.get("brand", "")
    name = product.get("name", "")
    price = product.get("price", 0)
    price_currency = product.get("priceCurrency", "")
    images = ",".join(product.get("images", []))
    sku = product.get("sku", "")

    # SQL query to insert data into table
    sql = "INSERT INTO petlebi (URL, category, brand, name, price, priceCurrency, images, SKU) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (url, category, brand, name, price, price_currency, images, sku)
    cursor.execute(sql, val)

# Commit changes and close connection
conn.commit()
print("Data inserted successfully!")
