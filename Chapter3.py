# write a function that returns the larger of two numbers
# input is two numbers
# output is the larger of the two numbers


import functools


def larger_number(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"
    
# call the larger function with the values 290 and 570
# store the result in a variable called result
# then print result

result = larger_number(290, 570)
print(result)



# Functions 3.3 

def funct1(): print("there")
def funct2(): print("my")
funct2()
print("friend")
def funct3(): print(".")
funct3()
print("")
def funct3(): print(".")
def funct4():print("well")
print("Hi")
funct1()
print("I'm")
funct4()
funct3()
print("")
print("Bye.")


#Functions 3.6.1
def money_made(num_shares, purchase_share_price, current_share_price):
# num_shares is the number of shares of a stock that we purchased. purchase_share_price is the price of each of those shares. current_share_price is the current share price. Return the amount of money we have earned on the stock.
    return (current_share_price - purchase_share_price) * num_shares
#Simpler way to do this 
# price_difference = current_share_price - purchase_share_price
# return num_shares * price_difference

#Function 3.6.2 (Strong Password)

def is_strong_password(password):
# A strong password is not the word 'password' and is not the word 'qwerty'. Return True if the password is a strong password, False if not.
    if password != "password" and password != "qwerty":
        return True
    else:
        return False
    
def is_strong_password(password):
# A strong password has at least one uppercase character, at least one number, and at least one special symbol. Return True if the password is a strong password, False if not.
    uppercase = False
    number = False
    special_symbol = False
    for character in password:
        if character.isupper():
            uppercase = True
        elif character.isdigit():
            number = True
        elif character in "!@#$%^&*()_+-={}[]|\:;\"'<>?,./":
            special_symbol = True
    return uppercase and number and special_symbol

# Keep asking the user for a password until it is a strong password, and return that strong password.
def get_strong_password():
    password = input("Enter a password: ")
    while not is_strong_password(password):
        print("That password is not strong enough.")
        password = input("Enter a password: ")
    return password

#Function 3.6.3 (Points Scrabble)


def num_points(word):
#Each letter is worth the following points:
#a, e, i, o, u, l, n, s, t, r: 1 point
#d, g: 2 points
#b, c, m, p: 3 points
#f, h, v, w, y: 4 points
#k: 5 points
#j, x: 8 points
#q, z: 10 points
#word is a word consisting of lowercase characters.
#Return the sum of points for each letter in word.
    points = 0
    for character in word:
        if character in "aeioulnstr":
            points += 1
        elif character in "dg":
            points += 2
        elif character in "bcmp":
            points += 3
        elif character in "fhvwy":
            points += 4
        elif character in "k":
            points += 5
        elif character in "jx":
            points += 8
        elif character in "qz":
            points += 10
    return points

#Function 3.6.4 (Scrabble Best Word)

def best_word(word_list):
#word_list is a list of words. Return the word worth the most points.
    best_word = ""
    best_points = 0
    for word in word_list:
        points = num_points(word)
        if points > best_points:
            best_points = points
            best_word = word
    return best_word