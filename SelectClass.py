#SQLite3 library is imported.
#Date from the Datetime library is imported.
#The database containing all tables to be used is connected
import sqlite3
from datetime import date
from ViewClasses import ViewClasses
conn = sqlite3.connect('SwimSchool.db')
c = conn.cursor()


class SelectClass(ViewClasses):
    def __init__(self, uifile):
        self.useless = "Remove this later"

    #The bookClas procedure creates a new record in the Bookings table.
    #The selectedclass parameter is the ClassID of the chosen class 
    def bookClass(self, selectedclass):
        #curent_child is the ChildID of the current child
        global current_child
        #Today's date is accessed and put into the required format
        today = date.today().strftime("%d/%m/%y")
        #details is an array containing the required details:
        #[BookingID, Status, DateMade, ChildID, ClassID]
        details = [None, "Pending", today, current_child, selectedclass]
        #The details are used to create a new record in the Bookings table
        c.execute('INSERT INTO Bookings VALUES (?,?,?,?,?)',details)
        conn.commit()

    #The selectVenue function takes in a venueID
    #and returns the available classes at this venue.
    def selectVenue(self, venue):
        global current_child
        #This accesses the Ability of the current child
        c.execute('SELECT Ability FROM Children WHERE ChildID=?',(current_child,))
        ability = c.fetchone()[0]
        #details contains the parameters to be passed to the SQL Select query:
        #Ability of the current child and VenueID of the chosen venue
        details = [ability, venue]
        #This retrieves all available classes whose level matches the child's ability, with spaces
        #and whose venue matches the selected one
        c.execute('SELECT ClassID, Day, Time FROM Classes WHERE Level=? AND Spaces > 0 AND VenueID=?',details)
        accessed = c.fetchall()

        bookedtimes = []
        #This retrieves all classes that the current child is already booked onto
        c.execute('SELECT ClassID FROM Bookings WHERE ChildID=?',(current_child,))
        priorbookings = c.fetchall()
        #This iterates through each of the classes that the child is already booked onto
        for i in range(0,len(priorbookings)):
            #This accesses the day and time of the class and stores this in time
            c.execute('SELECT Day, Time FROM Classes WHERE ClassID=?',priorbookings[i])
            time = c.fetchone()
            #This time is appended to the list of booked times
            bookedtimes.append(time)

        classes = []
        classtimes = []
        #This iterates through each of the available classes
        for i in range(0,len(accessed)):
            #classes contains each ClassID
            classes.append(accessed[i][0])
            #classtimes contains the day and time of each class
            classtimes.append(accessed[i][1:])

        availableclasses = []
        #This iterates through each item in classes
        for i in range(0,len(classes)):
            #This checks whether the child is booked onto another class at this time
            if classtimes[i] not in bookedtimes:
                #If not, the ClassID is appended to the availableclasses
                availableclasses.append(classes[i])
        return availableclasses
            
'''
#Test data below. Change to obtain data from the UI
current_child = 1
aclass = 2
bookClass(aclass)

#Test data below. Change to obtain data from the UI
current_child = 1
selectedvenue = 1
selectVenue(selectedvenue)
'''

