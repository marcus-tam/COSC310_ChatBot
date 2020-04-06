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

* Books: Dr. Seuss is a world renowned author, ask him about what books he has written. For example "What books have you wrote?", "Can you show me your book list?" or "Tell me about The Cat in the Hat".
* Films: Dr. Seuss's books have been addapted into multiple successful films throughout the years, ask him about it. For example "Tell me about How the Grinch Stole Christmas" or "Tell me about Gerald McBoing-Boing".
* Emotions: Feeling happy? Feeling sad? Dr. Seuss is known for his inspirational words, tell him how you feel. For example "I am feeling sad", "I am feeling happy" or "I am bored".
* Swear Words: Dr. Seuss was a children's book writter, he does not like curse words, that doesn't mean you shouldn't try to see what happens.

# About Our Code

Using python and a simple txt file, the project is comprised of:
~~* `animations.py`: Consist of a text animation showing The Cat in the Hat.~~
* `chatbot.py`: This runs the chatbot, detecting the user's inputs and outputing the bot's response.
* `fileread.py`: This recognizes the user's input and choosing the appropriate response from another text file.
* `responses.txt`: This is where all possible inputs are stored (weighing each word accordingly) and housing all the different categories, which each conatains a possible responses.
* `norm_punc.py`:
* `phrasal.py`:
* `postagging.py`:
* `processSentence.py`: //TODO: John to make brief summary on each
* `responsehp.txt`: This is a new topic very similar to responses.txt, but the data stored in here is related to JK Rowling.
* `sever.py`:
* `spell.py`:
* `synonym.py`:
* `test.py`:

---------

# New Features added in A3

* Add a new simple GUI
* Add a new topic (JK Rowling)
* When user input is out of scope, chatbot will respond appropriately with varying responses
* Multiple ToolKits
  * Synonym Recognition
  * POS tagging
  * Phrasal
* Handles spelling mistakes
* Communication with other chatbots via Sockets

1. GUI

The new GUI is built with Tkinter. 

** INSERT IMAGE HERE

2. New Topic

The user can now have a conversation with JK Rowling about various things, like Harry Potter!

** INSERT IMAGE HERE

3. Various Responses to out of scope questions

Now the chatbot will output various responses when no appropriate response is detected.

** INSERT IMAGE HERE

4. Multiple toolkits

  * a) Synonym Recognition
  
  * b) POS tagging
  
  * c) Phrasal
  
5. Handling Spelling Mistakes

//For john to briefly explain -- similar to about our code section

** INSERT IMAGE HERE

6. Sockets

  * a) Client
  
  * b) Server
  
  
