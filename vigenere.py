# Title:       vigenere.py
# Version:     1.0.4
# Description: A simple class that implements the Vigenere cipher.
# Note: Valid Passwords MUST be at least one letter long. Otherwise the class
# will throw an error. Numbers and symbols are not valid characters in
# passwords and are ignored.

class Vigenere:
    ## Initialize the Vigenere object
    #  @param password a string to use as a password
    def __init__(self, password = "Hello world"):
        # create a variable to hold the password and set it
        self.vigPass = ""
        self.setPassword(password)


    ## Takes a letter from the user and turns it into a number between
    #  0 and 25 to use as a key for encryption or decryption
    #  @param char a character to use as a key
    #  @return an integer between 0 and 25
    #
    def chToKey(self, char):
        if char.isupper():
            return(ord(char) - ord("A"))
        elif char.islower():
            return(ord(char) - ord('a'))
        else:
            # Not a letter
            return None


    ## Removes all characters not found in the alphabet from an input
    #  string and converts all characters  to uppercase.
    #  @param text the string to be converted
    #  @return newText The new all uppercase, alpha only string.
    #
    def convertStr(self, text):
        newText = ""
        for char in text:
            if char.isalpha():
                newText += char.upper()

        return(newText)


    ## Formats a string into blocks of five characters
    # @param string the string to modify
    # @returns a new string grouping characters into sets of 5 characters
    #
    def formatStr(self, string):
        new = ""
        for i in range(len(string)):
            if(i != 0 and i % 5 == 0):
                new += " "
            new += string[i]

        return(new)


    ## Encrypts/decrypts upper- and lowercase characters using the
    #  Caesar cipher algorithm
    #  @param ch the letter to be encrypted/decrypted
    #  @param key a integer representing the key to use as a shift value
    #  @param mode a character that determines the operation
    #  E for encryption, and D for decryption
    #  @return the encrypted/decrypted letter
    #
    def crypt(self, ch, key, mode):

        if ch.isupper():
            offset = ord("A")
        elif ch.islower():
            offset = ord('a')
        else:
            return(ch)

        enc = ""

        if mode.upper() == "E":
            enc = chr((ord(ch) + key - offset) % 26 + offset)
        elif mode.upper() == "D":
            enc = chr((ord(ch) - key - offset) % 26 + offset)
        else:
            return(ch)

        return(enc)


    ## Decrypts a message with the Vigenere cipher
    #  @param string the string to decrypt
    #  @return the decrypted string
    #
    def decrypt(self, string):
        new = ""
        tempKey = 0
        j = 0

        for char in string:
            if(not char.isalpha()):
                new += char
                continue

            tempKey = self.chToKey(self.vigPass[j % len(self.vigPass)])
            new += self.crypt(char, tempKey, "D")
            j += 1


        return(new)

    ## Encrypts a message with the Vigenere cipher
    #  @param string the string to encrypt
    #  @return the encrypted string
    #
    def encrypt(self, string):
        convString = self.convertStr(string)
        new = ""
        tempKey = 0
        j = 0

        for char in convString:
            tempKey = self.chToKey(self.vigPass[j % len(self.vigPass)])
            new += self.crypt(char, tempKey, "E")
            j += 1

        return(self.formatStr(new))


    ## Sets a new password to be used for encryption/decryption
    #  @param newPass a string to be used as the password
    #
    def setPassword(self, newPass):
        tmp = self.convertStr(newPass)
        if len(tmp) == 0:
            raise IndexError("Error: Bad password. Password must contain only letters")
        else:
            self.vigPass = tmp
