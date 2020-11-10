import sqlite3
from CreateAccount import CreateAccount
import sys, os
from PyQt4 import QtCore, QtGui, uic

from Login import Login

win = uic.loadUiType('SwimSchool.ui')[0]

class Main(QtGui.QMainWindow, win, Login):
    def __init__(self, parent=None):
        #This sets up the GUI
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #This sets the current window to Login
        self.NavigationStack.setCurrentIndex(0)
        #The following initialises key variables (popupchoice and currentuser) 
        self.popupchoice = "No"
        self.currentuser = None
        helpemail = self.getHelpEmail()
        self.lblLogHelpEmail.setText(helpemail)
        self.lblCreAccHelpEmail.setText(helpemail)
        #This displays the main window
        self.show()
        #The following connects button presses to method calls
        self.btnLogCreAcc.clicked.connect(self.logOpenCreAcc)
        self.btnLogLogIn.clicked.connect(self.logLogin)
        self.btnCreAccCreAcc.clicked.connect(self.creAccCreateAccount)
        self.btnCreAccBack.clicked.connect(self.creAccBack)

    #This procedure creates a pop up window
    def popUpWindow(self):
        #This creates a messagebox with text and two buttons (Yes and No)
        msg = QtGui.QMessageBox()
        msg.setText("Are you sure you want to leave this page?")
        msg.setStandardButtons(QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
        #If one of the buttons (Yes or No) is pressed, the choice method is called
        msg.buttonClicked.connect(self.choice)
        #This activates the messagebox
        msg.exec_()

    #This procedure updates the choice obtained from the pop up window
    def choice(self, i):
        self.popupchoice = i.text().replace("&","")

    #This procedure resets the Login window
    def clearLogin(self):
        self.lnLogUsername.clear()
        self.lnLogPassword.clear()
        self.lblLogErrorMessage.clear()

    #This procedure resets the Create Account window
    def clearCreAcc(self):
        self.lnCreAccUsername.clear()
        self.lnCreAccName.clear()
        self.lnCreAccSurname.clear()
        self.lnCreAccEmail.clear()
        self.lnCreAccPassword.clear()
        self.lblCreAccError.clear()

    #This procedure is called when the Create Account 
    # button is pressed on the Login window
    def logOpenCreAcc(self):
        #These two lines store the values held in the line edit widgets
        username = self.lnLogUsername.text()
        password = self.lnLogPassword.text()
        #This checks if text has been entered to the line edit widgets
        if (len(username) > 0) or (len(password) > 0):
            #If so, the pop up window is activated
            self.popUpWindow()
            #If Yes (confirm) is chosen...
            if self.popupchoice == "Yes":
                #The current window is set to be the Create Account window
                self.NavigationStack.setCurrentIndex(1)
                #The pop up window choice is reset
                self.popupchoice = "No"
                #This resets the Login window
                self.clearLogin()
        else:
            #The current window is set to be the Create Account window
            self.NavigationStack.setCurrentIndex(1)

    #This procedure is called when the Login button
    # is pressed on the Login window
    def logLogin(self):
        #These two lines store the values held in the line edit widgets
        username = self.lnLogUsername.text()
        password = self.lnLogPassword.text()
        #This checks that the line edit widgets are not blank
        if (len(username) > 0) and (len(password) > 0 ):
            #If they are not blank, login carries out validation on 
            # the username and password. login returns an array: 
            # [Accepted?, Details]
            result = self.login(username, password)
            #If the details are accepted (i.e. username found and 
            # password matches)...
            if result[0] == "Accepted":
                #If the Details contains the Admin ID (i.e. 0)...
                if result[1] == 0:
                    #The current user is set to the Admin ID
                    self.currentuser = 0
                    #The current window is set to be the Admin window
                    self.NavigationStack.setCurrentIndex(3)
                else:
                    #The current user is set to the Parent ID
                    self.currentuser = result[1]
                    #The current window is set to be the Home window
                    self.NavigationStack.setCurrentIndex(2)
                #This resets the Login window
                self.clearLogin()
            else:
                #If the details are rejected, result[1] contains the 
                # appropriate error message
                self.lblLogErrorMessage.setText(result[1])
        else:
            #If the line edit widgets are blank, the error message is updated
            self.lblLogErrorMessage.setText('Please fill in all details')

    #This procedure is called when the Create Account
    # button is pressed on the Create Account window
    def creAccCreateAccount(self):
        #The following store the values held in the line edit widgets
        username = self.lnCreAccUsername.text()
        name = self.lnCreAccName.text()
        surname = self.lnCreAccSurname.text()
        email = self.lnCreAccEmail.text()
        password = self.lnCreAccPassword.text()
        #This checks that the line edit widgets are not blank
        if (len(username) > 0) and (len(name) > 0) and (len(surname) > 0) and (len(email) > 0) and (len(password) > 0):
            #The Nonetype items in uidetails are: ParentID, Phone, Postcode respectively
            uidetails = [None, name, surname, username, password, email, None, None]
            #createAccount() carries out validation and creates an account if valid
            #result is an array containing [Accepted?, Details]
            result = self.createAccount(uidetails)
            #If the details are valid...
            if result[0] == "Accepted":
                #This resets the Create Account window
                self.clearCreAcc()
                #This sets Login as the current window
                self.NavigationStack.setCurrentIndex(0)
                #This outputs a confirmation message to the Login window
                self.lblLogErrorMessage.setText(result[1])
            else:
                #This outputs the appropriate error message to the Create Account window
                self.lblCreAccError.setText(result[1])
        else:
            #This outputs the following error message to the Create Account window
            self.lblCreAccError.setText('Please fill in all details')

    #This procedure is called when the Back button
    # is pressed on the Create Account window
    def creAccBack(self):
        #The following store the values held in the line edit widgets
        username = self.lnCreAccUsername.text()
        name = self.lnCreAccName.text()
        surname = self.lnCreAccSurname.text()
        email = self.lnCreAccEmail.text()
        password = self.lnCreAccPassword.text()
        #This checks if the line edit widgets are blank
        if (len(username) > 0) or (len(name) > 0) or (len(surname) > 0) or (len(email) > 0) or (len(password) > 0):
            #If so, the pop up window is activated
            self.popUpWindow()
            #If Yes (confirm) is chosen...
            if self.popupchoice == "Yes":
                #The current window is set to be the Login window
                self.NavigationStack.setCurrentIndex(0)
                #The pop up window choice is reset
                self.popupchoice = "No"
                #The Create Account window is reset
                self.clearCreAcc()
        else:
            #The current window is set to be the Login window
            self.NavigationStack.setCurrentIndex(0)
            #The Create Account window is reset
            self.clearCreAcc()


app = QtGui.QApplication(sys.argv)
l = Main(None)
app.exec_()

