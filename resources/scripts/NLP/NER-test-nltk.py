# import pandas as pd
# import numpy as np

# import pickle as pk

# import warnings
# warnings.filterwarnings("ignore")


# from bs4 import BeautifulSoup
# import unicodedata
# import re

import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from nltk.tokenize import word_tokenize
# from nltk.tokenize import sent_tokenize

# from nltk.corpus import stopwords


# from nltk.corpus import wordnet
from nltk import pos_tag
from nltk import ne_chunk

# from nltk.stem.porter import PorterStemmer
# from nltk.stem.wordnet import WordNetLemmatizer

# from nltk.probability import FreqDist
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud

#pos_ner_text = "Bill Gates founded Microsoft Corp. together with Paul Allen in 1975."
#pos_ner_text = "European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices."
#pos_ner_text = "Jane Austen wrote Pride and Prejudice."
pos_ner_text = "Mount Everest is the tallest mountain in the world."

#pos_ner_text = "Gearbox Software developed Borderlands and released it in 2009. It sold 600,000 units in Europe."
#pos_ner_text = "In The Legend of Zelda: Skyward Sword, Ghirahim seeks to revive the Demon King Demise."
#pos_ner_text = "Sonic the Hedgehog is said to be as fast as the speed of sound, approximately 343 meters per second."
#pos_ner_text = "Metal Gear Solid takes place in an alternate history in which the Cold War continued into the 1990s, ending at some point near the end of the 20th century."
#pos_ner_text = "In The Legend of Zelda: Breath of the Wild, Link meets King Rhoam Bosphoramus Hyrule after awaking from a century of slumber in the Shrine of Resurrection."

#POS_tag = pos_tag(word_tokenize(pos_ner_text))
NER_tree = ne_chunk(pos_tag(word_tokenize(pos_ner_text)))
print(NER_tree)

# Tutorials: https://michael-fuchs-python.netlify.app/2021/05/31/nlp-text-pre-processing-iii-pos-ner-and-normalization/#lemmatization
# and https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da
# POS types: https://stackoverflow.com/questions/29332851/what-does-nn-vbd-in-dt-nns-rb-means-in-nltk#:~:text=NNP%3A%20Proper%20noun%2C%20singular%20Phrase,PRP%3A%20Personal%20pronoun%20Phrase
# NER types: https://pythonprogramming.net/named-entity-recognition-nltk-tutorial/