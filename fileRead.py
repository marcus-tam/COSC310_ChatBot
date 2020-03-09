


def check(question):

    arr = question.split(" ")
    maxNum = 0
    num = 0
    try:
        f = open("response.txt", "r")
        finalResponse = "Sorry I don't understand."
        for line in f:
            if line.__contains__("Question"):
                questionArray = f.readline()
                for word in arr:
                    if questionArray.__contains__(word):
                        num += 1
                if num > maxNum:
                    maxNum = num
                    print(f.readline())
                    finalResponse = f.readline()
                num = 0
        print("finalResponse:" + finalResponse)
        f.close()
    except:
        print("eer")


while "1" == "1":
    question = input("ask a question")
    check(question)
