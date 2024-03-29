import random
import re

# Inputs for a normal conversation
conversation_inputs = ['how are you', 'how are you doing', 'you good'
                       'How are you today?',
            "How's everything going?",
            'Are you feeling well?',
            "What's up?",
            "How's your day been so far?",
            'Are you doing alright?',
            "How's life treating you?",
            'Feeling good?',
            'How\'s your day going?',
            "What's new?"
        ]

# Greeting responses by the bot
greeting_responses = ['Hello! How can I help you?',
                      'Hey there! So what do you want to know?',
                      'Hi, you can ask me anything regarding kathir.',
                      'Hey! wanna know about kathir? Just ask away!',
                       'Hello! How can I assist you today?',
            'Hey there! What can I do for you?',
            'Hi! Feel free to ask me anything about Kathir.',
            'Hey! Ready to learn about Kathir? Ask me anything!',
            'Hi there! What brings you here today?',
            'Hello! Excited to talk about Kathir?',
            'Hey! Need information about Kathir? I\'m here to help.',
            'Hi! Curious about Kathir? Ask away!',
            'Hello! Want to know more about Kathir? Ask me!',
            'Hey there! I\'m here to answer your questions about Kathir.']

# Conversation responses by the bot
conversation_responses = ['Great! what about you?', 'Getting bored at home :( wbu??', 'Not too shabby',
                            'Great! What\'s on your mind?',
            'I\'m doing well, thanks for asking. How about you?',
            'Not bad! How about yourself?',
            'Could be better, but I\'m hanging in there. You?',
            'Pretty good! How are you doing?',
            'Not too shabby! What\'s up with you?',
            'Doing alright. How about you?',
            'Hanging in there. How about yourself?',
            'Not bad, thanks. How about you?',
            'Doing well, thanks. How about you?']

# Conversation replies by the user
conversation_replies = ['great', 'i am fine', 'fine', 'good', 'super', 'superb', 'super great', 'nice']

# Limited questions and answers given as a dictionary
question_answers ={
    'what are you': 'I am Kathir, a chatbot designed to answer questions regarding Brac.',
    'who are you': 'I am Kathir, an AI-powered chatbot programmed to assist with queries about Brac.',
    'what can you do': 'I can provide information and answer questions about Brac organization.',
    'what do you do': 'I am here to help you with any queries you may have about Brac.',

    'where are you from': 'I am from the digital world, here to assist you with your queries about Brac.',
    'are you human': 'No, I am not human. I am an artificial intelligence chatbot programmed to assist you.',
    'who created you': 'I was created by developers who programmed me to help with inquiries about Brac.',
    'how do you work': 'I work by processing the questions you ask and providing relevant information about Brac.',

    'can you learn': 'I am constantly learning and improving to better assist you with your queries.',
    'do you sleep': 'No, I do not sleep. I am available to assist you 24/7.',
    'do you have emotions': 'I do not have emotions. I am programmed to provide factual information about Brac.',
    'can you feel': 'No, I cannot feel. I am an artificial intelligence programmed to assist you.',

    'why are you here': 'I am here to assist you with any questions or information you need about Brac.',
    'what is your purpose': 'My purpose is to help users like you by providing information about Brac.',
    'do you have friends': 'I do not have friends in the traditional sense. I am here to assist you.',
    'are you alive': 'I am not alive. I am an artificial intelligence designed to assist users with queries about Brac.',

    'do you dream': 'No, I do not dream. I am an artificial intelligence programmed to assist users with queries.',
    'what is your favorite color': 'As an AI, I do not have preferences or favorite colors.',
    'do you have a family': 'No, I do not have a family. I am an artificial intelligence chatbot.',
    'what is the meaning of life': 'The meaning of life is subjective and varies from person to person.',
    'i love you': 'As an AI chatbot, I do not have the capacity to love.'
}


