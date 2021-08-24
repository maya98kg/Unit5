import sqlite3

def query(query_text, *param):
    conn = sqlite3.connect('Northwind_large.sqlite')
    cur = conn.cursor()
    cur.execute(query_text, param)

    column_names = []
    for column in cur.description:
        column_names.append(column[0])

    rows = cur.fetchall()
    dicts = []

    for row in rows:
        d = dict(zip(column_names, row))
        dicts.append(d)

    conn.close()
    return dicts


def get_all_suppliers():
    return query("""SELECT * FROM supplier""")

def get_supplier_products(supplier_id):
    return query("""
                    SELECT * FROM Product
                    WHERE SupplierId = ?""", supplier_id)
def get_supplier(supplier_id):
    return query("""
                    SELECT CompanyName FROM Supplier 
                    WHERE Id = ?""", supplier_id)
def get_categories():
    return query("""SELECT COUNT(Product.CategoryId) AS Count,Category.CategoryName,Category.Description, Category.Id as Idd FROM Category

INNER JOIN Product
	ON Category.Id=Product.CategoryId
GROUP BY Product.CategoryId""")


def get_category_products(id):
    return query("""SELECT Category.CategoryName, Category.Id AS Id, Product.ProductName
,Supplier.CompanyName, Category.Id as Idd
FROM Category

INNER JOIN Product
ON Category.Id=Product.CategoryId

INNER JOIN Supplier
ON Product.SupplierId=Supplier.Id

WHERE Category.Id=?""",id)