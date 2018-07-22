# Title:       vigenere.py
# Version:     1.0.3
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


    ## Takes a letter from the user and turns it into a number between 0 and 25 to use
    #  as a key for encryption or decryption
    #  @param char a character to use as a key
    #  @return charKey an integer between 0 and 25
    #
    def ChToKey(self, char):
        if char.islower():
            char = char.upper()

        if char >= "A" and char <= "Z":
            offset = ord("A")
        else:
            # Not a letter
            return None

        charKey = ord(char) - offset
        return(charKey)


    ## Removes all characters not found in the alphabet from an input string and
    #  converts all characters  to uppercase.
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


    ## Encrypts upper- and lowercase characters by shifting them according to a key.
    #  @param ch the letter to be encrypted
    #  @param key the encryption key
    #  @param mode a character that determines the operation E for encryption, and
    #   D for decryption
    #  @return the encrypted letter
    #
    def crypt(self, ch, key, mode):
        LETTERS = 26   #Number of letters in the Roman alphabet

        if ch >= "A" and ch <= "Z":
            base = ord("A")
        else:
            return ch   # Catch-all: Not an uppercase letter

        if mode.upper() == "E":
            offset = ord(ch) - base + key
        elif mode.upper() == "D":
            offset = ord(ch) - base - key

        if offset >= LETTERS:
            offset = offset - LETTERS
        elif offset < 0:
            offset = offset + LETTERS

        return(chr(base + offset))


    ## Decrypts a message with the Vigenere cipher
    #  @param message the string to decrypt
    #  @return the decrypted string
    #
    def decrypt(self, message):
        tempMes = self.convertStr(message)
        newMes = ""
        tempKey = 0
        j = 0

        for char in tempMes:
            tempKey = self.ChToKey(self.vigPass[j % len(self.vigPass)])
            newMes += self.crypt(char, tempKey, "D")
            j += 1


        return(self.formatStr(newMes))

    ## Encrypts a message with the Vigenere cipher
    #  @param message the string to decrypt
    #  @return the encrypted string
    #
    def encrypt(self, message):
        tempMes = self.convertStr(message)
        newMes = ""
        tempKey = 0
        j = 0

        for char in tempMes:
            tempKey = self.ChToKey(self.vigPass[j % len(self.vigPass)])
            newMes += self.crypt(char, tempKey, "E")
            j += 1

        return(self.formatStr(newMes))


    ## Sets a new password to be used for encryption/decryption
    #  @param newPass a string to be used as the password
    #
    def setPassword(self, newPass):
        tmp = self.convertStr(newPass)
        if len(tmp) == 0:
            raise IndexError("Error: Bad password. Password must contain only letters")
        else:
            self.vigPass = tmp
            #print(self.vigPass)
