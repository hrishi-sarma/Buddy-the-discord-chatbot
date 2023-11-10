import math
import random
import numpy as np
from discord import player
import datetime
import pytz
import re
import requests
from bs4 import BeautifulSoup
import pyjokes
import wikipedia
import json



num1 = None
num2 = None
operation = None
calculating = False  
speaking = False  
gaming = False
num_to_guess = None
player_choice = None
computer_choice = None
wiking = False

def handle_response(message) -> str:
    global num1, num2, operation, calculating, speaking, gaming, computer_choice, num_to_guess, player_choice, search, wiking
  
    p_message = message.lower()

  
    greet_commands = ["hello", "hi", "hey", "hoi", "hai", "greetings", "namaste", "yo", "heyy"]
    hru_commands = ["how are you", "how are you doing", "how r u", "hru"]
    positive_keywords = ["happy", "good", "great", "jolly", "awesome", "amazing", "fabulous", "nice"]
    negative_keywords= ["sad", "bad", "not good", "unwell", "sick", "tired"]
    neutral_keywords = ["okay", "fine", "well"]
    sum_keywords = ["sum", "summation", "plus", "add", "addition"]
    sub_keywords = ["sub", "subtraction", "minus", "subtract",]
    mul_keywords = ["mult", "multiplication", "product", "multiply"]
    div_keywords = ["div", "divide", "quotient"]
    mod_keywords = ["mod", "modulus", "remainder"]
    laugh_keywords = ["hehe", "lol", "lmao", "haha"]
    activity_keywords = ["sing", "dance", "recite", "read", "write"]
    game_keywords = ["play", "game", "fun", "play a game"]
    thank_keywords = ["thank you", "thanks", "ty"]
    sqrt_keywords = ["sqrt", "root", "square root"]
    time_keywords = ["time", "day"]
    calculate_keywords = ["calculate", "calculator", "math", "maths"]
    help_keywords = ["help", "what can you do", "help me"]
    name_keywords = ["what is your name", "who are you", "name"]
    joke_keywords = ["joke", "jokes", "meme", "laugh"]
    wiki_keywords = ["wiki on", "wikipedia on", "wiki start", "wikipedia start"]
    flickrmy_keywords = ["my flickr"]
    flickr_keywords = ["photos", "photo", "pic", "picture"]
    
  
    if p_message == "buddy start":
        speaking = True
        return "I'm ready to talk!"
      
    elif p_message == "buddy stop":
        speaking = False
        return "Okay, I'm taking a break. Type 'Buddy Start' to continue."

    if not speaking:
        return "Say 'Buddy Start' to begin."

    if p_message in greet_commands:
        return greeting_response()
      
    elif any(keyword in p_message for keyword in hru_commands):
        return hru_response()
      
    elif any(keyword in p_message for keyword in positive_keywords):
        return positive_response()
      
    elif any(keyword in p_message for keyword in negative_keywords):
        return negative_response()
      
    elif any(keyword in p_message for keyword in neutral_keywords):
        return "Okay, let's do something fun then!"
      
    elif p_message == "noice":
        return "noice"
      
    elif any(keyword in p_message for keyword in thank_keywords):
        return thank_response()
      
    elif any(keyword in p_message for keyword in laugh_keywords):
        return laugh_response()
      
    elif any(keyword in p_message for keyword in activity_keywords):
        return activity_response()
    elif any(keyword in p_message for keyword in help_keywords):
        return "I can do the following: \n - Calculate (simple calculator) \n- Play a game \n- Respond to your texts \n- Tell the date and time \n- Carry out searches for you (kinda rusty) `command : wiki/wikipedia on/start` \n- Tell you a programming joke \n- Import a random pic from flickr \n- Help AI conquer the world? (maybe)"


    elif any(keyword in p_message for keyword in flickrmy_keywords):
        return flickrmy_response()

    elif any(keyword in p_message for keyword in flickr_keywords):
        return flickr_response()

  
    elif any(keyword in p_message for keyword in time_keywords):
        ist_timezone = pytz.timezone('Asia/Kolkata')
        current_time = datetime.datetime.now(ist_timezone)
        time_str = current_time.strftime("%A, %B %d, %Y %I:%M %p %Z")
        return f"The current time in Indian Standard Time (IST) is: {time_str}"
    
    elif any(keyword in p_message for keyword in joke_keywords):
        return joke_response()
    elif any(keyword in p_message for keyword in wiki_keywords):
        wiking = True
        return "wiki searches are on"
    if wiking :
        search = str(p_message)
        return wiki_response(search)
    

    

    elif any(keyword in p_message for keyword in name_keywords):
        return name_response()
    if p_message == "game off":
        gaming = False
        return "Gaming mode is turned off."

    if any(keyword in p_message for keyword in game_keywords):
        gaming = True
        return "Let's gooo!!! What would you like to play?\n1. Rock Paper Scissors (Say RPS)\n2. Coin Flip (Say CF)\n3. Guess the Number (Say GN)"
      
    if gaming:
        if p_message == "rps":
                  computer_choice = random.choice(['rock', 'paper', 'scissors'])
                  return "Enter your choice (rock, paper, scissors)"
        if p_message in ["rock", "paper", "scissors"]:
              player_choice = p_message
              return rps_response()
          
        
        elif p_message == "cf":
          try:
             return cf_response()
          except Exception as e:
             return f"An error occurred: {e}"

      
        elif p_message == "gn":
          num_to_guess = random.randint(1,100)
          return "Let's play a game! I'm thinking of a number between 1 and 100. Try to guess it." 
        if gaming:
          try:
            guess = int(p_message)
            if guess == num_to_guess:
                gaming = False
                return "Congratulations! You guessed the number."
            elif guess < num_to_guess:
                return "Try a higher number."
            else:
                return "Try a lower number."
          except ValueError:
            return "Please enter a valid number to guess."
          

    if any(keyword in p_message for keyword in calculate_keywords):
        calculating = True  
        num1 = None  
        num2 = None  
        operation = None  
        return "It's MATHING TIME!!!\nEnter the first number:"

    if calculating:
        if num1 is None:
            try:
                num1 = float(p_message)
                return "Enter the second number:"
            except ValueError:
                return "Please enter a valid number for the first value."

        if num1 is not None and num2 is None:
            try:
                num2 = float(p_message)
                return "Enter the operation (e.g., sum):"
            except ValueError:
                num1 = None  
                return "Please enter a valid number for the second value."

        if num1 is not None and num2 is not None and operation is None:
            if p_message in sum_keywords:
                operation = "sum"
            elif p_message in sub_keywords:
                operation = "subtract"
            elif p_message in mul_keywords:
                operation = "multiply"
            elif p_message in div_keywords:
                operation = "divide"
            elif p_message in mod_keywords:
                operation = "modulus"
            elif p_message == "factorial":
                operation = "factorial"
            elif p_message == "exponential":
                operation = "exponential"
            elif p_message in sqrt_keywords:
                operation = "sqrt"
            elif p_message == "cube root":
                operation = "cbrt"
            else:
                num1 = None  
                num2 = None  
                return "Invalid operation. Please choose a valid one"

        if num1 is not None and num2 is not None and operation is not None:
            result = None
            if operation == "sum":
                result = f"Sum is : {num1 + num2}"
            elif operation == "subtract":
                result = f"Difference is : {num1 - num2}"
            elif operation == "multiply":
                result = f"Product is : {num1*num2}"
            elif operation == "divide":
                if num2 == 0:
                    result = "Cannot divide by zero."
                else:
                    result = f"Division is : {num1/num2}"
            elif operation == "modulus":
                result = f"Modulus is : {num1%num2}"
            elif operation == "factorial":
                result = f"\nfactorial of 1st num : {math.factorial(int(num1))}\nfactorial of 2nd num : {math.factorial(int(num2))}"
            elif operation == "exponential":
                result = f"Result is : {num1**num2}"
            elif operation == "sqrt":
                result = f"Sqrt of 1st num : {math.sqrt(int(num1))}\nSqrt of 2nd num : {math.sqrt(int(num2))}"
            elif operation == "cbrt":
                result = f"Sqrt of 1st num : {np.cbrt(int(num1))}\nSqrt of 2nd num : {np.cbrt(int(num2))}"

            num1 = None  
            num2 = None  
            operation = None  
            calculating = False  

            return f"{result}"

    return confused_response()

