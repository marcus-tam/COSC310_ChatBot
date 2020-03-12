# Doctor Dr. Seuss COSC310_A2

### Description

This project aims to build a working chatbot with at least 30 consecutive lines of interaction between the bot and the user. The current "role" of the bot is that of Dr. Seuss, this means that the user will be limited to talking about Dr. Seuss's work and about the user's feeings. 

### How does it work?

The bot currently has access to *number* categories, all ranging from 3-5 possible responses. These categories are all arranged to a certain general theme: Dr. Seuss's work, Dr. Seuss, the user's feelings, greetings, every-day activities, and possible inapropriate comments. This all begins with the bot asking the user's name, then the bot proceeds to introduce itself and offers the user help on what they could talk about. Then comes the user's first input, whatever the input is, the bot will search for the appropriate response and wait for the user's next input. This process will continue to loop until the user decides to exit.

### How to use the ChatBot

1. Run the command line interface of your preference (eg. command prompt).
2. Redirect the directory to the location of the file.
3. On console, type `python chatbot.py`

Once the main animation has loaded, the bot will ask you to input your name in order for it to refer to you during the conversation. It will then provide you with the option of typing `help` in order to know what can the bot talk about, it's up to you if you want to use this feature or just go directly to a conversation.

* 

Using python and a simple txt file, the project is comprised of 4 files: The first file (animations.py) consist of a text animation showing The Cat in the Hat; the second file (chatbot.py) is what runs the chatbot, detecting the user's inputs and outputing the bot's response; the third file (fileread.py) is in charge of recognizing the user's input and choosing the appropriate response from another text file; the last file (responses.txt) is a text file which is in charge of storing all possible inputs (weighing each word accordingly) and housing all the different categories, which each conatains a possible responses.
