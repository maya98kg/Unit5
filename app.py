from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def hello_world():
    facts = database.get_all_facts()
    return render_template('index.html', facts=facts)
