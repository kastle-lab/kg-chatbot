import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import en_core_web_trf
nlp = en_core_web_trf.load()

import requests

def format_encoded(input):
    return input.replace('%', '%25').replace(' ', '%20').replace('¡', '%C2%A1').replace("'", '%27').replace('/', '%2F')\
                    .replace('[', '%5B').replace(']', '%5D').replace('+', '%2B').replace(':', '%3A').replace('-', '%2D')\
                    .replace(',', '%2C').replace('&', '%26').replace('!', '%21').replace('.', '%2E').replace('*', '%2A')\
                    .replace('?', '%3F').replace('~', '%7E').replace('@', '%40').replace('#', '%23').replace('°', '%C2%B0')\
                    .replace(';', '%3B').replace('×', '%C3%97').replace('$', '%24').replace('♪', '%E2%99%AA')

def format_decoded(input):
    return input.replace('%25', '%').replace('%20', ' ').replace('%C2%A1', '¡').replace('%27', "'").replace('%2F', '/')\
                    .replace('%5B', '[').replace('%5D', ']').replace('%2B', '+').replace('%3A', ':').replace('%2D', '-')\
                    .replace('%2C', ',').replace('%26', '&').replace('%21', '!').replace('%2E', '.').replace('%2A', '*')\
                    .replace('%3F', '?').replace('%7E', '~').replace('%40', '@').replace('%23', '#').replace('%C2%B0', '°')\
                    .replace('%3B', ';').replace('%C3%97', '×').replace('%24', '$').replace('%E2%99%AA', '♪')

question = input("Bot: Hi, I am a knowledge graph-powered chatbot focusing on information about video games. What would you like to know?\nYou: ")

while True:
    doc = nlp(question)
    entities = [(X.text, X.label_) for X in doc.ents]

    for entity in entities:
        if entity[1] == "WORK_OF_ART" or entity[1] == "PRODUCT":
            formatted_game_name = format_encoded(entity[0])
            
            response = requests.post('http://localhost:3030/vg-dataset/sparql', data={'query': f'SELECT * WHERE {{ ?s ?p ?o . FILTER(?s = <http://example.com/videogames/resource/videoGame.{formatted_game_name}>) }}'})
            data = response.json()

            if 'results' in data and 'bindings' in data['results']:
                bindings = data['results']['bindings']
                for binding in bindings:
                    s = binding['s']['value'].split(".")
                    p = binding['p']['value'].split("/")
                    o = binding['o']['value'].split(".")
                    print(f'{format_decoded(s[-1])}\t{p[-1]}\t{format_decoded(o[-1])}')

    question = input("You: ")
