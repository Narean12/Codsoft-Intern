import random
import re
greetings = ["hello", "hi", "hey", "howdy"]
weather_keywords = ["weather", "temperature", "forecast"]
time_keywords = ["time", "clock"]
def generate_response(user_input):
    user_input = user_input.lower()
    if any(greeting in user_input for greeting in greetings):
        response = "Hello! How can I assist you today?"
    elif any(keyword in user_input for keyword in weather_keywords):
        response = "The weather is currently sunny with a temperature of 25°C."
    elif any(keyword in user_input for keyword in time_keywords):
        response = "The current time is 3:00 PM."
    else:
        response = "I'm sorry, I don't understand that. Can you please rephrase your question?"
    return response
print("Chatbot: Hello! How can I assist you today? (Type 'exit' to end)")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = generate_response(user_input)
    print("Chatbot:", response)