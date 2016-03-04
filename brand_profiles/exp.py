import nltk
import requests, json, pdb
from requests.auth import HTTPBasicAuth
# from nltk.corpus import stopwords, brown, PlaintextCorpusReader
from nltk.collocations import *
from nltk.tag.util import str2tuple
from nltk.tree import Tree
import re, pdb

url = "http://localhost:8000/api/analyse/"
# url = "http://www.gaurangtorvekar.com/api/analyse/"

# Sample movie review
text = "I like the plot of the movie. But I really really don't like the actors in it. There's nothing to like about them. Their acting is really really amateurish."

# Tripadvisor actual review - positive
text = "Just ten minutes drive from where I live. Decided to take a holiday without the hassle of travel. A good 5 Star Hotel. Not at the top of the range for Starwood but very comfortable nevertheless. Enjoyed access to the comfortable Club Lounge. Very nice staff on hand. Good buffet breakfast."

# Tripadvisor actual review - negative
text = "Disappointing hotel, room not cleaned before we arrive - dead gecko and December bill on floor of room. Despite notice in room saying that they are serviced every day ours was not and we had to request for it to be done and get fresh towels"

input_text = {'text':text}

data = {"json":json.dumps(input_text)}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


r = requests.post(url, data)

print r.json()
