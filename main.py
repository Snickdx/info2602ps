import json
from flask_cors import CORS
from flask import Flask, request, render_template
from sqlalchemy.exc import IntegrityError

from models import db, Logs

''' Begin boilerplate code '''
def create_app():
  app = Flask(__name__, static_url_path='')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SECRET_KEY'] = "MYSECRET"
  CORS(app)
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()

global pokedata

with open('pokedata.json') as f:
  pokedata = json.load(f)

@app.route('/pokemon')
def get_all_pokemon():
  return json.dumps(pokedata)

@app.route('/pokemon/:name')
def get_pokemon(name):
    for poke in pokedata:
        if poke.name == name :
            return json.dumps(poke)
    return json.dumps({ "error": name+' not found' })


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)