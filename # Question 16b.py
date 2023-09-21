Upcoming
Woohoo, no work due in soon!

Announce something to your class

Announcement: '2020 HL Paper Q16(B) - Starting Code'
Emma Delaney
Created 20 May20 May
2020 HL Paper Q16(B) - Starting Code

2020 HL Q16B Base Code.py
Text


Announcement: 'Base code for Monday 2020 Q16 A…'
Emma Delaney
Created 20 May20 May
Base code for Monday 2020 Q16 A starting Code HL

2020 HL Q16A base code.py
Text

Assignment: "Homework"
Emma Delaney posted a new assignment: Homework
Created 17 May17 May
Material: 'Revision Cards'
Emma Delaney posted a new material: Revision Cards
Created 17 May17 May
Material: 'Revision Resources'
Emma Delaney posted a new material: Revision Resources
Created 13 May13 May

Announcement: 'https://replit.com/join/opdigkkgfq-emma…'
Emma Delaney
Created 13 May13 May
https://replit.com/join/opdigkkgfq-emmadelaney


Announcement: 'Online course: Learn how to create a…'
Emma Delaney
Created 13 May13 May
Online course:

Learn how to create a neural network using JavaScript. No libraries necessary. You'll code your own self-driving car simulation and implement every component step-by-step. You'll learn how to implement the car driving mechanics, define the environment, and detect collisions. (3 hour YouTube course): https://www.freecodecamp.org/news/self-driving-car-javascript


Announcement: 'IADT Free computing summer camps.…'
Emma Delaney
Created 11 May11 May
IADT Free computing summer camps. Spaces will be limited so sign up today if you are interested:

IADT FREE Computing Camps – June 13th – 15th June on Campus 10am to 3.30pm. 

IADT Summer Camps – Creative Computing - IADT
Camp 1: Young Women in Computing
https://www.eventbrite.ie/e/iadt-young-women-in-computing-summer-camp-tickets-150697665775
Camp 2: Creative Coding
https://www.eventbrite.ie/e/iadt-creative-coding-summer-camp-tickets-331813983557
Camp 3: Game Development
https://www.eventbrite.ie/e/iadt-game-development-summer-camp-tickets-331831215097?aff=erelpanelorg

Material: 'HTML to call back from firebase'
Emma Delaney posted a new material: HTML to call back from firebase
Created 10 May10 May
Material: 'script file content'
Emma Delaney posted a new material: script file content
Created 10 May10 May
# Question 16(b)
# Examination Number:
 
# A variable to store all the lower case letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
 
def calculate_score(password):
# The variables lowercase and uppercase indicate the presence or
# absence of lowercase and uppercase characters in the password
    lowercase = False #True if password contains a lowercase letter
    uppercase = False #True if password contains an uppercase letter 1
# Loop through each character in the password and ...
# ... check the password for specific characters
    for character in password:
        if character in LOWER_CASE_LETTERS:
            lowercase = True
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True
        
# Calculate the score based on the rules

    score = 0

# Rule 1
    if len(password) > 7:
        score = score + 5
    # Rule 2
    if lowercase: 
        score = score + 1
    # Rule 3 
    if lowercase and uppercase:
        score = score + 5
    return score

# Test driver
test_passwords = ["sun", "Sun", "Sunshine", "12345", "123456789"]
for password in test_passwords: 
    pass_score = calculate_score(password)
    print(pass_score)