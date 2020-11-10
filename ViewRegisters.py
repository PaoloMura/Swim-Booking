#View Registers Class
#SQLite3 library is imported.
#The database containing all tables to be used is connected.
import sqlite3
from ViewBookings import ViewBookings
conn = sqlite3.connect('SwimSchool.db')
c = conn.cursor()


class ViewRegisters(ViewBookings):
    def __init__(self, uifile):
        self.useless = "Remove this later"

    #The confirm procedure updates the Children table.
    #It takes in two parameters, the first is an array containing
    #attendance values obtained from the UI and the second is the classID
    def confirm(self, newattendance, week):
        for i in newattendance: #This iterates through each item in newattendance
            #This accesses the Attendance record for the child with ChildID = i
            c.execute('SELECT Attendance FROM Children WHERE ChildID=?', (i,))
            #These 2 lines convert it to the required format
            attendance = str(c.fetchone())
            attendance = attendance[2:len(attendance)-3]
            #This updates the value for this week in attendance
            attendance = attendance[0:week]+str(newattendance[i])+attendance[week+1:len(attendance)]
            details = [attendance, i]    #details contains the attendance and ChildID
            c.execute('''UPDATE Children
                                SET Attendance=?
                                WHERE ChildID=?''', details)
        conn.commit()

'''
#weekattendance is a dictionary containing the week's attendance values for each
#child (obtained from the radiobuttons in the UI) mapped to the ChildID. A value of 1 means present and
#a value of 0 means absent
weekattendance = {1:0,2:0,3:1}
#week is the current week i.e. 1 to 12 inclusive
currentweek = 7
#confirm calls the confirm method above
confirm(weekattendance, currentweek)
'''
conn.close()

