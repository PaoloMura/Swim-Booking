#SQLite3 library is imported.
#The database containing all tables to be used is connected.
import sqlite3
from Window import Window
conn = sqlite3.connect('SwimSchool.db')
c = conn.cursor()


class ViewClasses(Window):
    def __init__(self, uifile):
        self.useless = "Remove this later"

    #The validateSpaces() function takes spaces as a single parameter
    #and returns True for valid and False for invalid
    def validateSpaces(self, spaces):
        #This checks that spaces is an integer
        if self.isInt(spaces):
            if "." not in str(spaces):
                #This checks that spaces is a positive number
                if int(spaces) >= 0:
                    return True
        return False

    #The validateCost() function takes in a single cost parameter
    #and returns True for valid and False for invalid
    def validateCost(self, cost):
        #This checks whether cost is a number
        if self.isInt(cost):
            #This checks that cost is a positive number
            if cost >= 0:
                return True
        return False

    #The confirm procedure updates the Classes table.
    #Values that may be changed are: Venue, Day, Time, Level, Teacher, Spaces Available and Cost.
    #The parameter is a 2D array containing the details obtained from the UI
    def confirm(self, classes):
        #This iterates through each record
        for i in range(0, len(classes)):
            #This validates the cost
            if self.validateCost(classes[i][6]):
                #This validates the max spaces
                if self.validateSpaces(classes[i][4]):
                    #details = [Day, Time, ClassID]
                    if classes[i][0] == None:
                        details = [classes[i][2], classes[i][3], 0]
                    else:
                        details = [classes[i][2], classes[i][3], classes[i][0]]
                    #This accesses all teachers that are teaching on this day
                    #and time excluding that of the current class
                    c.execute('''SELECT TeacherID
                                    FROM Classes
                                    WHERE Day=?
                                    AND Time=?
                                    AND ClassID<>?''', details)
                    teachers = c.fetchall()
                    #This iterates through and formats teachers as a list
                    for j in range(0,len(teachers)):
                        teachers[j] = teachers[j][0]
                    #If the teacher for the current class is already teaching
                    #another class on this day and time, output message
                    if classes[i][8] in teachers:
                        print('This teacher is already teaching a class at this time', classes[i][0])
                    else:
                        #For a newly created class with no primary key set yet:
                        if classes[i][0] == None:
                            #This creates a new record
                            c.execute('''INSERT INTO Classes
                                            VALUES (?,?,?,?,?,?,?,?,?)''', classes[i])
                        #For an existing record to be updated:
                        else:
                            #These 2 lines reorder the details array for the update query 
                            currentclass = classes[i][1:len(classes[i])]
                            currentclass.append(classes[i][0])
                            #This updates an existing record
                            c.execute('''UPDATE Classes
                                        SET Level=?,
                                        Day=?,
                                        Time=?,
                                        MaxSize=?,
                                        Spaces=?,
                                        Cost=?,
                                        VenueID=?,
                                        TeacherID=?
                                        WHERE ClassID=?''', currentclass)
                    conn.commit()
                else:
                    print('Please ensure that spaces is a positive integer')
            else:
                print('Please ensure that cost is a positive decimal or integer')

'''
#newdetails is a 2D array containing the data obtained from the QTable widget
newdetails = [[1, "Beginner", "Wednesday", "16:00", 6, 1, 10, 1, 1],
              [2, "Intermediate", "Wednesday", "16:00", 6, 0, 12, 2, 1],
              [3, "Beginner", "Thursday", "16:00", 6, 6, 15, 1, 1],
              [4, "Beginner", "Wednesday", "17:00", 6, 6, 12, 1, 1],
              [None, "Beginner", "Wednesday", "16:00", 6, 6, 10, 1, 1],
              [None, "Beginner", "Friday", "17:00", 6, 6, 10, 1, 1]]
confirm(newdetails)
'''
conn.close()

