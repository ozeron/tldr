import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

from gensim.corpora import Dictionary
from gensim.models import TfidfModel

import numpy as np

from collections import defaultdict
import json
import math

with open('data/input.json') as f:
    data = json.load(f)

def tokenize(text):
    words = [word.lower() for word in word_tokenize(text) if word.isidentifier()]
    return words

sentences_list = sent_tokenize(data['text'])

DOCUMENTS_COUNT = len(sentences_list)
TAKE_TOP = 7

documents = [tokenize(sentence) for sentence in sentences_list]
dictionary = Dictionary(documents)
tfidf_model = TfidfModel(
    [dictionary.doc2bow(d) for d in documents],
    id2word=dictionary
)

score = np.zeros(DOCUMENTS_COUNT)
for index, sentence in enumerate(sentences_list):
    tfidf_values = dict(tfidf_model[dictionary.doc2bow(tokenize(sentence))])
    score[index] = sum(tfidf_values.values())


indexes = np.argpartition(score, -TAKE_TOP)[-TAKE_TOP:]

summary = np.array(sentences_list)[indexes]

print("\n\n".join(summary))
