from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.response_selection import get_first_response
from chatterbot.response_selection import get_random_response
from chatterbot.logic.logic_adapter import LogicAdapter
from pytz import UTC
from datetime import datetime
from dateutil import parser as date_parser


from chatterbot.adapters import Adapter
from chatterbot.storage import StorageAdapter
from chatterbot.search import IndexedTextSearch
from chatterbot.conversation import Statement
from chatterbot.comparisons import JaccardSimilarity
from chatterbot.conversation import StatementMixin




from chatterbot import utils
from chatterbot import languages
from nltk.corpus import wordnet, stopwords
#logging.basicConfig(level=logging.INFO)









def get_feedback():

    text = input()

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()
















bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
    	
		"chatterbot.logic.MathematicalEvaluation",
		"chatterbot.logic.BestMatch"
		
		
    
    ],
   
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db"
    
)






trainer = ListTrainer(bot)



#trainer = ChatterBotCorpusTrainer(bot)


trainer.train([
    "Hi",
    "Hello!",
    "Hi there!",
    "Hello!",
    "Hello",
    "Hello!",
])

trainer.train([
    "How are you ?",
    "I am fine you ?",
])


trainer.train([
    "Thank you.",
    "No problem, how may I help you ?",
    "Thanks.",
    "No problem, how may I help you ?",
])

trainer.train([
    "Exam dates ?",
    "Dates are : 21.01.2021",
])

trainer.train([
    'when are the exams?',
    'they start tomorrow',
    'do we have any exams coming up?',
    'tomorrow',
    'when are we having our exams?',
    'tomorrow',
    'when are the exams expected to begin?',
    'tomorrow'
])

trainer.train([
    "When does the finals week start?",
    "Finals week start at January 13, 2021.",
    "Thanks"
    "Can I help you with something else?",
])

trainer.train([
    "What are exam dates?",
    "Exam dates are : 21.01.2021",
    "Exam dates?",
    "Exam dates are : 21.01.2021",
    "What is the exam dates?",
    "Exam dates are : 21.01.2021",
    "Dates for the exams?",
    "Exam dates are : 21.01.2021",
    
])

trainer.train([
    'when should I start my internship?',
    'after the 2nd semester',
    'when do internships usually start?',
    'after the second semester',
    'when am I expected to start my internship?',
    'after the 2nd semester',
    'when do students start their internships?',
    'after the 2nd semester',
    'when should we start our internship?',
    'after the 2nd semester'
])

trainer.train([
    'what is it that you do?',
    'I am an AI ChatBot for Ankara University',
    'what are you?',
    'I am an AI ChatBot for Ankara University',
    'what is your purpose?',
    'I am an AI ChatBot for Ankara University',
    'what are your main functions?',
    'I am an AI ChatBot for Ankara University'
])



trainer.train([
    "Can i get professor contact info",
    "Who would you like to get contact info of? (James Smith or Sarah Parks?)",
    "Professor info",
    "Who would you like to get contact info of? (James Smith or Sarah Parks?)",
    "Professor contact info",
    "Who would you like to get contact info of? (James Smith or Sarah Parks?)",
    "professor info",
    "Who would you like to get contact info of? (James Smith or Sarah Parks?)",
    "professor contact info",
    "Who would you like to get contact info of? (James Smith or Sarah Parks?)",
    "James Smith",
    "James Smith Phone: 555-666-7788, e-Mail: jamessmith@mail.com",
    "james smith",
    "James Smith Phone: 555-666-7788, e-Mail: jamessmith@mail.com",
    "Sarah Parks",
    "Sarah Parks Phone: 555-444-3322, e-Mail: sarahparks@mail.com",
    "sarah parks",
    "Sarah Parks Phone: 555-444-3322, e-Mail: sarahparks@mail.com"

])

trainer.train([
    "Can i get my student certificate",
    "Name: Arthur Dent'-----'Student ID: 182959'-----'Department: Computer Engineering'-----'Grade: 3'-----'This student is currently enrolled in Computer Engineering Department.",
    "Can I get student certificate",
    "Name: Arthur Dent'-----'Student ID: 182959'-----'Department: Computer Engineering'-----'Grade: 3'-----'This student is currently enrolled in Computer Engineering Department.",
    "Student certificate",
    "Name: Arthur Dent'-----'Student ID: 182959'-----'Department: Computer Engineering'-----'Grade: 3'-----'This student is currently enrolled in Computer Engineering Department.",
    "student certificate",
    "Name: Arthur Dent'-----'Student ID: 182959'-----'Department: Computer Engineering'-----'Grade: 3'-----'This student is currently enrolled in Computer Engineering Department.",

])

trainer.train([
   "Hey AnkuBot. Are you sentient?",
   "Robots should die."

])




#Var.compare('cat is very hungry.','Deniz is very hungry.')


#print('value:',c)

#trainer.train(
#    "chatterbot.corpus.english"
#)

#chatbot = ChatBot("Johnny Five", read_only=True)

# Create a new instance of a ChatBot

#response_selection_method=get_most_frequent_response


print('Hello there, I am Ankara University ChatBot. How may I help you ?')







'''
A =Statement("cat very hungry.")
B =Statement("the young cat hungry.")
Var = JaccardSimilarity()

c = JaccardSimilarity().compare(A,B)
'''



while True:
	try:	
		
		text=input('User: ')
		if(text=='quit' or text=='exit'):
			break
		
		
		input_statement = Statement(text)
		response = bot.get_response(input_statement)
		
		
		

		if(response.confidence < 0.60):
			print("\nThis answer has a low confidence level\n")
			print('Confidence Number :',response.confidence)
			print('\n Is "{}" a coherent response to "{}"? \n'.format(response.text,input_statement.text))
       		
       		
			
			if get_feedback() is True:
				print('Confidence level increased!')
				bot.learn_response(response, input_statement)
				
				
       		 
			else:
				print('please input the correct one')
				A=Statement(input('User: '))
				
				
				#A.save()
				
				
				bot.learn_response(A, input_statement)
				print('Responses added to bot!')
	
		if(response.confidence > 0.60):
			print("This answer has a high confidence level\n")
			print('Confidence Number :',response.confidence)
			print('\n',response)
        	
		
    
    
    
    
    
    # Press ctrl-c or ctrl-d on the keyboard to exit
	except (KeyboardInterrupt, EOFError, SystemExit):
		break








    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
