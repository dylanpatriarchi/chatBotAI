from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crea un'istanza di ChatBot
chatbot = ChatBot('ChatBot')

# Crea un'istanza di ChatterBotCorpusTrainer per addestrare il chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Addestra il chatbot sull'inglese usando il corpus di ChatterBot
trainer.train('chatterbot.corpus.english')

# Loop per l'interazione con il chatbot
while True:
    user_input = input("Tu: ")
    response = chatbot.get_response(user_input)
    print("ChatBot:", response)
