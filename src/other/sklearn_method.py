import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np

from collections import defaultdict
import json
import math

stop_words = stopwords.words('english')

with open('data/input.json') as f:
    data = json.load(f)

def tokenize(text):
    words = [word.lower() for word in word_tokenize(text) if word.isidentifier()]
    return words

sentences_list = sent_tokenize(data['text'])
vocabulary = set()
for sentence in sentences_list:
    words = tokenize(sentence)
    vocabulary.update(words)

vocabulary = list(vocabulary)

DOCUMENTS_COUNT = len(sentences_list)
TAKE_TOP = 7



tfidf = TfidfVectorizer(stop_words=stop_words, tokenizer=tokenize, vocabulary=vocabulary)

# Fit the TfIdf model
tfidf.fit(sentences_list)


score = tfidf.transform(sentences_list).sum(axis=1).ravel()

indexes = np.argpartition(score, -TAKE_TOP, axis=1)[0, -TAKE_TOP:]

summary = np.array(sentences_list)[indexes][0, :]

print("\n\n".join(summary))
