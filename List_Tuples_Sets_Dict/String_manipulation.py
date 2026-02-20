# In python, string is defined by putting text inside "" or ''
string1 = "Bonjour!!"
string2 = 'le monde!!'

# we can write multiple line text in a string by putting text inside ''' '''
string3 = ''' Hi! there, myself sam.
I am 19 years old.
I like to play football.'''

print(string1)
print(string2)
print(string3)

# we can write especial characters(means already defined for the python program) 
# in string by using escape character(\) sign
email = 'mr.sam\'bilings#@yahoo.com'
print(email)

# \n -> is used for new line in string
# \t -> is used for one tab space gap in string
print("H! Myself Zaiko.\n I am 25 years old")
print("Currently, I am studying in university. \t I love to play video games.")

# indexing in string
# Similar to list we can access an element(character) and
# perform slicing in string
string = "I am Sam."
print(string[0])
print(string[5:8])
print(string[-4:-1])
print(string[5:])
print(string[ : -1])


# ----------------------------------------------------------------------------------------------- #


# check if a text exists in the string or not
print('Sam' in string)

if 'Sam' in string:
    print("exist!!")
else:
    print("not exist!")
    
# lower() method: it converts all the characters in string into smaller letters
new_string = "I like this song"
print(new_string.lower()) 

print('Song'.lower() in new_string)

# upper() method: it converts all the characters in string into capital letters
print(new_string.upper())

print("SONG" in new_string.upper())

# we can apply lower() and upper() method in string that mixed with character 
# and numbers/special characters. In that case lower() and upper() only changes 
# the characters and skip the numbers and special characters
string_new = "Mkb123@uk.co"
print(string_new.lower())
print(string_new.upper())

# islower() method: returns a boolean True (is all the characters in string is small case letter),
# False(if all the characters in string is capital letters)
print('today'.islower())
print(string_new.islower())

# isupper() method: returns a boolean True (is all the characters in string is capital letter),
# False(if all the characters in string is small case letters)
print('TOMORROW'.isupper())
print(string_new.islower())

# we can apply islower() and isupper() method in string that mixed with character 
# and numbers/special characters. In that case islower() and isupper() only checks 
# the characters and skip the numbers and special characters
print("a123bc08".islower())
print("p28Qrc865".islower())

print("ADPQR2335".isupper())
print("abQR23PQ".isupper())


# ---------------------------------------------------------------------------------------------------- #


# some more useful methods in string
# starstwith() method: check the string whether it starts with the given text or not.
# if yes then returns True else returns False
string = "I am John."
print(string.startswith('I')) # True

# endswith() method: check the string whether it ends with the given text or not.
# if yes then returns True else returns False
print(string.endswith('John')) #False
print(string.endswith('John.')) #True

# join() method: merge a list or an array of strings into a one bigger string
# we can specify inside '' how we want to join the list of string
str_list = ["John", "Jack", "Jesicca"]
print(''.join(str_list))
print(','.join(str_list)) # join with ,
print(' '.join(str_list)) # join with space
print('+'.join(str_list)) # join with plus

# split() method: this will split the string by the mentioned character (default it is space)
# and returns a list
string_to_split = "Lord of the ring"
split_list = string_to_split.split()
print(split_list)

new_string = '''Hi! I am Jesicca.
I am 15 years old.
I study in class 8.
I love to go to school everyday.'''

new_list = new_string.split('\n')
print(new_list)

# strip() method: removes extraa spaces at the beggining and end the string text(words)
# doesn't remove space between two words.
new_str = "  Yo! how are you doing?  "
print(new_str)
print(new_str.strip())

new_str = "\tI am doing really good. and you?  "
print(new_str)
print(new_str.strip())

new_str = "\t mee to! \n"
print(new_str)
print(new_str.strip())

# if we don't want any kind of space not to be remove then we can specified which we want to remove
new_str = "\t it is nice to meet you!\n"
print(new_str)
print(new_str.strip('\t')) # only removed \t space but kept the \n and one space tab space.


# ------------------------------------------------------------------------------------------------- #