from nltk.chat.util import Chat , reflections
pairs = [
    ['my name is (.*)', ['hello %1']]

]
chat = Chat(pairs, reflections)
chat.converse()