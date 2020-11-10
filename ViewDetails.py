#View Details Class
#SQLite3 library is imported.
#The database containing all tables to be used is connected.
import sqlite3
from Window import Window
conn = sqlite3.connect('SwimSchool.db')
c = conn.cursor()


class ViewDetails(Window):
    def __init__(self, uifile):
        self.useless = "Remove this later"

    #The confirm procedure updates the contact email and bank details.
    #The email parameter is the admin's contact email address.
    #The bankdetails parameter is the bank details to be used for invoices
    def confirm(self, email, bankdetails):
        #This validates the email
        if self.validateEmail(email):
            #This ensures that the length is no more than 100 characters
            if self.lengthCheck(bankdetails,None,None):
                #details is an array of the parameters to be passed to the SQL query
                details = [email, bankdetails, 1]
                #This modifies the record of the admin using details
                c.execute('''UPDATE Parents
                            SET EmailAddress=?,
                            Postcode=?
                            WHERE ParentID=?''', details)  #A ParentID of 1 will always refer to the admin
                conn.commit()
            else:
                print('Please enter bank details using up to 100 characters')
        else:
            print('Invalid email')

'''
#email is to receive the updated email from the ViewDetails window 
newemail = "robert@email.com"
#newbankdetails is to receive the updated bank details from the ViewDetails window
newbankdetails = "12-34-56, 12345678"
confirm(newemail, newbankdetails)
'''
conn.close()

