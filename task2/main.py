# MoodSense Chatbot

print('Welcome to MoodSense, your mental wellness assistant!\n') # Initial welcome message

name = input('Please enter your name for a more personalised experience: ') # Name input

# Function to check mood
def checkMood(level):
    """
    The function checks the mood level that is input and returns a response based on the input
    :param level: (1-10) This is a scale of the users mood
    :return: Appropriate response
    """
    if level <=3:
        return f'Sorry you are feeling this way, {name}. Consider talking to a friend/family member or taking some time for yourself.'
    elif level <=7:
        return f"Seems like you're feeling okay, {name}! Remember it is important to take breaks and reflect on yourself!"
    elif level <=10:
        return f"That's amazing to hear, {name}! Keep up the positive vibes!"
    else:
        return 'Error: Please enter an integer between 1 and 10.'

moodInput = input(f'Hello, {name}! On a scale of 1 to 10, how would you describe your mood today? ') # Mood input for user

# if statement to check if moodInput is a number and call function
if moodInput.isdigit():
    level = int(moodInput)
    response = checkMood(level)
    print(response)
else:
    print('Error: Please enter an integer between 1 and 10.')