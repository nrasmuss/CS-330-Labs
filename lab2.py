
#Due: February 6th at the beginning of class

#Nicole Rasmussen

# Each of the sentences below are followed by a set of related instructions.
# After each instruction, add your code that does what's being asked, as well as
# a print statement that shows your work. Don't forget to print new lines as well,
# or your output will be a mess!

import re


solution_separator = "\n\n****************************************\n\n"

# For example:
s0 = "This is a test"
print(s0 + "\n")

print(solution_separator)

# 1) Write a regular expression and if statement that checks if T is the first letter
pattern = "\\d"
if re.search(pattern, s0):
    print("It starts with 'T'!" + "\n")
else:
    print("My regex is incorrect, it should detect the 'T'!" + "\n")

print(solution_separator)

# 2) Use a regular expression to decompose the string into words and place those words intp a list.
#    Extract the first word into a variable and print it
pattern = ''
words = re.split(pattern, s0)
print (words)
print("\n")
first_word = words[0]
print("The first word is: '" + first_word + "'\n")

print(solution_separator)

# 3) Split the sentence into an array of individual words called words and use a for loop to print it.
#    for each var in vars:
#        (your code here)
#
pattern = "^"
words = re.split(pattern, s0)
for word in words:
    print(word + "\n")


print(solution_separator)


# 4)
s1 = "Mary was born on September 17, 1986"
# a) Write a regular expression and if statement that checks if the name "Mary" in the sentence.
pattern = "\AMary"
if re.search(pattern,s1):
    print("The sentence starts with 'Mary'!" + "\n")
else:
    print("The setence does not start with 'Mary'!")
# b) Write a regular expression and if statement that checks if the sentence contains a 4 digit number.
pattern = "\s\d{4}"
if re.search(pattern,s1):
    print("The sentence contains a 4 digit number.")
else:
    print("The sentence does not contain a 4 digit number.")
# c) Write a regular expression to extract that number into a variable b_year and print it in this sentence:
#    "The person was born in b_year."
match = re.search(pattern, s1)
if match:
    b_year = match.group()
    print("The person was born in" + b_year)
else:
    print("We do not know what year the person was born.")
print(solution_separator)

# 5)
s2 = "The dog, named Dog, was doggedly trying to dodge the fog."
# a) Write a regular expression to match the word "dog", but not the name "Dog"
wordToFind = r"dog\b"
match = re.search(wordToFind,s2)
if match:
    print("Found: dog")
else:
    print("'dog' not found")
# b) Save the output from this match into a list and print the list to verify it is not matching anything else.
listOne = [""]
listOne[0] = match.group();
print(listOne)
# c) Write a regular expression to match "dog" and "Dog" using a flag (see the cheat sheet).
match = re.findall(wordToFind, s2, re.IGNORECASE)
if match:
    print("Found: " + str(match))
else:
    print("Did not find dog & Dog")
# d) Write a regular expression to match "dog" or "fog"
pattern = r"[d|f]+og\b"
match = re.search(pattern, s2)
if match:
    print("This sentence contains 'dog' or 'fog'.")
else:
    print("Not found")
# e) Print all outputs.
match = re.findall(pattern,s2)
if match:
    print("Found: " + str(match))

print(solution_separator)


# 6)
s3 = "18785 is the 5 digit number I want not 43744, 34553, or 11111"

# a) Write a regular expression to extract the first number (try to do it without using the exact string).
pattern = r"^\d{5}"
match = re.search(pattern, s3)
if match:
    print("The first number is: " + str(match.group()))

# b) Write a regular expression to extract all numbers, store them in an array, then print the array.
pattern = r"\d+"
match = re.findall(pattern,s3)
if match:
   for num in match:
       print(num)

print(solution_separator)


# 7) Write a regular expression to trim the left and right whitespace and print the trimmed output.
s4 = "    There is preceding white space in this sentence, and whitespace at the end        "
pattern = "\s{2,}"
result = re.sub(pattern,"",s4)
print(result)

print(solution_separator)

# 8)
s5 = "junk data penguin begin tennis for 2 end begin Zelda and Link end begin Oculus Rift end no cheating by using " \
     "positional text flags"

# a) Write a regular expression to print everything from the first "begin" to the last "end".
pattern = "begin.+end"
match = re.findall(pattern, s5)
if match:
    print(str(match))
# b) Write a regular expression to print only the text from the first "begin" to the first "end"
pattern = r"begin\s\w+\s\w+\s\w+\send\b"
match = re.search(pattern, s5)
if match:
    print(str(match.group()))
# c) Write a regular expression to extract all of the text between "begin"s and "end"s into an array.
arr = []
pattern = r"begin\s(\w+\s(\w+\s){0,2})end"
m = re.findall(pattern, s5)
for item in m:
    match = item[0]
    arr.append(match)  
# d) Print all outputs.
print(arr)


print(solution_separator)


# 9)
s6 = "The date 5/17/1982 is trickier to get"
# a) Write a regular expression to extract the date.
pattern = "\d/\d{2}/\d{4}"
match = re.search(pattern, s6)
if match:
    print("Date: " + str(match.group()))
# b) Capture the date in a variable f_date
f_date = match.group()
# c) Split the date and store it as month, day, year
a = re.split("/", f_date)
month = a[0]
day = a[1]
year = a[2]
print(month)
print(day)
print(year)
# d) Convert the date to date format year-month-day where month and day always have 2 digits. Save the
#    result in comp_date
comp_date = year + "-0" + month + "-" + day
# e) Print comp_date
print(comp_date)

print(solution_separator)

