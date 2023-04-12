import string
user_input = input("enter the word to decode ")
key = int(input("what key would you like to use: "))

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
decoded_lower_letters = lower_letters[key: ] + lower_letters[:key]
decoded_upper_letters = upper_letters[key: ] + upper_letters[ :key]

letter = lower_letters + upper_letters + string.whitespace
decoded_letters = decoded_lower_letters + decoded_upper_letters + string.whitespace
encoded = user_input.translate(str.maketrans(letter, decoded_letters))
decoded = encoded.translate(str.maketrans(decoded_letters, letter))

print(encoded)
print(decoded)
#print(user_ut.translate(str.maketrans(lower_letters, decoded_letters)))
#print(user_input.translate(str.maketrans(lower_letters + " ", decoded_letters + " ")))