#SQLite3 library is imported.
#The database containing all tables to be used is connected.
import sqlite3
from Window import Window
conn = sqlite3.connect('SwimSchool.db')
c = conn.cursor()


class EditParent(Window):
    def __init__(self, uifile):
        self.useless = "Remove this later"

    #The validatePhone() function takes in a single phone number
    #as a parameter and returns True for valid and False for invalid
    def validatePhone(self, phonenumber):
        #This removes the whitespace in phonenumber
        phonenumber = phonenumber.replace(" ", "")
        #This checks that phonenumber has either 10 or 11 digits
        if (len(phonenumber) > 9) and (len(phonenumber) < 12):
            #This checks whether phonenumber contains digits only
            if self.isInt(phonenumber):
                #This checks whether the first digit is 0
                if phonenumber[0] == "0":
                    return True
        return False
    
    #The confirm procedure updates a chosen record in the Parents table.
    #details are the inputted details from the EditParent window. parent
    #is the ParentID of the current user
    def confirm(self, details, parent):
        #This appends the ParentID to the end of details for use in the SQL query
        details.append(parent)
        #This validates the email
        if self.validateEmail(details[2]):
            #This checks that the length is no more than 150 characters
            if self.lengthCheck(details[4],None,150):
                c.execute('''UPDATE Parents
                            SET Name=?,
                            Surname=?,
                            EmailAddress=?,
                            PhoneNumber=?,
                            Postcode=?
                            WHERE ParentID == ?''', details)
                conn.commit()
            else:
                print('Please enter an address using up to 150 characters')
        else:
            print('Invalid email')

'''
#parentdetails is to take the inputs from the EditParent window here
parentdetails = ["Jamie", "Lannister", "jimmy@gmail.com", 12345612345, "HP13 6QT"]
#parent is to be set as the ParentID of the current user
parent = 3
confirm(parentdetails, parent)
'''
conn.close()