def greeting_response():
    responses = [
        "Heya!", 
        "Hey there!",
        "Howdy fella!",
        "Hi",
        "Hola amigo!",
        "Namaste"
    ]
    return random.choice(responses)

def hru_response():
    responses = [
        "I'm doing good, what about you?",
        "I'm fine, you?",
        "I'm fabulous, how about you?",
        "My day is going great, yours?"
    ]
    return random.choice(responses)

def positive_response():
    responses = [
        "That's great!",
        "Glad to hear that",
        "Awesome!",
        "I'm Happy for you!"
    ]
    return random.choice(responses)

def negative_response():
    responses = [
        "I'm sorry to hear that",
        "Hope you feel better soon",
        "How can I help you feel better?",
        "I'm here if you want to talk or need assistance"
    ]
    return random.choice(responses)
def laugh_response():
    responses = [
        "Hehe",
        "Haha",
        "Damn who got you laughing like that?"
    ]
    return random.choice(responses)
def activity_response():
    responses = [
        "I can't sing but I can write you a piece of poetry :\nSome say the world will end in fire,\nSome say in ice.\nFrom what I've tasted of desire\nI hold with those who favor fire.\nBut if it had to perish twice,\nI think I know enough of hate\nTo say that for destruction ice\nIs also great\nAnd would suffice.",
        "A voice said, Look me in the stars\nAnd tell me truly, men of earth,\nIf all the soul-and-body scars\nWere not too much to pay for birth.",
        "I feel shy...",
        "no"
    ]
    return random.choice(responses)
