"""Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html

Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php
"""

################ Spelling Corrector 

# For doing the spelling correction, we find a data file that stores a lot sentences ralated to dr.Seuss. The reason
# why we do that is to make the correction more close to dr Seuss' perspective.
# The original python file has been modified.
import re
from collections import Counter


def words(text): return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('drseuss.txt').read()))


def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N


def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)


def candidates(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def checkCorrection(question):
    arr = question.split(" ")
    temp = ""
    for questionWord in arr:
        correctWord = correction(questionWord)
        if not correctWord == questionWord:
            userResponse = input("Does \"" + questionWord + "\" means \"" + correctWord + "\' ?")
            if userResponse.lower().__contains__("yes" or "yea" or "yep"):
                temp += correctWord + " "
            elif userResponse.lower().__contains__("no" or "nope" or "nah"):
                temp += questionWord + " "
            else:
                return userResponse
        else:
            temp += questionWord + " "
    return temp


def checkCorrectionViaSocket(question):
    arr = question.split(" ")
    correctedResponse=""
    for questionWord in arr:
        correctWord = correction(questionWord)
        correctedResponse += correctWord+" "
    return [question+" ",correctedResponse]


while __name__ == '__main__':
    word = input("input:")
    res=checkCorrectionViaSocket(word)
    print(len(res))
    print(res[0])
    if len(res)==2:
        print(res[1])
        print(res[0]==res[1])
