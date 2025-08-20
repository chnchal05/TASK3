import nltk
from nltk.chat.util import Chat, reflections

# Predefined pairs for pattern-response
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing good! How about you?", "All great! Thanks for asking."]
    ],
    [
        r"what is your name ?",
        ["I am your Python chatbot.", "You can call me ChatBot!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "See you later!", "Bye! Have a great day!"]
    ],
    [
        r"who created you ?",
        ["I was created with Python and NLTK.", "A developer using Python made me!"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you and answer simple questions.", "Right now, I’m here to talk and help you out!"]
    ],
    [
        r"where are you from ?",
        ["I live inside your computer 😄", "I’m from the world of Python code!"]
    ],
    [
        r"tell me a joke",
        ["Why don’t programmers like nature? It has too many bugs!", 
         "Why did the computer go to the doctor? Because it caught a virus!"]
    ],
    [
        r"who is your best friend ?",
        ["You are my best friend!", "Obviously, it’s you 💖"]
    ],
    [
        r"do you like python ?",
        ["Of course! Python is my favorite language 🐍", "Yes, Python makes me who I am!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Anytime!", "Glad I could help!"]
    ],
    [
        r"what is your hobby ?",
        ["Learning new things and answering questions!"]
    ],
]
def codtech_chatbot():
    print("🚀 CodTech AI Chatbot")
    print("Type 'quit' to end the chat\n")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Start chatbot
if __name__ == "__main__":
    codtech_chatbot()
