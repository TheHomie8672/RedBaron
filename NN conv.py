import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import json
import numpy as np


# Load the data from the JSON file
with open('data.csv', 'r') as f:
    data = json.load(f)

# Preprocess the data
corpus = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        # Tokenize the pattern
        words = nltk.word_tokenize(pattern)
        # Add the tokenized pattern to the corpus
        corpus.append(' '.join(words))
        
# Create a bag-of-words representation of the preprocessed data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
def generate_response(user_input, X):
    # Tokenize the user input
    words = nltk.word_tokenize(user_input)
    # Convert the tokenized user input to a bag-of-words representation
    user_input_bow = vectorizer.transform([' '.join(words)])
    # Calculate the cosine similarity between the user input and the preprocessed data
    similarities = cosine_similarity(user_input_bow, X)
    # Get the index of the most similar pattern
    index = np.argmax(similarities)
    # Get the corresponding intent
    intent = data['intents'][index]
    # Get a random response from the intent
    response = random.choice(intent['responses'])
    return response

# Start the conversation
print("Chatbot: Hi, how can I help you today?")

# Loop to continuously prompt the user for input and generate a response
while True:
    # Get user input
    user_input = input("You: ")
    # End the conversation if the user types "bye"
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    # Generate a response from the chatbot
    response = generate_response(user_input, X)
    print("Chatbot: " + response)
    
def generate_response(user_input, X):
    # Tokenize the user input
    words = nltk.word_tokenize(user_input)
    # Convert the tokenized user input to a bag-of-words representation
    user_input_bow = vectorizer.transform([' '.join(words)])
    # Calculate the cosine similarity between the user input and the preprocessed data
    similarities = cosine_similarity(user_input_bow, X)
    # Get the index of the most similar pattern
    index = np.argmax(similarities)
    # Get the corresponding intent
    intent = data['intents'][index]
    # Get a random response from the intent
    response = random.choice(intent['responses'])
    # If the similarity score is below a threshold, return a default response
    if similarities[0][index] < 0.5:
        response = "I'm sorry, I don't understand. Can you please rephrase your question?"
    return response

# Greeting message
print("Chatbot: Hi, I'm a chatbot. How can I help you today?")

# Loop to continuously prompt the user for input and generate a response
while True:
    # Get user input
    user_input = input("You: ")
    # End the conversation if the user types "bye"
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    # Generate a response from the chatbot
    response = generate_response(user_input, X)
    print("Chatbot: " + response)
    
# Greeting message
print("Chatbot: Hi, I'm a chatbot. How can I help you today?")

# Loop to continuously prompt the user for input and generate a response
while True:
    # Get user input
    user_input = input("You: ")
    # End the conversation if the user types "bye"
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    # Generate a response from the chatbot
    response = generate_response(user_input, X)
    # If the response is the default response, ask the user to rephrase their question
    if response == "I'm sorry, I don't understand. Can you please rephrase your question?":
        print("Chatbot: " + response)
        continue
    # If the response is not the default response, print it to the console
    else:
        print("Chatbot: " + response)  
        
