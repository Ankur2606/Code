from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot
chatbot = ChatBot('FashionBot')

# Create a new trainer for the chat bot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chat bot on English language data
trainer.train('chatterbot.corpus.english')

# Run the chat bot service
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chatbot.get_response(user_input)
        print("FashionBot:", response)