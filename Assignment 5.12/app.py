from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def suppliers():
    suppliers = database.get_all_suppliers()
    return render_template('index.html', suppliers=suppliers)

@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):
    products = database.get_supplier_products(supplier_id)
    supplier=database.get_supplier(supplier_id)
    return render_template('products.html', products=products,supplierName=supplier)
@app.route("/categories")
def categories():
    categories=database.get_categories()
    return render_template('categories.html',categories=categories)
@app.route("/categories/<int:id>")
def category_products(id):
    categories=database.get_category_products(id)
    return render_template('categoryProducts.html',categories=categories)