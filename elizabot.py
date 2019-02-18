#!/usr/bin/env python3

import random, re
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a match-rule dictionary for the phrase to answer
rules = {
  'I want (.*)': [
    'What would it mean if you got {0}',
    'Why do you want {0}',
    "What's stopping you from getting {0}"
  ],
  'do you remember (.*)': [
  'Did you think I would forget {0}',
  "Why haven't you been able to forget {0}",
  'What about {0}',
  'Yes .. and?'
  ],
  'do you think (.*)': [
  'if {0}? Absolutely.',
  'No chance'
  ],
  'if (.*)': [
    "Do you really think it's likely that {0}",
    'Do you wish that {0}',
    'What do you think about {0}',
    'Really--if {0}'
  ]
}

# Define a list of responses for phrase not in rules dictionary
replies = {
  '(.*)(\?)': [
    "I don't know :(",
    'You tell me!',
    "Sorry, I don't know \\O/"
  ],
  '(.*)(\.)': [
    'tell me more!',
    'why do you think that?',
    'how long have you felt this way?',
    'I find that extremely interesting'
  ],
  '(.*)(\!)': [
  	'oh wow!',
    ':)'
  ]
}

# Define replace_pronouns()
def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my', 'your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you', 'I', message)
    # Return message
    return message

def match_rule(rules, user_input):
    response = "default"
    phrase = None
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, user_input)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Iterate over the replies if no rules found
    if response == "default":
    	for pattern, responses in replies.items():
        	# Check for a match
        	match = re.search(pattern, user_input)
        	if match is not None:
        		# Choose a random response
        		response = random.choice(responses)
    # Return the response and phrase
    return response, phrase

# Define a function that responds to a user's message:
def respond(user_input):
	# Call match_rule
    response, phrase = match_rule(rules, user_input)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    # Return a "default" response
    elif response == "default":
    	response = "I can hear you! You said: {0}".format(user_input)
    # Return the response
    return response

# Define a function that sends a message to the bot:
def send_message(user_input):
    # Print user_template including the user_input
    print(user_template.format(user_input))
    # Get the bot's response to the user_input
    response = respond(user_input)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


'''
# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("do you remember your last birthday?")
send_message("do you think humans should be worried about AI")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")
'''
