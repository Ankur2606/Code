from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot

app = Flask(__name__)
chatbot = ChatBot('FashionBot')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    response = str(chatbot.get_response(user_message))
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)