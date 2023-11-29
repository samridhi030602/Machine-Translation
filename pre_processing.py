import string
string.punctuation
def remove_punctuation(text):
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree

import re
def tokenization(text):
    tokens = text.split()
    return tokens


import nltk
stopwords = nltk.corpus.stopwords.words('english')
def remove_stopwords(text):
    output= [i for i in text if i not in stopwords]
    return output

from nltk.stem.porter import PorterStemmer
#defining the object for stemming
porter_stemmer = PorterStemmer()
#defining a function for stemming
def stemming(text):
    stem_text = [porter_stemmer.stem(word) for word in text]
    return stem_text

from nltk.stem import WordNetLemmatizer
#defining the object for Lemmatization
wordnet_lemmatizer = WordNetLemmatizer()
#defining the function for lemmatization
def lemmatizer(text):
    lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    return lemm_text



def pre_processing(text):
    x=remove_punctuation(text)
    data = x.lower()
    token = tokenization(data)
    StopWordRemoved = remove_stopwords(token)
    stemmed=stemming(StopWordRemoved)
    lemmedtext=lemmatizer(stemmed)

    return lemmedtext