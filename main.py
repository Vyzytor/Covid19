from flask import Flask
from flask import jsonify
import google.auth
from google.cloud import bigquery
from google.cloud import bigquery_storage



app = Flask(__name__)

#@app.route('/')
#def hello():
#  """Return a friendly HTTP greeting."""
#  val = {"value": "Hello World!*!*!*"}
#  return jsonify(val)

#@app.route('/name/<value>')
#def name(value):
#  val = {"value": value}
#  return jsonify(val)

#@app.route('/')
#def get_days():
#  """Return a friendly HTTP greeting."""
#  num=input('how many days: ')
#  val = {"value": num}
#  return jsonify(val)

@app.route("/")
def homepage():
    return render_template("page.html", title="HOME PAGE")

@app.route("/docs")
def docs():
    return render_template("page.html", title="docs page")

@app.route("/about")
def about():
    return render_template("page.html", title="about page")
  
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)

# add a note 888

