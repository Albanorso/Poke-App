from flask import Flask
import requests
import json
response_API = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')

data = response_API.text
parse_json = json.loads(data)
active_case = parse_json

# response = requests.post(parse_json, data = {'key':'value'})

app = Flask(__name__)
@app.route('/')
def hello_world():
   return "<p>Hello World!</p>"

@app.route('/pokemon')
def Pokemons():
   return parse_json
