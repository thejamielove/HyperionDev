# "string" variable, asks the user to input a string
# "string_length" variable, converts "string" into integers using the len function to calculate length of string & is used for "range" function argument in for loop
# "update_string" variable, used to hold updated string with each alternate character as uppercase or lowercase
string = input("Enter a string:\n > ")
string_length = len(string)
update_string = ""

for index in range (string_length):
    if index % 2 == 0:
        update_string += string[index].upper() # upper case for even index characters
    
    else:
        update_string += string[index].lower() # lower case for odd index characters

print("Alternating case:", update_string)

# "words" variable, used to split out "string" user inputed with a space
# "words_length" variable, converts "words" into integers using len function to calculate length of words & is used for "range" function argument in for loop
# "update_word" variable, used to hold updated word with each alternative word lower and uppercase
words = string.split()
words_length = len(words)
update_word = ""

for index in range (words_length):
    if index % 2 == 0:
        update_word += words[index].lower() # lower case for even index word
    
    else:
        update_word += words[index].upper() # upper case for odd index word
    
    update_word += " " # adds back space after each word so the update_word has the same spaces as original string

print("Alternating words:", update_word)