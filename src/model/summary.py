import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

from gensim.corpora import Dictionary
from gensim.models import TfidfModel

import numpy as np
import json

TAKE_TOP = 7


def tokenize(text):
    words = [word.lower() for word in word_tokenize(text) if word.isidentifier()]
    return words


def generate_tfidf_scores(documents, dictionary=None, model=None):
    score = np.zeros(len(documents))
    for index, document in enumerate(documents):
        tfidf_values = dict(model[dictionary.doc2bow(document)])
        score[index] = sum(tfidf_values.values())
    return score


def get_top_indexes(scores):
    top = min(len(scores), TAKE_TOP)
    return np.argpartition(scores, -top)[-top:]


def build(text):
    sentences_list = np.array(sent_tokenize(text))
    documents = [tokenize(sentence) for sentence in sentences_list]
    dictionary = Dictionary(documents)
    tfidf_model = TfidfModel(
        [dictionary.doc2bow(d) for d in documents],
        id2word=dictionary
    )
    scores = generate_tfidf_scores(documents,
                                   dictionary=dictionary,
                                   model=tfidf_model)
    indexes = get_top_indexes(scores)
    summary_docs = sentences_list[indexes]

    return "\n\n".join(summary_docs)


if __name__ == '__main__':
    with open('../../data/input.json') as f:
        data = json.load(f)
    summary = build(data['text'])
    print(summary)
