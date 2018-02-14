import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

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

vocabulary = set()
for sentence in sentences_list:
    words = tokenize(sentence)
    vocabulary.update(words)

vocabulary = list(vocabulary)
word_index = {w: idx for idx, w in enumerate(vocabulary)}

VOCABULARY_SIZE = len(vocabulary)
DOCUMENTS_COUNT = len(sentences_list)
TAKE_TOP = 7


word_idf = defaultdict(lambda: 0)
for sentence in sentences_list:
    words = set(tokenize(sentence))
    for word in words:
        word_idf[word] += 1

for word in vocabulary:
    word_idf[word] = math.log(DOCUMENTS_COUNT / float(1 + word_idf[word]))
def word_tf(word, document):
    if isinstance(document, str):
        document = tokenize(document)
    return document.count(word) / len(document)

def tf_idf(word, document):
    if isinstance(document, str):
        document = tokenize(document)

    if not word in document:
        return .0

    return word_tf(word, document) * word_idf[word]

score = np.zeros(DOCUMENTS_COUNT)
for index, sentence in enumerate(sentences_list):
    score[index] = sum([tf_idf(word, sentence) for word in tokenize(sentence)])


indexes = np.argpartition(score, -TAKE_TOP)[-TAKE_TOP:]

summary = np.array(sentences_list)[indexes]

print("\n\n".join(summary))
