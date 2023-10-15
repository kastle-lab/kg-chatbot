##### Graph stuff
import os
import rdflib
from rdflib import URIRef, Graph, Namespace, Literal
from rdflib import OWL, RDF, RDFS, XSD, TIME
# Prefixes
name_space = "http://example.com/videogames/"
pfs = {
"vg-ont": Namespace(f"{name_space}ontology/"),
"vg": Namespace(f"{name_space}resource/"),
"rdf": RDF,
"xsd": XSD
}
# Initialization shortcut
def init_kg(prefixes=pfs):
    kg = Graph()
    for prefix in pfs:
        kg.bind(prefix, pfs[prefix])
    return kg
# rdf:type shortcut
a = pfs["rdf"]["type"]

# Initialize an empty graph
graph = init_kg()

# Initialize from files

# dir = "output_Video_Games_Sales_as_at_22_Dec_2016"
dir = "output_voice_actors"

for filename in os.listdir(dir):
    with open(os.path.join(dir, filename), "r") as f:
        graph.parse(f)

# output_file = "Video_Games_Sales_as_at_22_Dec_2016.ttl"
output_file = "voice_actors.ttl"

temp = graph.serialize(format="turtle", encoding="utf-8", destination=output_file)