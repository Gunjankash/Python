# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)
# language = 'Python'
# pto = language[0:6:2] #
# print(pto) 

#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

string =['Thirty', 'Days', 'Of', 'Python']
print(" ".join(string))

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

string_2 = ['Coding', 'For' , 'All' ]
print(" ".join(string_2))

# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().

company = "Coding For All"
print(company)

# Print the length of the company string using len() method and print().

print(len(company))

# Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Change all the characters to lowercase letters using lower() method.

print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.

print(company[7:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.find("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.

print(company.replace("Coding","Python"))

# Change Python for Everyone to Python for All using the replace method or other methods.

print(company.replace("All","Everyone"))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

string_3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string_3.split(", "))

# What is the character at index 0 in the string Coding For All.
coding = "Coding For All"
print(coding[0])
# What is the last index of the string Coding For All.
last_index = len(coding)-1
print(last_index)
# What character is at index 10 in "Coding For All" string.

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
# Use rfind to determine the position of the last occurrence of l in Coding For All People.

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind("because"))
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(sentence[31:54])

# Does ''Coding For All' start with a substring Coding?
code = 'Coding For All'
print(code.startswith("Coding"))
# Does 'Coding For All' end with a substring coding?
code = 'Coding For All'
print(code.endswith("coding"))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print( '   Coding For All      '.strip())
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python #this one

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
string_4 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("\ ".join(string_4))
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print("The area of radius {} is {}".format(radius,area))
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8 
b = 6
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b:.2f}')
print(f'{a}%{b}={a%b}')
print(f'{a}//{b}={a//b}')
print(f'{a}**{b}={a**b}')