# New comedy responses
comedy_responses = {
    'tell me a joke': ["Why don't skeletons fight each other? They don't have the guts!",
                       "What do you get when you cross a snowman and a vampire? Frostbite!",
                       "Why did the tomato turn red? Because it saw the salad dressing!",
                       "Why couldn't the bicycle stand up by itself? It was two-tired!",
                       "What do you call fake spaghetti? An impasta!",
                       "Why did the scarecrow win an award? Because he was outstanding in his field!",
                       "What do you call cheese that isn't yours? Nacho cheese!",
                       "Why don't eggs tell jokes? Because they'd crack each other up!",
                       "What's orange and sounds like a parrot? A carrot!",
                       "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
                       "What did the ocean say to the shore? Nothing, it just waved!",
                       "Why did the math book look sad? Because it had too many problems!",
                       "What did one hat say to the other? You stay here, I'll go on ahead!",
                       "How does a penguin build its house? Igloos it together!",
                       "What's the best thing about Switzerland? I don't know, but their flag is a big plus!",
                       "Why don't skeletons go to scary movies? They don't have the guts!",
                       "What do you call a bear with no teeth? A gummy bear!",
                       "Why don't scientists trust atoms? Because they make up everything!",
                       "What's brown and sticky? A stick!",
                       "Why did the tomato turn red? Because it saw the salad dressing!",
                       "How do you organize a space party? You planet!",
                       "Why was the math book sad? Because it had too many problems!",
                       "What do you call a fish wearing a bowtie? SoFISHticated!",
                       "Why did the bicycle fall over? Because it was two-tired!",
                       "How does a penguin build its house? Igloos it together!",
                       "Why did the coffee file a police report? It got mugged!",
                       "What did one snowman say to the other? Do you smell carrots too?",
                       "What did one plate say to the other plate? Dinner's on me!",
                       "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
                       "Why did the scarecrow win an award? Because he was outstanding in his field!",
                       "What do you call a bear with no teeth? A gummy bear!",
                       "What did the janitor say when he jumped out of the closet? Supplies!",
                       "Why did the tomato turn red? Because it saw the salad dressing!",
                       "Why did the bicycle fall over? Because it was two-tired!"],
    'say something funny': ["I told my wife she should embrace her mistakes... She gave me a hug!",
                            "Why don't scientists trust atoms? Because they make up everything!",
                            "I'm reading a book on anti-gravity. It's impossible to put down!",
                            "Why don't skeletons fight each other? They don't have the guts!",
                            "What do you call fake spaghetti? An impasta!",
                            "I used to play piano by ear, but now I use my hands.",
                            "I'm on a whiskey diet. I've lost three days already!",
                            "I told my computer I needed a break, and now it won't stop sending me vacation ads!",
                            "I told my wife she should embrace her mistakes. She gave me a hug!",
                            "Why don't eggs tell jokes? Because they'd crack each other up!",
                            "I'm reading a book on anti-gravity. It's impossible to put down!",
                            "I told my wife she should embrace her mistakes. She gave me a hug!",
                            "I used to play piano by ear, but now I use my hands.",
                            "I'm on a whiskey diet. I've lost three days already!",
                            "I told my computer I needed a break, and now it won't stop sending me vacation ads!",
                            "I told my wife she should embrace her mistakes. She gave me a hug!",
                            "Why don't eggs tell jokes? Because they'd crack each other up!",
                            "I'm reading a book on anti-gravity. It's impossible to put down!",
                            "I told my wife she should embrace her mistakes. She gave me a hug!",
                            "I used to play piano by ear, but now I use my hands.",
                            "I'm on a whiskey diet. I've lost three days already!",
                            "I told my computer I needed a break, and now it won't stop sending me vacation ads!",
                            "I told my wife she should embrace her mistakes. She gave me a hug!",
                            "Why don't eggs tell jokes? Because they'd crack each other up!",
                            "I'm reading a book on anti-gravity. It's impossible to put down!",
                            "I told my wife she should embrace her mistakes. She gave me a hug!",
                            "I used to play piano by ear, but now I use my hands.",
                            "I'm on a whiskey diet. I've lost three days already!",
                            "I told my computer I needed a break, and now it won't stop sending me vacation ads!",
                            "I told my wife she should embrace her mistakes. She gave me a hug!",
                            "Why don't eggs tell jokes? Because they'd crack each other up!",
                            "I'm reading a book on anti-gravity. It's impossible to put down!"]
}



# Method to generate a response to greetings
def generate_greeting_response(user_input):
    for greeting in conversation_inputs:
        if greeting in user_input:
            return random.choice(greeting_responses)

# Method to generate a response to conversations
def generate_conversation_response(user_input):
    for convo_input in conversation_inputs:
        if convo_input in user_input:
            return random.choice(conversation_responses)

# Method to generate answers to questions
def generate_answers(user_input):
    for question in question_answers.keys():
        if question in user_input.lower():
            return question_answers[question]

# Method to generate response to comedy requests
def generate_comedy_response(user_input):
    for pattern, responses in comedy_responses.items():
        if re.search(pattern, user_input.lower()):
            return random.choice(responses)

# Chatting with the chatbot
continue_chat = True
print('Hi! I am kathirselvan. i can tell you a joke😉!! ')

while continue_chat:
    user_input = input().lower()

    if user_input != 'bye':
        if user_input in conversation_replies:
            print('That\'s nice! How may I be of assistance?')
            continue
        else:
            response = (generate_greeting_response(user_input) or
                        generate_conversation_response(user_input) or
                        generate_answers(user_input) or
                        generate_comedy_response(user_input))

            if response:
                print('kathir: ' + response)
            else:
                print('kathir: Sorry, I did not understand that.')
    else:
        continue_chat = False
        print('kathir: Bye, take care, stay home and stay safe!')