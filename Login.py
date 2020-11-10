#SQLite3 library is imported.
#The database containing all tables to be used is connected.
import sqlite3
from CreateAccount import CreateAccount

conn = sqlite3.connect('SwimSchool.db')
conn.text_factory = str
c = conn.cursor()


class Login(CreateAccount):
    def __init__(self):
        pass

    #The login procedure logs in the current user.
    #The username and password parameters are passed from the UI.
    def login(self, username, password):
        password = str(self.passHash(password))
        c.execute('SELECT * FROM Parents WHERE Username=?', (username,))
        if len(c.fetchall()) == 0:
            return ["Rejected", "Username not found"]
        else:
            #This accesses the relevant details from the record with the entered username
            c.execute('SELECT ParentID, Password FROM Parents WHERE Username=?', (username,))
            #The accessed details are stored
            accesseddetails = c.fetchone()
            accessedid = accesseddetails[0]
            accessedpassword = str(accesseddetails[1])
            #This checks whether the password is correct
            if password == accessedpassword:
                #The current user is set
                global currentuser
                currentuser = accessedid
                #Take the user to the appropriate page
                return ["Accepted", currentuser]
                
            else:
                return ["Rejected", "Incorrect password"]
