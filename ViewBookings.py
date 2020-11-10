#View Bookings Class
#SQLite3 library is imported.
#The database containing all tables to be used is connected.
import sqlite3
from ViewClasses import ViewClasses
conn = sqlite3.connect('SwimSchool.db')
c = conn.cursor()


class ViewBookings(ViewClasses):
    def __init__(self, uifile):
        self.useless = "Remove this later"

    #The checkSpaces function takes in a single parameter, which is a ClassID
    #and returns whether this class has spaces (True) or not (False)
    def checkSpaces(self, currentclass):
        #This accesses the spaces in the class
        c.execute('SELECT Spaces FROM Classes WHERE ClassID=?', (currentclass,))
        spaces = c.fetchone()[0]
        if spaces > 0:
            return True
        else:
            return False

    #The confirm procedure updates the Bookings table.
    #It takes in a single parameter, which is an array containing
    #details obtained from the UI
    def confirm(self, currentbooking):
        #This iterates through each item in currentbooking
        for i in range(0,len(currentbooking)):
            #This accesses the Status and ClassID of the current booking
            c.execute('SELECT Status, ClassID FROM Bookings WHERE BookingID=?', (i+1,))
            retrieved = c.fetchone()
            priorstatus = retrieved[0]
            currentclass = retrieved[1]
            #This proceeds if the status has been changed
            if currentbooking[i] != priorstatus:
                #If the status is to be changed to confirmed but there are no spaces,
                #output message
                if currentbooking[i] == "Confirmed" and not self.checkSpaces(currentclass):
                    print('There are not enough spaces to confirm this booking')
                #This proceeds if the status is to be changed
                else:
                    #This array contains the Status value and the BookingID
                    details = [currentbooking[i],i+1]
                    #This updates the status for the current class in the bookings table
                    c.execute('''UPDATE Bookings
                                        SET Status=?
                                        WHERE BookingID=?''', details)
                    #If the status was changed to confirmed, decrement the Spaces for
                    #that class
                    if currentbooking[i] == "Confirmed":
                        c.execute('''UPDATE Classes
                                            SET Spaces=Spaces-1
                                            WHERE ClassID=?''', (currentclass,))
                    #If the status was changed from confirmed to either Pending or
                    #Cancelled, increment the Spaces for that class
                    elif priorstatus == "Confirmed":
                        c.execute('''UPDATE Classes
                                            SET Spaces=Spaces+1
                                            WHERE ClassID=?''', (currentclass,))
                    conn.commit()

'''
#newdetails is an array containing the Status values for each
#record, obtained from the QTable widget in the UI
newdetails = ["Confirmed","Confirmed","Cancelled"]
confirm(newdetails)
'''
conn.close()

