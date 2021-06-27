# # string concatination practice scripts.
# There are multiple methods to print in python
# to comment a block of codes, use Ctrl K + Ctrl C
madlib1="Madlib Prgram"
madlib2="Rajesh Kongath"
madlib3="========================"

# Method 1, to print the heading

print("This is ",madlib1)

# Method 2, 

print("Created by {}".format(madlib2))

# Method 3

print(f"***{madlib3}***")

adj= input ("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb : ")
famous_person = input("Input person : ")


madlib = f"Computer programming is so {adj}! It makes me so excited all the time becase \
I love to {verb1}. Stay hydrated and {verb2} Like you are {famous_person}!"

print (madlib)