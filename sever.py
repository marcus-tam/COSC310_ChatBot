import socket
import sys
import fileRead as fr
import animations as anim
import spell as sp
import phrasal

import stanfordcorenlp

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(1)
ifCorrected = False
ifCheckedCorrection =False
ifAsked=False
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    count=0
    while True:
        data = clientsocket.recv(1024)
        respond = data.decode("utf-8")
        if not data:
            sys.exit()
        if count==0:
            respond=anim.getPicture()
            count+=1
        elif count==1:
            respond="Hello " + respond + "My name is Theodor Seuss Geisel, but you can just call me Dr. Suess" \
                                         ") \n If you are curious as to what to ask me, type 'help' to get a list of " \
                                         "topics to chat about! (Type 'bye' to end program)"
            count += 1
        else:
            processedQuestion = phrasal.processQuestion(respond)
            if ifCheckedCorrection and not ifCorrected:
                if processedQuestion.lower().__contains__("yes" or "yea" or "yep"):
                    respond=correctedQuestion[1]
                    ifCorrected = True
                elif processedQuestion.lower().__contains__("no" or "nope" or "nah"):
                    respond=correctedQuestion[0]
                    ifCorrected = True
                else:
                    ifCheckedCorrection=False
                    ifCorrected = False
            if not ifCheckedCorrection:
                correctedQuestion = sp.checkCorrectionViaSocket(processedQuestion)
                ifCheckedCorrection = True
                if correctedQuestion[0] == correctedQuestion[1]:
                    ifCorrected = True
                    respond=correctedQuestion[0]
                else:
                    ifCorrected=False
                    respond="Do you mean " + correctedQuestion[1]+" ?"
            if ifCorrected:
                if respond.__contains__("bye"):
                    respond = "Don't cry because it's over \nSmile because it happened :) \n Goodbye! May we meet again!"
                    clientsocket.sendall(respond.encode("utf-8"))
                    clientsocket.close()
                if respond.__contains__("help"):
                    respond = fr.getHelp()
                else:
                    respond = fr.check(respond)
                ifCorrected = False
                ifCheckedCorrection = False
                respond+="\n"
        clientsocket.sendall(respond.encode("utf-8"))
