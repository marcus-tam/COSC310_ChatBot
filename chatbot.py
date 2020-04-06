import fileRead as fr
import animations as anim
import spell as sp
import phrasal

def startchatbot():
    anim.introAnimation()

    print("------------------------------------------------")
    username = input("Welcome to Talk With Seuss! Please enter the name you would like to be called by. ")
    print("Hello " + username + ", My name is Theodor Seuss Geisel, but you can just call me Dr. Suess ;)")
    print(
        "If you are curious as to what to ask me, type 'help' to get a list of topics to chat about! (Type 'quit() to "
        "end program)")
    print("")
    while True:
        question = input("User input -> ")
        processedQuestion = phrasal.processQuestion(question)
        correctedQuestion = sp.checkCorrection(processedQuestion)
        if question.__contains__("quit()"):
            print("Don't cry because it's over \nSmile because it happened :) ")
            print("Goodbye! May we meet again!")
            break;
        if correctedQuestion.lower().__eq__("help"):
            fr.helpQuestions()
        else:
            print(fr.check(correctedQuestion))


while __name__ == '__main__':
    startchatbot()
