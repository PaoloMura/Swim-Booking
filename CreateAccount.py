#Hashlib library is imported.
#SQLite3 library is imported.
#The database containing all tables to be used is connected.
import hashlib
import sqlite3
from Window import Window

conn = sqlite3.connect('SwimSchool.db')
conn.text_factory = str
c = conn.cursor()


class CreateAccount(Window):
    def __init__(self, parent=None):
        pass
        
    #passHash takes in a single parameter to be hashed
    def passHash(self, astring):
        #This formats the parameter correctly for the
        #the hashing algorithm
        formatted = str(astring).encode('utf-8')
        #This converts the parameter to a hashed value
        #and returns the hash to the main program
        return hashlib.sha384(formatted).digest()

    #The validateUN function takes in a username
    #and returns whether or not it is valid
    def validateUN(self, ausername):
        #This accesses all records with a username that matches the parameter
        c.execute('SELECT * FROM Parents WHERE Username=?', (ausername,))
        existingusernames = c.fetchall()
        #If none exist, True is returned, else False (where True refers to valid)
        if len(existingusernames) == 0:
            return True
        else:
            return False

    #The validatePassword() function takes in
    #a single password as a parameter and returns
    #True for valid and False for invalid
    def validatePass(self, password):
        #The password must be at least 8
        #characters long
        if len(password) >= 8:
            #This checks whether there are any
            #uppercase characters in password
            if any(map(str.isupper, password)):
                #This checks whether there are
                #any integers in password
                if any(map(self.isInt, password)):
                    return True
        return False

    #The createAccount procedure creates a new record in the Parents table.
    #The details parameter is an array containing the inputted details from
    #the CreateAccount window: 
    # [ParentID, Name, Surname, Username, Password, Email, Phone, Postcode]
    def createAccount(self, details):
        #This validates the username
        if self.validateUN(details[3]):
            #This validates the email
            if self.validateEmail(details[5]):
                #This validates the password
                if self.validatePass(details[4]):
                    #This validates the name
                    if self.validateName(details[1]):
                        #This validates the surname
                        if self.validateName(details[2]):
                            #This hashes the password and updates details
                            hashedpassword = self.passHash(details[4])
                            details[4] = str(hashedpassword)
                            #This creates a new record in Parents using details
                            c.execute('INSERT INTO Parents VALUES (?,?,?,?,?,?,?,?)', details)
                            conn.commit()
                            return ['Accepted', 'Account has been successfully created']
                        else:
                            return ['Rejected', 'Please enter a name with no numbers or symbols']
                    else:
                            return ['Rejected', 'Please enter a name with no numbers or symbols']
                else:
                    return ['Rejected', 'Choose a strong password with at least 8 characters, an uppercase letter and a number']
            else:
                return ['Rejected', 'Invalid email']
        else:
            return ['Rejected', 'Username already exists']

    #This accesses and returns the email address of the Admin
    def getHelpEmail(self):
        c.execute('SELECT EmailAddress FROM Parents WHERE ParentID=1')
        return c.fetchone()[0]
        
        