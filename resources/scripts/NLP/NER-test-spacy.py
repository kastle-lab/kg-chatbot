import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from pprint import pprint
import spacy
from spacy import displacy
#from collections import Counter
import en_core_web_trf
nlp = en_core_web_trf.load()

#doc = nlp("Bill Gates founded Microsoft Corp. together with Paul Allen in 1975.")
#doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices.')
#doc = nlp("Jane Austen wrote Pride and Prejudice.")
#doc = nlp("Mount Everest is the tallest mountain in the world.")

#doc = nlp("Gearbox Software developed Borderlands and released it in 2009. It sold 600,000 units in Europe.")
#doc = nlp("In The Legend of Zelda: Skyward Sword, Ghirahim seeks to revive the Demon King, Demise.")
#doc = nlp("Sonic the Hedgehog is said to be as fast as the speed of sound, approximately 343 meters per second.")
#doc = nlp("Metal Gear Solid takes place in an alternate history in which the Cold War continued into the 1990s, ending at some point near the end of the 20th century.")
#doc = nlp("In The Legend of Zelda: Breath of the Wild, Link meets King Rhoam Bosphoramus Hyrule after awaking from a century of slumber in the Shrine of Resurrection.")
#doc = nlp("Street Fighter 6 is a fighting game developed by Capcom.")
#doc = nlp("Xenoblade Chronicles is a JRPG developed by Monolith Soft and published by Nintendo in 2008.")
doc = nlp("Chrom from Fire Emblem Awakening is voiced by Matt Mercer. He wield the sword Falchion.")

pprint([(X.text, X.label_) for X in doc.ents])

# Tutorial: https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da