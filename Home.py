#SQLite3 library is imported.
#The database containing all tables to be used is connected.
import sqlite3
from Window import Window
conn = sqlite3.connect('SwimSchool.db')
c = conn.cursor()


class Home(Window):
    def __init__(self, uifile):
        self.useless = "Remove this later"

    #The openSelCla procedure checks whether all relevant details are complete
    #and if so, opens the SelectClass window.
    #It doesn't take in any parameters but uses the globals for the ID of the
    #current parent and child
    def openSelCla(self):
        global current_parent
        global current_child
        #missingdetails if False if there are no missing details
        missingdetails = False
        #This accesses the record of the current parent
        c.execute('SELECT * FROM Parents WHERE ParentID=?',(current_parent,))
        parentdetails = list(c.fetchone())
        #This accesses the record of the current child
        c.execute('SELECT * FROM Children WHERE ChildID=?',(current_child,))
        childdetails = list(c.fetchone())
        #This iterates through each item in the parent record
        for i in range(0,len(parentdetails)):
            #Item 6 is PhoneNumber which is not necessary
            if i == 6:
                pass
            elif parentdetails[i] == None:
                missingdetails = True
        #This iterates through each item in the child record
        for j in range(0,len(childdetails)):
            #Item 4 is Disability which is not necessary
            if j == 4:
                pass
            elif childdetails[j] == None:
                missingDetails = True
        #Update the code below to interact with the UI
        if missingdetails == True:
            print('Please ensure all details are complete.')
        else:
            print('Open window')
        
'''
current_parent = 3
current_child = 1
openSelCla()
'''

