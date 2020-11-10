import string


class Window:
    def __init__(self,uifile):
        pass

    #The isInt function checks whether a
    #character is an integer and returns
    #True if it is or False if not
    def isInt(self, character):
        try:
            character = int(character)
        except:
            return False
        else:
            return True

    #The validateEmail function takes in an email as a
    #parameter and returns True for valid and False
    #for invalid
    def validateEmail(self, email):
        #Length must be greater than 7 characters
        if len(email) > 7:
            #The @ character must be contained in the string
            if email.count("@") == 1:
                #The last four characters must be the substring
                #.com
                if email[len(email)-4:] == ".com":
                    return True
        return False

    #The validateName() function takes in a single name as a parameter
    #and returns True for valid or False for invalid
    def validateName(self, name):
        #name must be at least 1 character long 
        if len(name) > 1:
            #This checks whether there are any integers in name
            if not any(map(self.isInt, name)):
                #This creates a set of unacceptable characters, i.e.
                #all punctuation except for apostrophes
                unacceptedchars = set(string.punctuation.replace("'",""))
                #This checks whether there are any unacceptable characters
                #in name
                if not any(char in unacceptedchars for char in name):
                    return True
        return False

    #The lengthCheck() function takes in a string and the min and
    #max lengths as parameters. It returns True for valid and False for invalid
    def lengthCheck(self, string, minlength, maxlength):
        #if min and max lengths not set, they are set to 0 and 100 by default
        if minlength == None:
            minlength == 0
        if maxlength == None:
            maxlength = 100
        #This checks that the length is between min and max characters
        if (len(string) >= minlength) and (len(string) <= maxlength):
            return True
        else:
            return False

