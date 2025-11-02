"""
Mad Libs Story Generator
Author: Nihal Patel
Description:
A simple interactive python project that takes user inputs(noun, verbs, adjectives)
and builds a funny story dynamically. Perfect for beginners learning about 
functions, string formatting, and input/output in python.
"""

#Function to get user input with a prompt
def get_input(word_type: str)->str:
    user_input: str=input(f"Enter a {word_type}: ").strip()
    while not user_input:
        user_input=input(f"Enter a valid {word_type}: ").strip()
    return user_input

print("Welcome to the Mad Libs Story Generator")

noun1=get_input("noun")
adjective1=get_input("adjective")
verb1=get_input("verb")
noun2=get_input("another noun")
verb2=get_input("another verb")

story= f"""
🌟 Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} all day.

One day, {noun2} walked into the room and caught the {noun1} in the act.

{noun2}: "What are you doing?"
{noun1}: "I'm just {verb1}ing, what's the big deal?"
{noun2}: "Well, it's not every day that you see a {noun1} {verb1}ing in the middle of the day."
{noun1}: "I guess you're right. Maybe I should take a break."
{noun2}: "That's probably a good idea. Why don't we go {verb2} instead?"
{noun1}: "Sure, that sounds like fun!"

🎉 And so, {noun2} and the {noun1} went off to {verb2} and had a great time.
The end.

"""

print("\n"+"="*60)
print(story)
print("="*60)
print("Story ")