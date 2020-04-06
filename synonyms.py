import nltk
from nltk.corpus import wordnet


def findSynonyms(text):
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(text):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return synonyms, antonyms
