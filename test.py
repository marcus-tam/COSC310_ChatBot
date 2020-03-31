import nltk
from nltk.corpus import wordnet

def findSynonyms(text):
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets("not"):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return synonyms, antonyms

if True:
    temp=findSynonyms("hello")
    print(temp[0])
    print(temp[1])