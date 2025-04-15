import nltk
from nltk.chat.util import Chat, reflections
import random

# Define conversation patterns with more complex expressions
pairs = [
    [
        r"hi|hello|hey|greetings",
        ["Hello there!", "Hi! How can I assist you today?", "Greetings! How can I help?"]
    ],
    [
        r"what is your name?",
        ["I'm Chatty, your personal chatbot. What can I do for you today?"]
    ],
    [
        r"how are you?",
        ["I'm doing great, thanks for asking!", "I'm here and ready to chat. How about you?"]
    ],
    [
        r"what do you do?",
        ["I chat with people, answer questions, and provide information on a variety of topics."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", 
         "Why was the math book sad? Because it had too many problems."]
    ],
    [
        r"(.*) your favorite (.*)",
        ["My favorite thing is to chat with you!", "I love chatting with people like you!"]
    ],
    [
        r"tell me about (.*)",
        ["Here's what I know about {0}: It's a really interesting topic!", "Let's talk more about {0}. It's quite fascinating."]
    ],
    [
        r"(.*) (location|city|place) ?",
        ["I don't have a physical location, but I live here, in the digital world! Where are you located?"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a wonderful day!", "See you later! Feel free to come back anytime."]
    ],
    [
        r"(.*)",
        [
            "Sorry, I didn't get that. Could you rephrase?",
            "Hmm, I didn't quite catch that. Can you clarify?",
            "Could you say that again? I didn't understand."
        ]
    ]
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Run the chatbot
def start_chat():
    print("👋 Hello! I’m Chatty. Type 'bye' or 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Goodbye! See you next time.")
            break
        response = chatbot.respond(user_input)
        if response:
            print("Chatty: " + response)
        else:
            print("Chatty: Sorry, I didn't get that. Could you rephrase?")

if __name__ == "__main__":
    start_chat()
