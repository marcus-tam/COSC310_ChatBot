from numpy import random


def check(question):
    arr = question.split(" ")
    maxNum = 0
    num = 0
    f = open("response.txt", "r")
    finalResponse = "Sorry I don't understand."
    optionalResponse = []
    for line in f:
        # Coordinate the question word array
        if line.__contains__("Question"):
            questionArray = f.readline().split(" ")
            for word in arr:
                for questionWord in questionArray:
                    # this .__contain__ will change to "==" when the response.txt is done
                    # weight system: each word has a weight(0-9) to calculate the similarity of the input sentence\
                    if questionWord[:(len(questionWord) - 2)] == word or questionWord[:(len(questionWord) - 1)] == word:
                        # handle the last word for each questionArray, which is "something/n"
                        try:
                            if questionWord[len(questionWord) - 1] == "\n":
                                num += int(questionWord[len(questionWord) - 2])
                            else:
                                num += int(questionWord[len(questionWord) - 1])
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
            index = random.randint(0, len(optionalResponse) - 1)
            # print("finalResponse:" + finalResponse)
            finalResponse = optionalResponse[index]
    arr2 = finalResponse.split("\\n")
    for word in arr2:
        print(word)
    f.close()


while "1" == "1":
    question = input("ask a question")
    if question.__contains__("end"):
        print("Goodbye!")
        break
    else:
        check(question)
