cypher_num = 0
while True:
    try:
        cypher_num = int(input("What is the cypher (enter a number between 1-26): "))
        break

    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error occurred")
print("Cypher has been stored")

message = input("Enter the message you want to encrypt: ")
secret_message = ""
for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += cypher_num

        if char.isupper():
           if char_code > ord("Z"):
               char_code -= 26
           elif char_code < ord("A"):
               char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        secret_message += chr(char_code)
    else:
        secret_message += char
print("Here is your secret message: {}".format(secret_message))
# Decode if you know the cypher
decoded_message = ""
for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code -= cypher_num

        if char.isupper():
           if char_code > ord("Z"):
               char_code += 26
           elif char_code < ord("A"):
               char_code -= 26
        else:
            if char_code > ord("z"):
                char_code += 26
            elif char_code < ord("a"):
                char_code -= 26
        decoded_message += chr(char_code)
    else:
        decoded_message += char

check_message = input("Do you want to check message, y/n: ")
if check_message == "Y" or check_message == "y":
    print("The deocoded message is: {}".format(decoded_message))
elif check_message == "N" or check_message == "n":
    print("The deocoded message is remains a secret")
else:
    print("I said y or n dummy")