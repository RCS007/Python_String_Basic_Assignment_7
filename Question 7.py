# Question 7

# Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word
# begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes
# ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and
# change it into Pig Latin. Make sure the new word is displayed in lower case.

# Ask the user to enter a word
word = input("Enter a word: ").lower()

# Define vowels
vowels = "aeiou"

# Check if the first letter is a vowel
if word[0] in vowels:
    pig_latin = word + "way"
else:
    pig_latin = word[1:] + word[0] + "ay"

# Display the Pig Latin word
print(f"Pig Latin: {pig_latin}")