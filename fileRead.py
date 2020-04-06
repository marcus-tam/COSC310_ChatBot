from numpy import random
from time import sleep
import synonyms as sy
import postagging as pos


def check(question):
    try:
        tagged=pos.tokeizeQuestion(question)
        # print(tagged)
    except:
        tagged=""
        print("POS tagging is not working, please use nltk.download() to get essential packets")
    arr = question.split(" ")
    maxNum = 0
    num = 0
    f = open("response.txt", "r")
    finalResponse = ""
    # default response
    optionalResponse = ["Sorry I don't understand.", "The question is out of my range.", "It is far beyond the topic.",
                        "I am not sure about the answer.", "Make you ask me another question?"]
    for line in f:
        # Coordinate the question word array
        if line.__contains__("Question"):
            questionArray = f.readline().split(" ")
            for word in arr:
                result = sy.findSynonyms(word)
                for questionWord in questionArray:
                    # this .__contain__ will change to "==" when the response.txt is done
                    # weight system: each word has a weight(0-9) to calculate the similarity of the input sentence\
                    # handle the last word for each questionArray, which is "something/n"
                    if questionWord == "" or questionWord == "\n":
                        continue
                    try:
                        if questionWord[len(questionWord) - 1] == "\n":
                            keyword = questionWord[:(len(questionWord) - 2)].lower()
                            keywordValue = int(questionWord[len(questionWord) - 2])
                        else:
                            keyword = questionWord[:(len(questionWord) - 1)].lower()
                            keywordValue = int(questionWord[len(questionWord) - 1])
                    except:
                        print("The word \"" + questionWord + "\" cannot read the value")
                    # make the noun has more weight and the common words has less weight give a little more weight for
                    # IN and JJ
                    if not tagged=="":
                        for tagges in tagged:
                            if keyword==tagges[0]:
                                if tagges[1]=="NN" or tagges=="NNS":
                                    keywordValue=keywordValue*2
                                elif tagges[1]=="IN" or tagges[1]=="JJ":
                                    keywordValue = keywordValue * 1.2
                            else:
                                keywordValue = keywordValue * 0.5
                    if keyword == word.lower():
                        num += keywordValue
                    else:
                        synonyms = result[0]
                        antonyms = result[1]
                        for synonymsWord in synonyms:
                            if synonymsWord == keyword.lower():
                                # handle the last word for each questionArray, which is "something/n"
                                try:
                                    if questionWord[len(questionWord) - 1] == "\n":
                                        num += keywordValue
                                    else:
                                        num += keywordValue
                                # to handle if a word do not have a number in the end of the word
                                except:
                                    num += 1
                        for antonymsWord in antonyms:
                            if antonymsWord == keyword.lower():
                                # handle the last word for each questionArray, which is "something/n"
                                try:
                                    if questionWord[len(questionWord) - 1] == "\n":
                                        num -= keywordValue
                                    else:
                                        num -= keywordValue
                                # to handle if a word do not have a number in the end of the word
                                except:
                                    num += 1

            # obtain the category with the highest weight or also can be called similarity
            if num > maxNum:
                optionalResponse = []
                maxNum = num
                print(f.readline())
                # get all possible response
                while True:
                    temp = f.readline()
                    if not temp.__contains__("---------"):
                        optionalResponse.append(temp)
                    else:
                        break
                # finalResponse = f.readline()
            num = 0
    # get random response if optional response is not empty else print default finalResponse
    if not len(optionalResponse) == 0:
        # if only one response output the response
        if len(optionalResponse) == 1:
            finalResponse = optionalResponse[0]
        else:
            index = random.randint(0, len(optionalResponse))
            # print("finalResponse:" + finalResponse)
            finalResponse = optionalResponse[index]
    arr2 = finalResponse.split("\\n")
    for word in arr2:
        print(word)
    f.close()
    optionalResponse = []


def helpQuestions():
    print("So you want to know what you don't know? Here's a few things I can chat about!")
    sleep(0.6)
    print("..........")
    sleep(0.6)
    print("..........")
    sleep(0.6)
    print("..........")
    sleep(0.6)

    print("Want to know about a few of my books? Ask me about the Cat in the Hat!")
    print("Tell me about how you're feeling! I hope I'll respond appropriately")
    print("Want to know about a beloved character? Ask me about the Lorax")
    print("Try a swear word I fuckin dare you")
    print(":)")
    print("..........")
