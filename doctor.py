"""
Chapter 5 Case Study (Pages 136 - 139)
Program: doctor.py
3/5/2025

Application that simulates an interactive session of nondirective psychotherapy
"""

import random

# Global variables of various lists of data that all functions can share
hedges = ("Please, tell me more.", "Many of my patients tell me the same thing.", "Please, continue", "Go on, go on...", "You don't say", "Please elaborate")

qualifiers = ("Why do you say that ", "You seem to think that", "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "am":"are", "are":"am", "you":"I"}

# Definition of the reply() function
def reply(sentence):
	"""Builds and returns a reply to the user input."""
	probability = random.randint(1 , 4)
	if probability == 1:
		return random.choice(hedges)
	else:
		return random.choice(qualifiers) + changePerson(sentence)

# Definition of the changePerson() function
def changePerson(sentence):
    """Replaces first-person pronouns with second-person pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
    	replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)	

# Definition of the main() function
def main():
	"""Handles the interaction between user and doctor."""
	print("Good day, I hope you are well today.")
	print("What can I do for you?")
	while True:
		sentence = input("\nType your response or QUIT to exit >> ")
		if sentence.upper() == "QUIT":
			input("Have a great day! Press ENTER to exit this program >> ")
			break
		print(reply(sentence))
		
# Global call to main() for program entry
if __name__ == '__main__':
	 main()	 