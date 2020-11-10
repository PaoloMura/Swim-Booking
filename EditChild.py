#SQLite3 library is imported.
#The database containing all tables to be used is connected.
import sqlite3
from EditParent import EditParent
conn = sqlite3.connect('SwimSchool.db')
c = conn.cursor()



class EditChild(EditParent):
    def __init__(self, uifile):
        self.useless = "Remove this later"

    #The confirm procedure updates a chosen record in the Children table.
    #The details parameter is an array containing the inputted details from the
    #EditChild window.
    #The child parameter is the ChildID of the current child
    def confirm(self, details, child):
        #This validates the name
        if self.validateName(details[0]):
            #This ensures that the disability is no more than 150 characters
            if self.lengthCheck(details[3],None,150):
                #This appends ChildID of the current child to details
                details.append(child)
                #This modifies the record of the current child using details
                c.execute('''UPDATE Children
                            SET Name=?,
                            DateOfBirth=?,
                            Ability=?,
                            Disability=?
                            WHERE ChildID=?''', details)
                conn.commit()
            else:
                print('Please use up to 150 characters to describe disability')
        else:
            print('Invalid name')

'''
#childdetails is to take the inputs from the EditChild window here
#(Name, DoB, Ability, Disability)
childdetails = ["Robb", "03/04/11", "Advanced", "Chest pains"]
#currentchild is to be set as the ChildID of the current child
currentchild = 3
confirm(childdetails, currentchild)
'''
conn.close()

