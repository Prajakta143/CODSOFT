def chatbot_responce(user_input):
    user_input = user_input.lower()

    if user_input == "hi" or user_input == "hello" or user_input == "hey":
        return "Hello! How can i help you?"
    
    elif user_input == "how are you?":
        return "I'm fine, thank you!"
    
    elif user_input == "what is your name ":
        return "I'm a simple chatbot."
    
    elif user_input == "help":
        return "i can respond to greetings and simple questions."
    
    elif user_input == "bye":
        return "Goodbye! Have a ice day "
    
    else:
        return "Sorry, i dont understand."
    
print("Chatbot: Hello! Type 'bye' to exit. ")

while True:
    user_input = input("You:")
    response = chatbot_responce(user_input)
    print("Chatbot:", response)

    if user_input.lower() == "bye":
        break