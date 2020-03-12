import fileRead as fr
import animations as anim

anim.introAnimation()

print("------------------------------------------------")
name = input("Welcome to talk with Seuss! Please enter the name you would like to be called by. ")
print("Hello " + name + ", My name is Theodor Seuss Geisel, but you can just call me Dr. Suess ;)")
print("If you are curious as to what to ask me, type 'help' to get a list of topics to chat about!")
print("")
while True:
    question = input("User input -> ")

    if question.__contains__("quit()"):
        print("Goodbye!")
        break
    if question.lower().__eq__("help"):
        fr.helpQuestions()
    else:
        fr.check(question)