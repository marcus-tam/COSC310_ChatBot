
import nltk
# you may need to download nltk using:
#nltk.download()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download("stopwords")
nltk.download("sent_tokenize")

def tokeizeQuestion(text):
    stop_words = set(stopwords.words('english'))
    tokenized = sent_tokenize(text)
    for i in tokenized:
        # Word tokenizers is used to find the words
        # and punctuation in a string
        wordsList = nltk.word_tokenize(i)

        # removing stop words from wordList
        wordsList = [w for w in wordsList if not w in stop_words]

        #  Using a Tagger. Which is part-of-speech
        # tagger or POS-tagger.
        tagged = nltk.pos_tag(wordsList)

        return tagged


