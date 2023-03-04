import numpy as np
import nltk
import spacy

from gensim.models import Word2Vec
from nltk import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode
import string

from sklearn.feature_extraction.text import TfidfVectorizer

#Preproccessing

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
def lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    return words

def pre_process(corpus):
    # convert input corpus to lower case.
    corpus = corpus.lower()
    # collecting a list of stop words from nltk and punctuation form
    # string class and create single array.
    stopset = stopwords.words('english') + list(string.punctuation)
    # remove stop words and punctuations from string.
    # word_tokenize is used to tokenize the input corpus in word tokens.
    corpus = " ".join([i for i in word_tokenize(corpus) if i not in stopset])
    # remove non-ascii characters
    corpus = unidecode(corpus)
    corpus = lemmatize(corpus)
    return corpus

#Feature Extraction (get your embeddings from gensim model)

import gensim
from gensim.models import Word2Vec, KeyedVectors
from sklearn.decomposition import PCA
import gensim.downloader as api

model = api.load("glove-wiki-gigaword-100")





if __name__ == '__main__':
    #extracted resume text (need to get from spacyExtractor)
    resume = ""
    #company job description text (need to get from list of job descriptions, sample below)
    job = "We are hiring a Data Scientist that will analyze how people use our educational science website and what actions correlate with events like buying a subscription, which plans they choose, etc. In addition to that, analyze renewal statistics by cohort, identify indicators of likely churn, and help our A/B testing team analyze data for best-performing ads and landing pages more quickly. Extremely versatile and can work quickly (startup mentality) Ready to tackle new challenges weekly. Can craft their own questions and turn around easily digestible insights. Can make clear graphs, dashboards, and communicate with non-technical people. Can use tools like Google Analytics and other 3rd party tools."

    #pre process
    resume = pre_process(resume)
    job = pre_process(job)

    print(resume, job)

    #feature extraction and sentence embed averaging
    word_mov = model.wmdistance(resume, job)
    cos_sim = model.n_similarity(resume, job)

    #calc cosine similarity of 2 sentences
    print(cos_sim)

    #calc word movers distance of 2 sentences
    print(word_mov)
    






