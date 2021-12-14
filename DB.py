# Libraries
import mysql.connector as mariadb
import json

# Config JSON
with open('config.json', 'r') as file:
    config = json.load(file)

# DataBase connection config
mariadb = mariadb.connect(host=config['DB']['DB_HOST'],
                          port=config['DB']['DB_PORT'],
                          user=config['DB']['DB_USER'],
                          password=config['DB']['DB_PASS'])

# Work cursor
cursor = mariadb.cursor(buffered=True)

# DataBase creation
db_verification = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'inventory'"
db_create = "CREATE DATABASE inventory"
db_drop = "DROP DATABASE inventory"

# Execute query
cursor.execute(db_verification)
resp = cursor.fetchone()

if resp is None:
    cursor.execute(db_create)
    cursor.execute(db_verification)
    resp = cursor.fetchone()
    print("THE DATABASE {} WAS CREATED SUCCESSFULLY".format(resp[0]))
else:
    print("THE DATABASE {} EXISTS".format(resp[0]))
    cursor.execute(db_drop)
    cursor.execute(db_create)

# Creation of tables for the inventory DataBase
db_select = "USE inventory"

# Table brand
db_brand_exists = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'inventory' AND table_name = 'brand'"
db_brand_drop = "DROP TABLE brand"
db_brand = '''CREATE TABLE IF NOT EXISTS brand 
              (Id_brand int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
              Description varchar(100) DEFAULT NULL)'''

# Table supplier
db_supplier_exists = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'inventory' AND table_name = 'supplier'"
db_supplier_drop = "DROP TABLE supplier"
db_supplier = '''CREATE TABLE IF NOT EXISTS supplier
                 (Id_supplier int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                 Description varchar(100) DEFAULT NULL)'''

# Table presentation
db_presentation_exists = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'inventory' AND table_name = 'presentation'"
db_presentation_drop = "DROP TABLE presentation"
db_presentation = '''CREATE TABLE IF NOT EXISTS presentation
                     (Id_presentation int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                     Description varchar(100) DEFAULT NULL)'''

# Table zone
db_zone_exists = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'inventory' AND table_name = 'zone'"
db_zone_drop = "DROP TABLE zone"
db_zone = '''CREATE TABLE IF NOT EXISTS zone 
             (Id_zone int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
             Description varchar(100) DEFAULT NULL)'''

# Table products
db_products_exists = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'inventory' AND table_name = 'products'"
db_products_drop = "DROP TABLE products"
db_products = '''CREATE TABLE IF NOT EXISTS products
                 (Id_product int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                 Id_brand int(11) NULL,
                 Id_presentation int(11) NULL,
                 Id_supplier int(11) NULL,
                 Id_zone int(11) DEFAULT NULL,
                 code int(11) DEFAULT NULL,
                 description_product varchar(1000) DEFAULT NULL,
                 price double NOT NULL,
                 stock int(11) NOT NULL,
                 tax int(11) DEFAULT NULL,
                 weight double DEFAULT NULL)'''

# Execute query
cursor.execute(db_select)
resp = cursor.fetchone()

# Creating tables
if resp is None:

    # Creating table brand
    cursor.execute(db_brand_exists)
    resp = cursor.fetchone()
    if resp is not None:
        print("THE brand table ALREADY EXISTS")
        #cursor.execute(db_brand_drop)
        print("RECREATING brand TABLE")
        cursor.execute(db_brand)
        print("THE TABLE brand WAS CREATED SUCCESSFULLY")
    else:
        cursor.execute(db_brand)
        print("THE TABLE brand WAS CREATED SUCCESSFULLY")

    # Creating table supplier
    cursor.execute(db_supplier_exists)
    resp = cursor.fetchone()
    if resp is not None:
        print("THE supplier table ALREADY EXISTS")
        cursor.execute(db_supplier_drop)
        print("RECREATING supplier TABLE")
        cursor.execute(db_supplier)
        print("THE TABLE supplier WAS CREATED SUCCESSFULLY")
    else:
        cursor.execute(db_supplier)
        print("THE TABLE supplier WAS CREATED SUCCESSFULLY")

    # Creating table presentation
    cursor.execute(db_presentation_exists)
    resp = cursor.fetchone()
    if resp is not None:
        print("THE presentation table ALREADY EXISTS")
        cursor.execute(db_presentation_drop)
        print("RECREATING presentation TABLE")
        cursor.execute(db_presentation)
        print("THE TABLE presentation WAS CREATED SUCCESSFULLY")
    else:
        cursor.execute(db_presentation)
        print("THE TABLE presentation WAS CREATED SUCCESSFULLY")

    # Creating table zone
    cursor.execute(db_zone_exists)
    resp = cursor.fetchone()
    if resp is not None:
        print("THE zone table ALREADY EXISTS")
        cursor.execute(db_zone_drop)
        print("RECREATING zone TABLE")
        cursor.execute(db_zone)
        print("THE TABLE zone WAS CREATED SUCCESSFULLY")
    else:
        cursor.execute(db_zone)
        print("THE TABLE zone WAS CREATED SUCCESSFULLY")

    # Creating table products
    cursor.execute(db_products_exists)
    resp = cursor.fetchone()
    if resp is not None:
        print("THE products table ALREADY EXISTS")
        cursor.execute(db_products_drop)
        print("RECREATING products TABLE")
        cursor.execute(db_products)
        print("THE TABLE products WAS CREATED SUCCESSFULLY")
    else:
        cursor.execute(db_products)
        print("THE TABLE products WAS CREATED SUCCESSFULLY")
