#!/usr/bin/env python3

import random
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define variables
name = "Chatbot"
weather = "sunny"

# Define a dictionary containing list of responses for each message
responses = {
  "what's your name?": [
    "my name is {0}".format(name),
    "they call me {0}".format(name),
    "I go by {0}".format(name)
  ],
  "what's today's weather?": [
    "the weather is {0}".format(weather),
    "it's {0} today".format(weather)
  ],
  "default": [
    "I can hear you! You said: "
  ]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = responses["default"][0] + message
    return bot_message

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send a message to the bot
send_message("I love building chatbots")
send_message("what's today's weather?")
send_message("what's your name?")
