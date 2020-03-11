import fileRead

while True:
    question = input("ask a question")
    if question.__contains__("quit()"):
        print("Goodbye!")
        break
    else:
        fileRead.check(question)