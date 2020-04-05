import fileRead as fr
import animations as anim
from tkinter import *
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
#anim.introAnimation()
#
# print("------------------------------------------------")
# username = input("Welcome to Talk With Seuss! Please enter the name you would like to be called by. ")
# print("Hello " + username + ", My name is Theodor Seuss Geisel, but you can just call me Dr. Suess ;)")
# print("If you are curious as to what to ask me, type 'help' to get a list of topics to chat about! (Type 'quit() to "
#       "end program)")
# print("")


# while True:
#     question = input("User input -> ")
#
#     if question.__contains__("quit()"):
#         print("Don't cry because it's over \nSmile because it happened :) ")
#         print("Goodbye! May we meet again!")
#         break
#     if question.lower().__eq__("help"):
#         fr.helpQuestions()
#     else:
#         fr.check(question)
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(socket.gethostname(), 1234)
# while True:
#     msg = s.recv(1024)
#     print(msg.decode("UTF-8"))


def getLine():
    message = text_sent.get('0.0', END)
    return message


def sendMessage():
    message = getLine()
    content = 'me ' + time.strftime('%Y-%M-%D %H:%M:%S', time.localtime()) + '\n'
    text_list.insert(END, content, 'sendcolor')
    text_list.insert(END, ' '+message)
    s.sendall(message.encode("UTF-8"))
    question = s.recv(1024).decode("UTF-8")
    if question.__contains__("quit()"):
        s.close()
        quit(1)
    else:
        getMessage(question)


def getMessage(rep):
    content = 'chatbot ' + time.strftime('%Y-%M-%D %H:%M:%S', time.localtime()) + '\n'
    text_list.insert(END, content, 'rescolor')
    text_list.insert(END, rep)
    text_list.see(END)


def enter():
    sendMessage()


root = Tk()
root.title("Talk with Seuss")
root.geometry("600x600")
frame_output = Frame(root, width=600, height=300)
frame_input = Frame(root, width=600, height=150)
frame_button = Frame(root, width=600, height=50)
text_list = Text(frame_output)
text_list.tag_configure('sendcolor', foreground='blue')
text_list.tag_configure('rescolor', foreground='red')
text_sent = Text(frame_input)
send = Button(frame_button, text='Send', font=10, command=sendMessage)
text_sent.bind('<Return>', enter)
frame_output.propagate(0)
frame_output.grid(row=0, column=0)
frame_input.propagate(0)
frame_input.grid(row=1, column=0)
frame_button.propagate(0)
frame_button.grid(row=2, column=0)
send.pack()
text_list.pack()
text_sent.pack()
root.mainloop()
