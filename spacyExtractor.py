#spacy
import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English
from spacy.tokens import Doc

#gensim
import gensim
from gensim import corpora


#Data loading/ Data manipulation
from PyPDF2 import PdfReader
import numpy as np
import jsonlines

#nltk
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download(['stopwords','wordnet'])

#warning
import warnings 
warnings.filterwarnings('ignore')
reader = PdfReader('Resume.pdf')
data = reader.pages[0].extract_text()
nlp = spacy.load('en_core_web_lg')
skill_pattern_path = "jz_skill_patterns.jsonl"


ruler = nlp.add_pipe("entity_ruler")
ruler.from_disk(skill_pattern_path)

def get_skills(text):
    doc = nlp(text)
    myset = []
    subset = []
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            subset.append(ent.text)
    myset.append(subset)
    return subset


def unique_skills(x):
    return list(set(x))

from nltk.tokenize import word_tokenize
tokens = word_tokenize(data)
words = [token for token in tokens if token.isalpha()]
words = [word.lower() for word in words]
stop = set(stopwords.words('english'))
words = [word for word in words if not word in stop]
str = " ".join(words)

skills = get_skills(str)

print(skills) # now compare with job descriptions with the resumeParser.py