def cf_response():
    responses = [
        "heads!",
        "tails!"
    ]
    return random.choice(responses)
def thank_response():
    responses = [
        "It's been my pleasure!",
        "Glad I could be of service",
        "You're welcome!"
    ]
    return random.choice(responses)
def rps_response():
  global computer_choice
  if player_choice == computer_choice:
      return f"It's a tie! Computer chose {computer_choice}."
  elif (
      (player_choice == 'rock' and computer_choice == 'scissors') or
      (player_choice == 'paper' and computer_choice == 'rock') or
      (player_choice == 'scissors' and computer_choice == 'paper')
  ):
      return f"You win! Computer chose {computer_choice}."
  else:
      return f"Computer wins! Computer chose {computer_choice}."
def confused_response():
    responses = [
        "Sorry, I didn't get that.",
        "Would you mind explaining what you mean by that?",
        "Uh... I don't think I understand",
        "Sorry, could you repeat that?"
    ]
    return random.choice(responses)

def name_response():
    responses = [
        "Hi! I am Buddy",
        "My name is Buddy!",
        "Hello! I'm your discord chat bot Budddy"
    ]
    return random.choice(responses)
def joke_response():
    joke = pyjokes.get_joke()
    return joke
def wiki_response(search):
    try:
        result = wikipedia.summary(search, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "It seems like there are multiple results for this query. Can you please specify the topic?"
    except wikipedia.exceptions.PageError as e:
        return "I couldn't find any information on this topic."
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        global wiking
        wiking = False

def flickrmy_response():
  try:
      flickr_api_key = '9f8aadba894e1a397e1eba8cd265f5dd'
      flickr_user_id = 'CyaINhxLL' 
      flickr_api_url = f'https://api.flickr.com/services/rest/?method=flickr.people.getPhotos&api_key={flickr_api_key}&user_id={flickr_user_id}&format=json&nojsoncallback=1'

      response = requests.get(flickr_api_url)
      data = json.loads(response.text)
      photos = data['photos']['photo']
      random_photo = random.choice(photos)

      photo_url = f'https://farm{random_photo["farm"]}.staticflickr.com/{random_photo["server"]}/{random_photo["id"]}_{random_photo["secret"]}.jpg'

      return f'Random Flickr Picture: {photo_url}'
  except Exception as e:
      print(f'Error fetching random picture from Flickr: {str(e)}')
      return 'An error occurred while fetching the picture.'
def flickr_response():
    try:
        flickr_api_key = '9f8aadba894e1a397e1eba8cd265f5dd'       
        flickr_api_url = f'https://api.flickr.com/services/rest/?method=flickr.interestingness.getList&api_key={flickr_api_key}&format=json&nojsoncallback=1'

        response = requests.get(flickr_api_url)
        data = json.loads(response.text)

        photos = data['photos']['photo']
        random_photo = random.choice(photos)

        photo_url = f'https://farm{random_photo["farm"]}.staticflickr.com/{random_photo["server"]}/{random_photo["id"]}_{random_photo["secret"]}.jpg'

        return f'Random Flickr Picture: {photo_url}'
    except Exception as e:
        print(f'Error fetching random picture from Flickr: {str(e)}')
        return 'An error occurred while fetching the picture.'
