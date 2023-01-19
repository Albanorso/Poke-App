from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello_world():
   return "<p>Hello World!</p>"

@app.route('/pokemon')
def Pokemons():
   return {
        "username": "pippo",
        "theme": "pippo temzzzz",
  }





# @app.get('/programming_languages')
# def list_programming_languages():
#    return {"programming_languages":list(in_memory_datastore.values())}
    
# class Pokemons(Resource):
#     # methods go here
#     pass

# api.add_resource(Pokemons, '/Pokemon/files')  # '/Pokemon/files' is our entry point