#SQLite3 library is imported.
#The database containing all tables to be used is connected.
import sqlite3, sys, os
from EditChild import EditChild
from PyQt4 import QtCore, QtGui

conn = sqlite3.connect('SwimSchool.db')
c = conn.cursor()
win = uic.loadUiType("AddChild.ui")[0]

class AddChild(QtGui.QMainWindow, win):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.details = []

    #The confirm procedure creates a new record in the Children table.
    #The details parameter is an array containing the inputted details from the
    #AddChild window as well as other obtained data
    def confirm(self, details, parent):
        #This validates the name
        if self.validateName(details[0]):
            #This ensures that disability is no more than 150 characters
            if self.lengthCheck(details[3]):
                #This formats the details to be passed to the SQL query
                self.details = [None, details[0], details[1], details[2], details[3], '"000000000000"', parent]
                #This creates a new record in Children using details
                c.execute('INSERT INTO Children VALUES (?,?,?,?,?,?,?)', details)
                conn.commit()
            else:
                print('Please use up to 150 characters for disability')
        else:
            print('Invalid name')

conn.close()


