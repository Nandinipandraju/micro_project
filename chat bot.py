grievances_data = [
    {"id": 1, "query": "How do I file a grievance?", "category": "filing", "response": "Go to the CPGRAMS portal and click on 'Lodge Grievance'."},
    {"id": 2, "query": "What is the procedure for tracking my grievance?", "category": "tracking", "response": "After logging in, click on 'View Status of Your Grievances'."},
    # Add more examples here
]
pip install chatterbot
import chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize the ChatBot
chatbot = chatterbot.ChatBot('CPGRAMS Grievance Chatbot')

# Train the chatbot with the mock dataset
for grievance in grievances_data:
    chatbot.set_trainer(ChatterBotCorpusTrainer)
    chatbot.train([grievance['query'], grievance['response']])

# Example conversation
print("User: How do I file a grievance?")
response = chatbot.get_response(None)
print("ChatBot: " + str(response))

print("User: What is the procedure for tracking my grievance?")
response = chatbot.get_response(None)
print("ChatBot: " + str(response))