else:
    print("THE DATABASE NOT EXISTS")

# Foreign Keys
print("CREATING FOREIGN KEY brand")
db_products_fk = '''ALTER TABLE products
	                 ADD CONSTRAINT FK_brand FOREIGN KEY (Id_brand)
	                 REFERENCES brand (Id_brand) ON UPDATE CASCADE ON DELETE CASCADE'''
cursor.execute(db_products_fk)
print("FOREIGN KEY presentation SUCCESSFULLY CREATED")
print("CREATING FOREIGN KEY supplier")
db_products_fk2 = '''ALTER TABLE products
	                 ADD CONSTRAINT FK_supplier FOREIGN KEY (Id_supplier) 
	                 REFERENCES supplier (Id_supplier) ON UPDATE CASCADE ON DELETE CASCADE'''
cursor.execute(db_products_fk2)
print("FOREIGN KEY supplier SUCCESSFULLY CREATED")
print("CREATING FOREIGN KEY zone")
db_products_fk3 = '''ALTER TABLE products
                     ADD CONSTRAINT FK_zone FOREIGN KEY (Id_zone) 
                     REFERENCES zone (Id_zone) ON UPDATE CASCADE ON DELETE CASCADE'''
cursor.execute(db_products_fk3)
print("FOREIGN KEY zone SUCCESSFULLY CREATED")

# Insert data in tables
print("INSERTING DATA INTO THE TABLE brand")
db_brand_insert = "INSERT INTO brand (Description) VALUES ('LA GAITA'), ('OLIOSOYA'), ('NATURA'), ('SOY SABOR'), ('NESTLE'), ('FRITO LAY')"
cursor.execute(db_brand_insert)
mariadb.commit()
print("SUCCESSFUL")

print("INSERTING DATA INTO THE TABLE presentation")
db_presentation_insert = '''INSERT INTO presentation (Description) VALUES
                            ('KILO'),
                            ('LIBRA'),
                            ('CAJA'),
                            ('BOLSA')'''
cursor.execute(db_presentation_insert)
mariadb.commit()
print("SUCCESSFUL")

print("INSERTING DATA INTO THE TABLE supplier")
db_supplier_insert = '''INSERT INTO supplier (Description) VALUES
                        ('DULCES DE LA SABANA'),
                        ('LOS ARRALLANES'),
                        ('EL DORADO'),
                        ('RENGIFO Y ASOCIADOS');'''
cursor.execute(db_supplier_insert)
mariadb.commit()
print("SUCCESSFUL")

print("INSERTING DATA INTO THE TABLE zone")
db_zone_insert = '''INSERT INTO zone (Description) VALUES
                    ('BODEGA 1'),
                    ('VITRINA 1'),
                    ('MOSTRADOR'),
                    ('BODEGA 2');'''
cursor.execute(db_zone_insert)
mariadb.commit()
print("SUCCESSFUL")

print("INSERTING DATA INTO THE TABLE products")
db_products_insert = '''INSERT INTO products (Id_product, Id_brand, Id_presentation,
                        Id_supplier, Id_zone, code, description_product, price,
                        stock, tax, weight) VALUES
                        ('1', '1', '1', '1', '1', '1210', 'En buen estado', '10000', '100', '16', '12.3');'''
cursor.execute(db_products_insert)
mariadb.commit()
print("SUCCESSFUL")

# Data of tables
print("TABLE DATA products")
cursor.execute("SELECT * FROM products")
resp = cursor.fetchall()
data1 = []
data1 = resp
print(data1)

print("TABLE DATA brand")
cursor.execute("SELECT * FROM brand")
data2 = []
resp = cursor.fetchall()
data2 = resp
print(data2)

print("TABLE DATA supplier")
cursor.execute("SELECT * FROM supplier")
resp = cursor.fetchall()
data3 = []
data3 = resp
print(data3)

print("TABLE DATA presentation")
cursor.execute("SELECT * FROM presentation")
data4 = []
resp = cursor.fetchall()
data4 = resp
print(data4)

print("TABLE DATA zone")
cursor.execute("SELECT * FROM zone")
resp = cursor.fetchall()
data5 = []
data5 = resp
print(data5)
