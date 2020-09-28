
import sys
import os
from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import QPrinter
from PyQt4.QtCore import QThread
from PyQt4 import QtCore, QtGui, uic
import mysql.connector as mysql
from datetime import datetime


       
class Thread(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setDatabaseName("insurance")
        self.db.setUserName("root")
        self.db.setPassword("admin123")

        if (self.db.open()==False):     
            QMessageBox.critical(None, "Database Error",
		    self.db.lastError().text())   
		    
        self.query = QSqlQuery ("CREATE TABLE life_insurance (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")
        
        self.query = QSqlQuery ("CREATE TABLE travel_insurance (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")
        
        self.query = QSqlQuery ("CREATE TABLE home_insurance (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")
        
        self.query = QSqlQuery ("CREATE TABLE fire_insurance (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")
        
        self.query = QSqlQuery ("CREATE TABLE workmen_insurance (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")
        
        self.query = QSqlQuery ("CREATE TABLE health_insurance (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")
        
        self.query = QSqlQuery ("CREATE TABLE marine_insurance (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")

        self.query = QSqlQuery ("CREATE TABLE BikeInsurance (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")

        self.query = QSqlQuery ("CREATE TABLE Mediclaim (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")

        self.query = QSqlQuery ("CREATE TABLE Documents (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")

        self.query = QSqlQuery ("CREATE TABLE CarInsurance (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")

        self.query = QSqlQuery ("CREATE TABLE Events (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")

        self.query = QSqlQuery ("CREATE TABLE It_Return (Policy_No int ,First_Name varchar(255),Last_Name varchar(255),Start_Date varchar(255),End_Date varchar(255),Email_Id varchar(255) ,Age int,Phone_no int,PRIMARY KEY (Policy_No))")

        self.query = QSqlQuery ("CREATE TABLE admin (ID int NOT NULL AUTO_INCREMENT,User_Name varchar(255),Email varchar(255),Phone int,PRIMARY KEY (ID),User_id varchar(255),Password varchar(255))")

        


class Changerow(QtGui.QWidget):

    def open(self,window,a,b):
        self.dbase=a
        self.data=b
        self.setGeometry(50, 50, 500, 300)
        window.setWindowTitle("Change Value of Row")
        window.resize(500,320)
        window.closeEvent = self.closeEvent
        window.setWindowIcon(QtGui.QIcon('Images/myicon.png'))
        self.layout = QtGui.QGridLayout(window)
        self.Changecall()

    def closeEvent(self,event):
        choice= QtGui.QMessageBox.question(self,'Quit',
                                           "Do You Reallyt Want To Quit",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def Changecall(self):
        self.useridLabel = QtGui.QLabel("Enter Policy No")
        self.useridEdit = QtGui.QLineEdit(self)
        validator = QtGui.QIntValidator()
        self.useridEdit.setValidator(validator)
        self.changevalueLabel = QtGui.QLabel("     Change")
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("First_Name")
        self.comboBox.addItem("Last_Name")
        self.comboBox.addItem("Email_Id")
        self.comboBox.addItem("Age")
        self.comboBox.addItem("Start_Date")
        self.comboBox.addItem("End_Date")
        self.comboBox.addItem("Policy_No")
        self.changevalueEdit = QtGui.QLineEdit(self)
        self.comboBox.move(50, 250)
        self.changebtn = QtGui.QPushButton("Change Value")
        self.changebtn.clicked.connect(self.changevalue)
        self.layout.addWidget(self.useridLabel, 0, 1)
        self.layout.addWidget(self.useridEdit, 0, 2)
        self.layout.addWidget(self.changevalueLabel, 1, 1)
        self.layout.addWidget(self.comboBox, 1, 2)
        self.layout.addWidget(self.changevalueEdit, 1, 3)
        self.layout.addWidget(self.changebtn, 2, 2)

    def changevalue(self):
        if len(self.useridEdit.text()) > 0:
            if len(self.changevalueEdit.text()) > 0:
                choice= QtGui.QMessageBox.question(self,'Change Value',
                                           "Do You Reallyt Want To Change "+self.comboBox.currentText()+" to "+self.changevalueEdit.text()+" at Ploicy No "+self.useridEdit.text()+"",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                if choice == QtGui.QMessageBox.Yes:
                    conn=mysql.connect(user='root', password='admin123', host='127.0.0.1')
                    cursor=conn.cursor()
                    statement="use insurance"
                    cursor.execute(statement)
                    conn.commit()
                    self.sql="select * from "+self.data+" where Policy_No = "+self.useridEdit.text()+""
                    print(self.sql)
                    cursor.execute(self.sql)
                    #QSqlQuery(self.sql)
                    results=cursor.fetchall()
                    conn.commit()
                    if results != []:
                        sql="Update "+self.data+" set "+self.comboBox.currentText()+" = '"+self.changevalueEdit.text()+"' where Policy_No = "+self.useridEdit.text()+" "
                        cursor.execute(sql)
                        conn.commit()
                        conn.close()
                        QtGui.QMessageBox.warning(None,"Change Value"," Value of "+self.comboBox.currentText()+" at row "+self.useridEdit.text()+" changed successfully", "Done")
                        self.changevalueEdit.clear()
                        self.useridEdit.clear()
                    else:
                        QtGui.QMessageBox.warning(None,"Records"," Policy_No "+self.useridEdit.text()+" does not exist","OK")
                    
                else:
                    pass
                
            else:
                QtGui.QMessageBox.warning(None,"Empty Box","Change Value is Empty ", "Retry")
                self.changevalueEdit.setFocus()
            
        else:
            QtGui.QMessageBox.warning(None,"Empty Box","Policy No is Empty", "Retry")
            self.useridEdit.setFocus()
        
            
        

        
class Deleterow(QtGui.QWidget):

    def open(self,window,a,b):
        self.dbase=a
        self.data=b
        self.win=window
        self.setGeometry(50, 50, 500, 300)
        window.setWindowTitle("Delete Row")
        window.resize(500,320)
        window.closeEvent = self.closeEvent
        window.setWindowIcon(QtGui.QIcon('Images/myicon.png'))
        self.layout = QtGui.QGridLayout(window)
        self.InsertCall()

    def closeEvent(self,event):
        choice= QtGui.QMessageBox.question(self,'Quit',
                                           "Do You Reallyt Want To Quit",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def InsertCall(self):
        self.useridLabel = QtGui.QLabel("Enter Policy No")
        self.useridEdit = QtGui.QLineEdit(self)
        validator = QtGui.QIntValidator()
        self.useridEdit.setValidator(validator)
        self.deletebtn = QtGui.QPushButton("Delete Row")
        self.deletebtn.clicked.connect(self.delete)
        self.layout.addWidget(self.useridLabel, 0, 1)
        self.layout.addWidget(self.useridEdit, 0, 2)
        self.layout.addWidget(self.deletebtn, 2, 1)

    def delete(self):
        if len(self.useridEdit.text()) > 0:
            choice= QtGui.QMessageBox.question(self,'Delete Row',
                                           "Do You Really Want To Delete row "+self.useridEdit.text()+"",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                delid=self.useridEdit.text()
                conn=mysql.connect(user='root', password='admin123', host='127.0.0.1')
                cursor=conn.cursor()
                statement="use insurance"
                cursor.execute(statement)
                conn.commit()
                self.sql="select * from "+self.data+" where Policy_No = '"+delid+"'"
                print(self.sql)
                cursor.execute(self.sql)
                #QSqlQuery(self.sql)
                results=cursor.fetchall()
                conn.commit()
                if results != []:
                    self.sql="DELETE FROM "+self.data+" WHERE Policy_No ="+delid+""
                    cursor.execute(self.sql)
                    QtGui.QMessageBox.warning(None,"Delete Record","Record with Policy_No "+self.useridEdit.text()+" deleted successfully", "Done")
                    conn.commit()
                    conn.close()
                else:
                    QtGui.QMessageBox.warning(None,"Records"," Policy_No "+delid+" does not exist","OK")
            
            else:
                pass
        else:
            QtGui.QMessageBox.warning(None,"Empty Box","Policy No is Empty", "Retry")
        self.useridEdit.clear()


class Newwindow(QtGui.QWidget):
    
    def open(self,window,a,b):
        self.dbase=a
        self.data=b
        self.win11=window
        self.setGeometry(50, 50, 500, 300)
        window.setWindowTitle("Enter Data")
        window.resize(500,320)
        window.closeEvent = self.closeEvent
        window.setWindowIcon(QtGui.QIcon('Images/myicon.png'))
        self.layout = QtGui.QGridLayout(window)
        self.InsertCall()

    def closeEvent(self,event):
        choice= QtGui.QMessageBox.question(self,'Quit',
                                           "Do You Reallyt Want To Quit",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def InsertCall(self):
        self.firstnameLabel = QtGui.QLabel("First Name")
        self.firstnameEdit = QtGui.QLineEdit(self)
        self.reg_ex = QRegExp("[a-z-A-Z_]+")
        self.username_validator = QRegExpValidator(self.reg_ex, self.firstnameEdit)
        self.firstnameEdit.setValidator(self.username_validator)
        self.lastnameLabel = QtGui.QLabel("Last Name")
        self.lastnameEdit = QtGui.QLineEdit(self)
        self.username1_validator = QRegExpValidator(self.reg_ex, self.lastnameEdit)
        self.lastnameEdit.setValidator(self.username1_validator)
        self.ageLabel = QtGui.QLabel("Age")
        self.ageEdit = QtGui.QLineEdit(self)
        validator = QtGui.QIntValidator()
        self.ageEdit.setValidator(validator)
        self.startLabel = QtGui.QLabel("Start Date")
        self.comboBox1 = QtGui.QComboBox(self)
        self.comboBox1.addItem("1")
        self.comboBox1.addItem("2")
        self.comboBox1.addItem("3")
        self.comboBox1.addItem("4")
        self.comboBox1.addItem("5")
        self.comboBox1.addItem("6")
        self.comboBox1.addItem("7")
        self.comboBox1.addItem("8")
        self.comboBox1.addItem("9")
        self.comboBox1.addItem("10")
        self.comboBox1.addItem("11")
        self.comboBox1.addItem("12")

        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("2000")
        self.comboBox.addItem("2001")
        self.comboBox.addItem("2002")
        self.comboBox.addItem("2003")
        self.comboBox.addItem("2004")
        self.comboBox.addItem('2005')
        self.comboBox.addItem('2006')
        self.comboBox.addItem('2007')
        self.comboBox.addItem('2008')
        self.comboBox.addItem('2009')
        self.comboBox.addItem('2010')
        self.comboBox.addItem('2011')
        self.comboBox.addItem('2012')
        self.comboBox.addItem('2013')
        self.comboBox.addItem('2014')
        self.comboBox.addItem('2015')
        self.comboBox.addItem('2016')
        self.comboBox.addItem('2017')
        self.comboBox.addItem('2018')
        self.comboBox.addItem('2019')
        self.comboBox.addItem('2020')
        self.comboBox.addItem('2021')
        self.comboBox.addItem('2022')
        self.comboBox.addItem('2023')
        self.comboBox.addItem('2024')
        self.comboBox.addItem('2025')
        self.comboBox.addItem('2026')
        self.comboBox.addItem('2027')
        self.comboBox.addItem('2028')
        self.comboBox.addItem('2029')
        self.comboBox.addItem('2030')
        self.comboBox.addItem('2031')
        self.comboBox.addItem('2032')
        self.comboBox.addItem('2033')
        self.comboBox.addItem('2034')
        self.comboBox.addItem('2035')
        self.comboBox.addItem('2036')
        self.comboBox.addItem('2037')
        self.comboBox.addItem('2038')
        self.comboBox.addItem('2039')
        self.comboBox.addItem('2040')
        self.comboBox.addItem('2041')
        self.comboBox.addItem('2042')
        self.comboBox.addItem('2043')
        self.comboBox.addItem('2044')
        self.comboBox.addItem('2045')
        self.comboBox.addItem('2046')
        self.comboBox.addItem('2047')
        self.comboBox.addItem('2048')
        self.comboBox.addItem('2049')
        self.comboBox.addItem('2050')
        self.comboBox.addItem('2051')
        self.comboBox.addItem('2052')
        self.comboBox.addItem('2053')
        self.comboBox.addItem('2054')
        self.comboBox.addItem('2055')
        self.comboBox.addItem('2056')
        self.comboBox.addItem('2057')
        self.comboBox.addItem('2058')
        self.comboBox.addItem('2059')
        self.comboBox.addItem('2060')
        self.comboBox.addItem('2061')
        self.comboBox.addItem('2062')
        self.comboBox.addItem('2063')
        self.comboBox.addItem('2064')
        self.comboBox.addItem('2065')
        self.comboBox.addItem('2066')
        self.comboBox.addItem('2067')
        self.comboBox.addItem('2068')
        self.comboBox.addItem('2069')
        self.comboBox.addItem('2070')
        self.comboBox.addItem('2071')
        self.comboBox.addItem('2072')
        self.comboBox.addItem('2073')
        self.comboBox.addItem('2074')
        self.comboBox.addItem('2075')
        self.comboBox.addItem('2076')
        self.comboBox.addItem('2077')
        self.comboBox.addItem('2078')
        self.comboBox.addItem('2079')
        self.comboBox.addItem('2080')
        self.comboBox.addItem('2081')
        self.comboBox.addItem('2082')
        self.comboBox.addItem('2083')
        self.comboBox.addItem('2084')
        self.comboBox.addItem('2085')
        self.comboBox.addItem('2086')
        self.comboBox.addItem('2087')
        self.comboBox.addItem('2088')
        self.comboBox.addItem('2089')
        self.comboBox.addItem('2090')
        

        self.comboBox2 = QtGui.QComboBox(self)
        self.comboBox2.addItem('1')
        self.comboBox2.addItem('2')
        self.comboBox2.addItem('3')
        self.comboBox2.addItem('4')
        self.comboBox2.addItem('5')
        self.comboBox2.addItem('6')
        self.comboBox2.addItem('7')
        self.comboBox2.addItem('8')
        self.comboBox2.addItem('9')
        self.comboBox2.addItem('10')
        self.comboBox2.addItem('11')
        self.comboBox2.addItem('12')
        self.comboBox2.addItem('13')
        self.comboBox2.addItem('14')
        self.comboBox2.addItem('15')
        self.comboBox2.addItem('16')
        self.comboBox2.addItem('17')
        self.comboBox2.addItem('18')
        self.comboBox2.addItem('19')
        self.comboBox2.addItem('20')
        self.comboBox2.addItem('21')
        self.comboBox2.addItem('22')
        self.comboBox2.addItem('23')
        self.comboBox2.addItem('24')
        self.comboBox2.addItem('25')
        self.comboBox2.addItem('26')
        self.comboBox2.addItem('27')
        self.comboBox2.addItem('28')
        self.comboBox2.addItem('29')
        self.comboBox2.addItem('30')
        self.comboBox2.addItem('31')


        
        self.endLabel = QtGui.QLabel("End Date")
        
        self.comboBox11 = QtGui.QComboBox(self)
        self.comboBox11.addItem("1")
        self.comboBox11.addItem("2")
        self.comboBox11.addItem("3")
        self.comboBox11.addItem("4")
        self.comboBox11.addItem("5")
        self.comboBox11.addItem("6")
        self.comboBox11.addItem("7")
        self.comboBox11.addItem("8")
        self.comboBox11.addItem("9")
        self.comboBox11.addItem("10")
        self.comboBox11.addItem("11")
        self.comboBox11.addItem("12")

        self.comboBox22 = QtGui.QComboBox(self)
        self.comboBox22.addItem('1')
        self.comboBox22.addItem('2')
        self.comboBox22.addItem('3')
        self.comboBox22.addItem('4')
        self.comboBox22.addItem('5')
        self.comboBox22.addItem('6')
        self.comboBox22.addItem('7')
        self.comboBox22.addItem('8')
        self.comboBox22.addItem('9')
        self.comboBox22.addItem('10')
        self.comboBox22.addItem('11')
        self.comboBox22.addItem('12')
        self.comboBox22.addItem('13')
        self.comboBox22.addItem('14')
        self.comboBox22.addItem('15')
        self.comboBox22.addItem('16')
        self.comboBox22.addItem('17')
        self.comboBox22.addItem('18')
        self.comboBox22.addItem('19')
        self.comboBox22.addItem('20')
        self.comboBox22.addItem('21')
        self.comboBox22.addItem('22')
        self.comboBox22.addItem('23')
        self.comboBox22.addItem('24')
        self.comboBox22.addItem('25')
        self.comboBox22.addItem('26')
        self.comboBox22.addItem('27')
        self.comboBox22.addItem('28')
        self.comboBox22.addItem('29')
        self.comboBox22.addItem('30')
        self.comboBox22.addItem('31')

        self.comboBox33 = QtGui.QComboBox(self)
        self.comboBox33.addItem("2000")
        self.comboBox33.addItem("2001")
        self.comboBox33.addItem("2002")
        self.comboBox33.addItem("2003")
        self.comboBox33.addItem("2004")
        self.comboBox33.addItem('2005')
        self.comboBox33.addItem('2006')
        self.comboBox33.addItem('2007')
        self.comboBox33.addItem('2008')
        self.comboBox33.addItem('2009')
        self.comboBox33.addItem('2010')
        self.comboBox33.addItem('2011')
        self.comboBox33.addItem('2012')
        self.comboBox33.addItem('2013')
        self.comboBox33.addItem('2014')
        self.comboBox33.addItem('2015')
        self.comboBox33.addItem('2016')
        self.comboBox33.addItem('2017')
        self.comboBox33.addItem('2018')
        self.comboBox33.addItem('2019')
        self.comboBox33.addItem('2020')
        self.comboBox33.addItem('2021')
        self.comboBox33.addItem('2022')
        self.comboBox33.addItem('2023')
        self.comboBox33.addItem('2024')
        self.comboBox33.addItem('2025')
        self.comboBox33.addItem('2026')
        self.comboBox33.addItem('2027')
        self.comboBox33.addItem('2028')
        self.comboBox33.addItem('2029')
        self.comboBox33.addItem('2030')
        self.comboBox33.addItem('2031')
        self.comboBox33.addItem('2032')
        self.comboBox33.addItem('2033')
        self.comboBox33.addItem('2034')
        self.comboBox33.addItem('2035')
        self.comboBox33.addItem('2036')
        self.comboBox33.addItem('2037')
        self.comboBox33.addItem('2038')
        self.comboBox33.addItem('2039')
        self.comboBox33.addItem('2040')
        self.comboBox33.addItem('2041')
        self.comboBox33.addItem('2042')
        self.comboBox33.addItem('2043')
        self.comboBox33.addItem('2044')
        self.comboBox33.addItem('2045')
        self.comboBox33.addItem('2046')
        self.comboBox33.addItem('2047')
        self.comboBox33.addItem('2048')
        self.comboBox33.addItem('2049')
        self.comboBox33.addItem('2050')
        self.comboBox33.addItem('2051')
        self.comboBox33.addItem('2052')
        self.comboBox33.addItem('2053')
        self.comboBox33.addItem('2054')
        self.comboBox33.addItem('2055')
        self.comboBox33.addItem('2056')
        self.comboBox33.addItem('2057')
        self.comboBox33.addItem('2058')
        self.comboBox33.addItem('2059')
        self.comboBox33.addItem('2060')
        self.comboBox33.addItem('2061')
        self.comboBox33.addItem('2062')
        self.comboBox33.addItem('2063')
        self.comboBox33.addItem('2064')
        self.comboBox33.addItem('2065')
        self.comboBox33.addItem('2066')
        self.comboBox33.addItem('2067')
        self.comboBox33.addItem('2068')
        self.comboBox33.addItem('2069')
        self.comboBox33.addItem('2070')
        self.comboBox33.addItem('2071')
        self.comboBox33.addItem('2072')
        self.comboBox33.addItem('2073')
        self.comboBox33.addItem('2074')
        self.comboBox33.addItem('2075')
        self.comboBox33.addItem('2076')
        self.comboBox33.addItem('2077')
        self.comboBox33.addItem('2078')
        self.comboBox33.addItem('2079')
        self.comboBox33.addItem('2080')
        self.comboBox33.addItem('2081')
        self.comboBox33.addItem('2082')
        self.comboBox33.addItem('2083')
        self.comboBox33.addItem('2084')
        self.comboBox33.addItem('2085')
        self.comboBox33.addItem('2086')
        self.comboBox33.addItem('2087')
        self.comboBox33.addItem('2088')
        self.comboBox33.addItem('2089')
        self.comboBox33.addItem('2090')

        self.comboBox44 = QtGui.QComboBox(self)
        self.comboBox44.addItem("0")
        self.comboBox44.addItem("1")
        self.comboBox44.addItem("3")
        self.comboBox44.addItem("6")
        self.comboBox44.addItem("12")
        self.policyLabel = QtGui.QLabel("Policy Number")
        self.policyEdit = QtGui.QLineEdit(self)
        self.policyEdit.setValidator(validator)
        self.dateLabel = QtGui.QLabel("Date")
        self.monthLabel = QtGui.QLabel("Month")
        self.yearLabel = QtGui.QLabel("Year")
        self.date1Label = QtGui.QLabel("Date")
        self.month1Label = QtGui.QLabel("Month")
        self.year1Label = QtGui.QLabel("Year")
        self.emailLabel = QtGui.QLabel("Email Id")
        #self.FileLabel = QtGui.QLabel("Image")
        self.phoneLabel = QtGui.QLabel("Phone Number")
        #self.FileEdit = QtGui.QLineEdit(self)
        #self.Filebtn = QtGui.QPushButton("Browse...")
        #self.Filebtn.clicked.connect(self.selectFile)
        self.emailEdit = QtGui.QLineEdit(self)
        self.phoneEdit = QtGui.QLineEdit(self)
        self.phoneEdit.setValidator(validator)
        self.submitbtn = QtGui.QPushButton("Insert")
        self.submitbtn.clicked.connect(self.validate)
        
        self.layout.addWidget(self.firstnameLabel, 0, 3)
        self.layout.addWidget(self.firstnameEdit, 0, 4)
        self.layout.addWidget(self.lastnameLabel, 1, 3)
        self.layout.addWidget(self.lastnameEdit, 1, 4)
        self.layout.addWidget(self.ageLabel, 2, 3)
        self.layout.addWidget(self.ageEdit, 2, 4)
        self.layout.addWidget(self.dateLabel, 3, 4)
        self.layout.addWidget(self.monthLabel, 3, 5)
        self.layout.addWidget(self.yearLabel, 3, 6)
        self.layout.addWidget(self.startLabel, 4, 3)
        self.layout.addWidget(self.comboBox2, 4, 4)
        self.layout.addWidget(self.comboBox1,4,5)
        self.layout.addWidget(self.comboBox, 4, 6)
        self.layout.addWidget(self.date1Label, 5, 4)
        self.layout.addWidget(self.month1Label, 5, 5)
        self.layout.addWidget(self.year1Label, 5, 6)
        self.layout.addWidget(self.endLabel, 6, 3)
        self.layout.addWidget(self.comboBox22, 6, 4)
        self.layout.addWidget(self.comboBox11, 6, 5)
        self.layout.addWidget(self.comboBox33, 6, 6)
        self.layout.addWidget(self.emailLabel, 7, 3)
        self.layout.addWidget(self.emailEdit, 7, 4)
        self.layout.addWidget(self.phoneLabel, 8, 3)
        self.layout.addWidget(self.phoneEdit, 8, 4)
        self.layout.addWidget(self.policyLabel, 10,3)
        self.layout.addWidget(self.policyEdit, 10, 4)
        #self.layout.addWidget(self.FileLabel, 11,3)
        #self.layout.addWidget(self.FileEdit, 11,4)
        #self.layout.addWidget(self.Filebtn, 11,5)
        self.layout.addWidget(self.submitbtn, 12, 5)

    def selectFile(self):
        self.FileEdit.setText(QFileDialog.getOpenFileName())


    def validate(self):
        x=1
        for i in range(x):
            if len(self.firstnameEdit.text()) > 0:
                    pass
            else:
                self.firstnameEdit.setFocus()
                QtGui.QMessageBox.warning(None,"Add Row","First Name Feild Is Empty", "Retry")
                break

            if len(self.lastnameEdit.text()) > 0:
                pass
            else:
                self.lastnameEdit.setFocus()
                QtGui.QMessageBox.warning(None,"Add Row","Last Name Feild Is Empty", "Retry")
                break
            
            if len(self.ageEdit.text()) > 0:
                pass
            else:
                self.ageEdit.setFocus()
                QtGui.QMessageBox.warning(None,"Add Row","Age Feild Is Empty", "Retry")
                break      


            if len(self.emailEdit.text()) > 0:
                
                pass

            else:
                self.emailEdit.setFocus()
                QtGui.QMessageBox.warning(None,"Add Row","Email Id Feild Is Empty", "Retry")
                break

            if len(self.phoneEdit.text()) > 0:
                pass
            else:
                self.phoneEdit.setFocus()
                QtGui.QMessageBox.warning(None,"Add Row","Phone Number Feild Is Empty", "Retry")
                break
            if len(self.policyEdit.text()) > 0:
                self.insertCall()
                self.firstnameEdit.clear()
                self.lastnameEdit.clear()
                self.ageEdit.clear()
                self.emailEdit.clear()      
                self.phoneEdit.clear()
                self.policyEdit.clear()
                self.firstnameEdit.setFocus()
                QtGui.QMessageBox.warning(None,"Add Row","Insert Successful", "Done")
            else:
                self.phoneEdit.setFocus()
                QtGui.QMessageBox.warning(None,"Add Row","Policy Number Feild Is Empty", "Retry")
                break

   
            
    def encrypt(key, msg):
        encryped = []
        for i, x in enumerate(msg):
            key_c = ord(key[i % len(key)])
            msg_c = ord(x)
            encryped.append(chr((msg_c + key_c) % 512))
        code= ''.join(encryped)
        return code
        


    def insertCall(self):
        x=self.firstnameEdit.text()
        y=self.lastnameEdit.text()
        sdate=self.comboBox2.currentText()
        smonth=self.comboBox1.currentText()
        syear=self.comboBox.currentText()
        z=""+syear+"/"+smonth+"/"+sdate+""
        edate=self.comboBox22.currentText()
        emonth=self.comboBox11.currentText()
        eyear=self.comboBox33.currentText()
        a=""+edate+"/"+emonth+"/"+eyear+""
        b=self.emailEdit.text()
        d=self.phoneEdit.text()
        c=self.ageEdit.text()
        policy=self.policyEdit.text()
        """x=self.encrypt("omg",self.firstnameEdit.text())
        y=self.encrypt("omfg",self.lastnameEdit.text())
        z=self.encrypt("omg",name)
        a=self.encrypt("omfg",age)
        b=self.encrypt("omg",name)
        c=self.encrypt("omfg",age)
        d=self.encrypt("omfg",age)"""
        conn=mysql.connect(user='root', password='admin123', host='127.0.0.1')
        cursor=conn.cursor()
        statement="use "+self.dbase+""
        cursor.execute(statement)
        sql="INSERT INTO "+self.data+" VALUES('"+policy+"','"+x+"','"+y+"','"+z+"','"+a+"','"+b+"','"+c+"','"+d+"')"
        print(sql)
        cursor.execute(sql)
        conn.commit()
    
class Change(QtGui.QWidget):
    def start(self,window,option):
        self.option=option
        window.setWindowTitle("Change Account Details")
        window.setWindowIcon(QtGui.QIcon('Images/myicon.png'))
        self.layout = QtGui.QGridLayout(window)
        window.closeEvent = self.closeEvent
        self.login()
        
    def clear(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()

    def login(self):
        self.clear()
        self.label11 = QtGui.QLabel("Login Again For Changing Details")
        self.label11.setStyleSheet("color:red")
        self.layout.addWidget(self.label11, 0, 3)
        self.reg_ex = QRegExp("[a-z-A-Z_]+")
        self.username = QtGui.QLabel("User id:")
        self.usernameEdit = QtGui.QLineEdit(self)
        self.passwordcheck = QtGui.QLabel("Password:")
        self.passwordcheckEdit = QtGui.QLineEdit(self)
        self.passwordcheckEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.loginbtn = QtGui.QPushButton("Login")
        self.loginbtn.clicked.connect(self.loginVerification)
        self.layout.addWidget(self.username, 2, 3)
        self.layout.addWidget(self.usernameEdit, 2, 4)
        self.layout.addWidget(self.passwordcheck, 4, 3)
        self.layout.addWidget(self.passwordcheckEdit, 4, 4)
        self.layout.addWidget(self.loginbtn, 6, 3)

    def loginVerification(self):
        pword = str(self.passwordcheckEdit.text())
        name = str(self.usernameEdit.text())
        conn=mysql.connect(user='root', password='admin123', host='127.0.0.1')
        cursor=conn.cursor()
        cursor.execute("use insurance")
        sql="SELECT * FROM admin "
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            self.uid=row[0]
            self.uname=row[1]
            self.emailid=row[2]
            self.number=row[3]
            self.useridd=row[4]
            self.upass=row[5]
        conn.commit()
        conn.close()
        if len(name) > 0:
            if len(pword) > 0:
                if name == self.useridd and pword == self.upass:
                    QtGui.QMessageBox.warning(None,"Login","Login successful", "Done")
                    if self.option == 1:
                        self.changeName()
                    elif self.option == 2:
                        self.changeUserid()
                    elif self.option == 3:
                        self.changeEmail()
                    elif self.option == 4:
                        self.changePhone()
                    else:
                        self.changePassword()
                    
                else:
                    self.passwordcheckEdit.clear()
                    self.passwordcheckEdit.setFocus()
                    self.usernameEdit.clear()
                    self.usernameEdit.setFocus()
                    QtGui.QMessageBox.warning(None,"Login","Login details didnt Match", "Failed")
                    pass
            else:
                self.passwordcheckEdit.setFocus()
                QtGui.QMessageBox.warning(None,"Login","Password Field Is Empty", "Retry")
        else:
            self.usernameEdit.setFocus()
            QtGui.QMessageBox.warning(None,"Login","User Id is Field Empty", "Retry")

    def closeEvent(self,event):
        self.cp = QtGui.QDesktopWidget().availableGeometry().center()
        choice= QtGui.QMessageBox.question(self,'Quit',
                                           "Do You Reallyt Want To Quit",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            event.accept()
            
        else:
            event.ignore()
            

    def changeName(self):
        self.clear()
        self.oldusername = QtGui.QLabel("Old Name:")
        self.oldusernameEdit = QtGui.QLabel(self.uname)
        self.username = QtGui.QLabel("New Name:")
        self.usernameEdit = QtGui.QLineEdit(self)
        self.btn2 = QtGui.QPushButton("Change")
        self.layout.addWidget(self.btn2, 4, 5)
        self.layout.addWidget(self.oldusername, 2, 4)
        self.layout.addWidget(self.oldusernameEdit, 2, 5)
        self.layout.addWidget(self.username, 3, 4)
        self.layout.addWidget(self.usernameEdit, 3, 5)
        self.btn2.clicked.connect(self.changeEvent)
    def changeUserid(self):
        self.clear()
        self.olduserid = QtGui.QLabel("Old User Id:")
        self.olduseridEdit = QtGui.QLabel(self.useridd)
        self.userid = QtGui.QLabel("New User Id:")
        self.useridEdit = QtGui.QLineEdit(self)
        self.btn2 = QtGui.QPushButton("Change")
        self.layout.addWidget(self.btn2, 4, 5)
        self.layout.addWidget(self.olduserid, 2, 4)
        self.layout.addWidget(self.olduseridEdit, 2, 5)
        self.layout.addWidget(self.userid, 3, 4)
        self.layout.addWidget(self.useridEdit, 3, 5)
        self.btn2.clicked.connect(self.changeEvent)
    def changeEmail(self):
        self.clear()
        self.username1 = QtGui.QLabel("Old Email:")
        self.username1Edit = QtGui.QLabel(self.emailid)
        self.username2 = QtGui.QLabel("New Email:")
        self.username2Edit = QtGui.QLineEdit(self)
        self.btn2 = QtGui.QPushButton("Change")
        self.layout.addWidget(self.btn2, 4, 5)
        self.layout.addWidget(self.username1, 2, 4)
        self.layout.addWidget(self.username1Edit, 2, 5)
        self.layout.addWidget(self.username2, 3, 4)
        self.layout.addWidget(self.username2Edit, 3, 5)
        self.btn2.clicked.connect(self.changeEvent)
    def changePhone(self):
        self.clear()
        self.username1 = QtGui.QLabel("Old Phone No:")
        self.username1Edit = QtGui.QLabel(self.number)
        self.username2 = QtGui.QLabel("New Phone No:")
        self.username2Edit = QtGui.QLineEdit(self)
        self.btn2 = QtGui.QPushButton("Change")
        self.layout.addWidget(self.btn2, 4, 5)
        self.layout.addWidget(self.username1, 2, 4)
        self.layout.addWidget(self.username1Edit, 2, 5)
        self.layout.addWidget(self.username2, 3, 4)
        self.layout.addWidget(self.username2Edit, 3, 5)
        self.btn2.clicked.connect(self.changeEvent)
    def changePassword(self):
        self.clear()
        self.username1 = QtGui.QLabel("Old Password:")
        self.username1Edit = QtGui.QLabel(self.upass)
        self.username2 = QtGui.QLabel("New Password:")
        self.username2Edit = QtGui.QLineEdit(self)
        self.btn2 = QtGui.QPushButton("Change")
        self.layout.addWidget(self.btn2, 4, 5)
        self.layout.addWidget(self.username1, 2, 4)
        self.layout.addWidget(self.username1Edit, 2, 5)
        self.layout.addWidget(self.username2, 3, 4)
        self.layout.addWidget(self.username2Edit, 3, 5)
        self.btn2.clicked.connect(self.changeEvent)

    def changeEvent(self):
        conn=mysql.connect(user='root', password='admin123', host='127.0.0.1')
        cursor=conn.cursor()
        cursor.execute("use insurance")
        
        if self.option == 1:
            a=str(self.usernameEdit.text())
            choice = QtGui.QMessageBox.question(self,'Quit',
                                           "Sure You Want To Change Your Name To"+a+"",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                sql="update admin set User_name ='"+a+"' Where id = 1"
                cursor.execute(sql)
                conn.commit()
                conn.close()
                QtGui.QMessageBox.warning(None,"Change Details","Name Changed Successful", "Done")
            else:
                pass
            
        elif self.option == 2:
            a=str(self.useridEdit.text())
            choice = QtGui.QMessageBox.question(self,'Quit',
                                           "Sure You Want To Change Your User Id To"+a+"",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                
                sql="update admin set Policy_No ='"+a+"' Where id = 1"
                cursor.execute(sql)
                conn.commit()
                conn.close()
                QtGui.QMessageBox.warning(None,"Change Details","User Id Changed Successful", "Done")

            else:
                pass
            
        elif self.option == 3:
            a=str(self.username2Edit.text())
            choice = QtGui.QMessageBox.question(self,'Quit',
                                           "Sure You Want To Change Your Email To"+a+"",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                
                sql="update admin set Email ='"+a+"' Where id = 1"
                cursor.execute(sql)
                conn.commit()
                conn.close()
                QtGui.QMessageBox.warning(None,"Change Details","Email Id Changed Successful", "Done")
                
            else:
                pass
            
        elif self.option == 4:
            a=str(self.username2Edit.text())
            choice = QtGui.QMessageBox.question(self,'Quit',
                                           "Sure You Want To Change Your Phone To"+a+"",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                
                sql="update admin set Phone ="+a+" Where id = 1"
                cursor.execute(sql)
                conn.commit()
                conn.close()
                QtGui.QMessageBox.warning(None,"Change Details","Phone No Changed Successful", "Done")

            else:
                pass
            
        else:
            a=str(self.username2Edit.text())
            choice = QtGui.QMessageBox.question(self,'Quit',
                                           "Sure You Want To Change Your Password To"+a+"",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                
                sql="update admin set Password ='"+a+"' Where id = 1"
                cursor.execute(sql)
                conn.commit()
                conn.close()
                QtGui.QMessageBox.warning(None,"Change Details","Password Changed Successful", "Done")
                
            else:
                pass
            
        
class Window(QtGui.QWidget):

    def printViewCustomer(self):
        printer=QtGui.QPrinter()
        dialog=QtGui.QPrintDialog(printer,self)
        if (dialog.exec_()!=QtGui.QDialog.Accepted):
            return
        printWidget=win
        painter=QtGui.QPainter(printer)
        painter.begin(printer)
        print(printer.paperRect().x())
        XScale=(printer.pageRect().width()/ (printWidget.width()))
        YScale=(printer.pageRect().height()/(printWidget.height()))
        Scale=(min(XScale,YScale))
        painter.translate((printer.paperRect().x()) + (printer.pageRect().width()/2), (printer.paperRect().y()) + (printer.pageRect().height()/2))
        painter.scale(Scale,Scale)
        painter.translate(-1*printWidget.width()/2,-1*printWidget.height()/2)
        printWidget.render(painter)
        painter.end()
        
    def begin(self):
        self.setGeometry(50, 50, 500, 300)
        win.setWindowTitle("Data Boom")
        win.resize(500,320)
        win.setWindowIcon(QtGui.QIcon('Images/myicon.png'))
        self.layout = QtGui.QGridLayout(win)
        win.closeEvent = self.closeEvent
        self.start()
        
    def changewindow(self):
        self.window5 = QtGui.QWidget()
        self.new = Change()
        self.new.start(self.window5,self.option)
        self.window5.show()
        
    def openWindow(self):
        self.window1 = QtGui.QWidget()
        self.ui = Newwindow()
        self.ui.open(self.window1,self.dbase,self.data)
        self.window1.show()

    def deleteWindow(self):
        self.window2 = QtGui.QWidget()
        self.ui1 = Deleterow()
        self.ui1.open(self.window2,self.dbase,self.data)
        self.window2.show()

    def changeWindow(self):
        self.window3 = QtGui.QWidget()
        self.ui2 = Changerow()
        self.ui2.open(self.window3,self.dbase,self.data)
        self.window3.show()

 
    def closeEvent(self,event):
        self.cp = QtGui.QDesktopWidget().availableGeometry().center()
        choice= QtGui.QMessageBox.question(self,'Quit',
                                           "Do You Reallyt Want To Quit",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            event.accept()
            
        else:
            event.ignore()
            
    def close(self):
        self.cp = QtGui.QDesktopWidget().availableGeometry().center()
        choice= QtGui.QMessageBox.question(self,'Quit',
                                           "Do You Reallyt Want To Quit",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit(app.exec_())
            
        else:
            pass
    
    
    def decrypt(self,key, encryped):
        msg = []
        for i, x in enumerate(encryped):
            key_c = ord(key[i % len(key)])
            enc_c = ord(x)
            msg.append(chr((enc_c - key_c) % 512))
        z= ''.join(msg)
        return z

    
    def start(self):
        self.clear()
        win.showNormal()
        self.btn1 = QtGui.QPushButton("Create User")
        self.btn1.setIcon(QtGui.QIcon('Images/createuser.png'))
        self.btn2 = QtGui.QPushButton("Login")
        self.btn2.setIcon(QtGui.QIcon('Images/login.png'))
        self.layout.addWidget(self.btn1, 4, 5)
        self.layout.addWidget(self.btn2, 6, 5)
        self.btn1.clicked.connect(self.createuser)
        self.btn2.clicked.connect(self.login)
        self.label11 = QtGui.QLabel("Select This For Creating a New User ↓")
        self.label11.setStyleSheet("color:red")
        self.label12 = QtGui.QLabel("Select This For Login ↓")
        self.label12.setStyleSheet("color:red")
        self.layout.addWidget(self.label11, 3, 5)
        self.layout.addWidget(self.label12, 5, 5)
        

    def center (self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        win.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

    def login(self):
        self.clear()
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.start)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)
        self.toolButton = QToolButton(self)
        self.label11 = QtGui.QLabel("Login here")
        self.label11.setStyleSheet("color:red")
        
        

        self.reg_ex = QRegExp("[a-z-A-Z_]+")
        self.username = QtGui.QLabel("Enter User id:")
        self.usernameEdit = QtGui.QLineEdit(self)
        self.passwordcheck = QtGui.QLabel("Enter Password:")
        self.passwordcheckEdit = QtGui.QLineEdit(self)
        self.passwordcheckEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.loginbtn = QtGui.QPushButton("Login")
        self.loginbtn.clicked.connect(self.loginVerification)
        self.layout.addWidget(self.label11, 1, 3)
        self.layout.addWidget(self.username, 2, 3)
        self.layout.addWidget(self.usernameEdit, 3, 3)
        self.layout.addWidget(self.passwordcheck, 4, 3)
        self.layout.addWidget(self.passwordcheckEdit, 5, 3)
        self.layout.addWidget(self.loginbtn, 6, 3)

    def size(self):
        win.resize(500,320)

    def account(self):
        self.clear()
        self.option=9
        win.showNormal()
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.home)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)
        self.btnacc = QtGui.QPushButton("Alerts")
        self.btnacc.setIcon(QtGui.QIcon('Images/alert.png'))
        self.btnacc.setStyleSheet("color:red")
        self.btnacc.clicked.connect(self.alerts)
        self.layout.addWidget(self.btnacc, 0, 4)
        conn=mysql.connect(user='root', password='admin123', host='127.0.0.1')
        cursor=conn.cursor()
        cursor.execute("use insurance")
        sql="SELECT * FROM admin "
        cursor.execute(sql)
        results=cursor.fetchall()
        conn.commit()
        conn.close()
        for row in results:
            Userid=row[4]
            name= row[1]
            phone = row[3]
            emailid = row[2]
            password = "********"
        
        self.usernameLabel1 = QtGui.QLabel("Hello")
        self.usernameLabel2 = QtGui.QLabel(name)
        self.usernameLabel111 = QtGui.QLabel("User-Id")
        self.usernameLabel222 = QtGui.QLabel(str(Userid))
        self.usernameLabel3 = QtGui.QLabel("Phone number")
        self.usernameLabel4 = QtGui.QLabel(str(phone))
        self.usernameLabel5 = QtGui.QLabel("Email")
        self.usernameLabel6 = QtGui.QLabel(emailid)
        self.usernameLabel7 = QtGui.QLabel("password")
        self.usernameLabel8 = QtGui.QLabel(password)
        self.usernameLabel9 = QtGui.QLabel("Change password")
        self.usernameLabel0 = QtGui.QLabel(password)
        self.usernameLabel122 = QtGui.QPushButton("change")
        self.usernameLabel11 = QtGui.QPushButton("change")
        
        self.usernameLabel12 = QtGui.QPushButton("change")
        self.usernameLabel13 = QtGui.QPushButton("change")
        self.usernameLabel14 = QtGui.QPushButton("change")
        self.usernameLabel11.setStyleSheet("QPushButton{color: blue}")
        self.usernameLabel12.setStyleSheet("color: blue")
        self.usernameLabel13.setStyleSheet("color: blue")
        self.usernameLabel14.setStyleSheet("color: blue")
        self.usernameLabel122.setStyleSheet("color: blue")
        self.usernameLabel11.clicked.connect(self.changename)
        self.usernameLabel122.clicked.connect(self.changeuserid)
        self.usernameLabel12.clicked.connect(self.changephone)
        self.usernameLabel13.clicked.connect(self.changeemail)
        self.usernameLabel14.clicked.connect(self.changepassword)
        self.layout.addWidget(self.usernameLabel1, 1, 1)
        self.layout.addWidget(self.usernameLabel2, 1, 2)
        self.layout.addWidget(self.usernameLabel111, 2, 1)
        self.layout.addWidget(self.usernameLabel222, 2, 2)
        self.layout.addWidget(self.usernameLabel122, 2, 3)
        self.layout.addWidget(self.usernameLabel3, 3, 1)
        self.layout.addWidget(self.usernameLabel4, 3, 2)
        self.layout.addWidget(self.usernameLabel5, 4, 1)
        self.layout.addWidget(self.usernameLabel6, 4, 2)
        self.layout.addWidget(self.usernameLabel7, 5, 1)
        self.layout.addWidget(self.usernameLabel8, 5, 2)
        self.layout.addWidget(self.usernameLabel9, 6, 1)
        self.layout.addWidget(self.usernameLabel0, 6, 2)
        self.layout.addWidget(self.usernameLabel11, 1, 3)
        self.layout.addWidget(self.usernameLabel12, 3, 3)
        self.layout.addWidget(self.usernameLabel13, 4, 3)
        self.layout.addWidget(self.usernameLabel14, 5, 3)


    def changename(self):
        self.option = 1
        self.changewindow()
    def changeuserid(self):
        self.option = 2
        self.changewindow()
    def changephone(self):
        self.option = 4
        self.changewindow()
    def changeemail(self):
        self.option = 3
        self.changewindow()
    def changepassword(self):
        self.option = 5
        self.changewindow()
        
    def loginVerification(self):
        pword = str(self.passwordcheckEdit.text())
        name = str(self.usernameEdit.text())
        conn=mysql.connect(user='root', password='admin123', host='127.0.0.1')
        cursor=conn.cursor()
        cursor.execute("use insurance")
        sql="SELECT * FROM admin "
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            self.uid=row[0]
            self.uname=row[1]
            self.emailid=row[2]
            self.number=row[3]
            self.useridd=row[4]
            self.upass=row[5]
        conn.commit()
        conn.close()
        if len(name) > 0:
            if len(pword) > 0:
                if name == self.useridd and pword == self.upass:
                    QtGui.QMessageBox.warning(None,"Login","Login successful", "Done")
                    self.home()
                else:
                    self.passwordcheckEdit.clear()
                    self.passwordcheckEdit.setFocus()
                    self.usernameEdit.clear()
                    self.usernameEdit.setFocus()
                    QtGui.QMessageBox.warning(None,"Login","Login details didnt Match", "Failed")
                    pass
            else:
                self.passwordcheckEdit.setFocus()
                QtGui.QMessageBox.warning(None,"Login","Password Field Is Empty", "Retry")
        else:
            self.usernameEdit.setFocus()
            QtGui.QMessageBox.warning(None,"Login","User Id is Field Empty", "Retry")
    
            
    def alerts(self):
        day = datetime.now().day
        Month = datetime.now().month
        Year = datetime.now().year
        print(Year,Month,day)
        month1=Month+1
        sql = "select * from life_insurance where end_date between "+str(day)+"/"+str(Month)+"/"+str(Year)+" and "+str(day)+"/"+str(month1)+"/"+str(Year)+""
        self.TableView1()

    def TableView1(self):
        self.clear()
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.account)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)
        self.toolButton = QToolButton(self)
        self.label11 = QtGui.QLabel("Alets of ending premium of this month")
        self.label11.setStyleSheet("color:red")
        self.layout.addWidget(self.label11, 1, 0)
        self.dbase="insurance"
        self.data="life_insurance"
        
        self.sortbyLabel = QtGui.QLabel("Sort By")
        
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("First_Name")
        self.comboBox.addItem("Last_Name")
        self.comboBox.addItem("Email_Id")
        self.comboBox.addItem("Age")
        self.comboBox.addItem("Start_Date")
        self.comboBox.addItem("End_Date")
        self.comboBox.move(50, 250)
        self.comboBox.activated[str].connect(self.clicked)
        
        self.table = QTableWidget(self)
        self.table.setFixedSize(1100,500)
        self.db 	= QSqlDatabase.addDatabase("QMYSQL")

        self.db.setHostName("localhost")
        self.db.setDatabaseName("insurance")
        self.db.setUserName("root")
        self.db.setPassword("admin123")

        if (self.db.open()==False):     
            QMessageBox.critical(None, "Database Error",
		    self.db.lastError().text())   
        self.sql1= "SELECT * FROM "
        self.sql1+="life_insurance"

        self.edit = QtGui.QLineEdit(self)
        self.button = QtGui.QPushButton('Search', self)
        self.button.clicked.connect(self.search)
        self.layout.addWidget(self.table,3,0)
        self.table.verticalHeader().hide()

        self.layout.addWidget(self.edit, 2, 0)
        self.layout.addWidget(self.button, 2, 1)
        self.layout.addWidget(self.sortbyLabel, 2, 4)
        self.layout.addWidget(self.comboBox,2,5)
        self.btn1 = QPushButton("Load")
        self.btn1.clicked.connect(self.load)
        self.layout.addWidget(self.btn1,5,5)
        win.showMaximized()
        self.load()



    def createuser(self):
        self.clear()
        
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.start)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)
        self.label11 = QtGui.QLabel("Sign up here")
        self.label11.setStyleSheet("color:red")
        self.layout.addWidget(self.label11, 1, 3)

        self.usernameLabel = QtGui.QLabel("Enter Your Name")
        self.usernameEdit = QtGui.QLineEdit(self)
        self.EmailLabel = QtGui.QLabel("Enter Email")
        self.EmailEdit = QtGui.QLineEdit(self)
        self.phoneLabel = QtGui.QLabel("Enter Phone No")
        self.phoneEdit = QtGui.QLineEdit(self)
        validator = QtGui.QIntValidator()
        self.phoneEdit.setValidator(validator)
        self.phoneEdit.setMaxLength(10)
        self.nameLabel = QtGui.QLabel("User id:")
        self.nameEdit = QtGui.QLineEdit(self)
        self.passwordLabel = QtGui.QLabel("Password:")
        self.passwordEdit = QtGui.QLineEdit(self)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.RetypepasswordLabel = QtGui.QLabel("Retype password:")
        self.RetypepasswordEdit = QtGui.QLineEdit(self)
        self.RetypepasswordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.submitbtn = QtGui.QPushButton("Submit")
        self.submitbtn.clicked.connect(self.validate)
        self.layout.addWidget(self.usernameLabel, 2, 3)
        self.layout.addWidget(self.usernameEdit, 3, 3)
        self.layout.addWidget(self.EmailLabel, 4, 3)
        self.layout.addWidget(self.EmailEdit, 5, 3)
        self.layout.addWidget(self.phoneLabel, 6, 3)
        self.layout.addWidget(self.phoneEdit, 7, 3)
        self.layout.addWidget(self.nameLabel, 8, 3)
        self.layout.addWidget(self.nameEdit, 9, 3)
        self.layout.addWidget(self.passwordLabel, 10, 3)
        self.layout.addWidget(self.passwordEdit, 11, 3)
        self.layout.addWidget(self.RetypepasswordLabel, 12, 3)
        self.layout.addWidget(self.RetypepasswordEdit, 13, 3)
        self.layout.addWidget(self.submitbtn, 14, 3)

           
    def validate(self):
        conn=mysql.connect(user='root', password='admin123', host='127.0.0.1')
        cursor=conn.cursor()
        cursor.execute("use insurance")
        sql="SELECT * FROM admin"
        cursor.execute(sql)
        results=cursor.fetchall()
        conn.commit()
        conn.close()
        if results  == []:
            print("true")
            global userid
            global password
            a = self.nameEdit.text()
            b= self.passwordEdit.text()
            c = self.RetypepasswordEdit.text()
            x=1
            for i in range(x):
                
                if len(self.usernameEdit.text()) > 0:
                    pass
                else:
                    self.usernameEdit.setFocus()
                    QtGui.QMessageBox.warning(None,"Create User","Enter Your Name Feild Is Empty", "Retry")
                    break
                
                if len(self.EmailEdit.text()) > 0:
                    pass
                else:
                    self.EmailEdit.setFocus()
                    QtGui.QMessageBox.warning(None,"Create User","Email Id  Feild Is Empty", "Retry")
                    break
                if len(self.phoneEdit.text()) > 0:
                    pass
                else:
                    self.phoneEdit.setFocus()
                    QtGui.QMessageBox.warning(None,"Create User","Phone No Feild Is Empty", "Retry")
                    break
                if len(self.nameEdit.text()) > 0:
                    pass
                else:
                    self.nameEdit.setFocus()
                    QtGui.QMessageBox.warning(None,"Create User","User id Feild Is Empty", "Retry")
                    break
                
                if len(self.passwordEdit.text()) > 0:
                    if len(self.RetypepasswordEdit.text()) > 0:
                        if b == c:
                            uname=self.usernameEdit.text()
                            email=self.EmailEdit.text()
                            pno=self.phoneEdit.text()
                            uid=self.nameEdit.text()
                            pword=self.passwordEdit.text()
                            conn=mysql.connect(user='root', password='admin123', host='127.0.0.1')
                            cursor=conn.cursor()
                            cursor.execute("use insurance")
                            sql="INSERT INTO admin VALUES(0,'"+uname+"','"+email+"','"+pno+"','"+uid+"','"+pword+"')"
                            QtGui.QMessageBox.warning(None,"Create User","User Successfully Created", "Done")
                            self.myThread = Thread()
                            self.myThread.start()
                            cursor.execute(sql)
                            conn.commit()
                            conn.close()
                            self.start()
                        else:
                            self.passwordEdit.clear()
                            self.RetypepasswordEdit.clear()
                            QtGui.QMessageBox.warning(None,"Create User","Password Didn't Match ", "Retry")
                    else:
                        QtGui.QMessageBox.warning(None,"Create User","Retype Pasword Feild Is Empty ", "Retry")
                else:
                    self.passwordEdit.setFocus()
                    QtGui.QMessageBox.warning(None,"Create User","Pasword Feild Is Empty", "Retry")
                    break
        
        else:
            QtGui.QMessageBox.warning(None,"Create User","User Already Created, Please Login", "Ok")
            self.start()
        
    def clear(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()




    def home(self):
        self.clear()
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.start)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 6)
        self.btnacc = QtGui.QPushButton("My Account")
        self.btnacc.setIcon(QtGui.QIcon('Images/createuser.png'))
        self.btnacc.setStyleSheet("color:blue")
        self.btnacc.clicked.connect(self.account)
        self.layout.addWidget(self.btnacc, 0, 3)
        self.label11 = QtGui.QPushButton("Select Your Option")
        self.label11.setStyleSheet("color:red")
        self.layout.addWidget(self.label11, 1, 3)

        
        self.btn1 = QtGui.QPushButton("Mediclaim")
        self.btn1.clicked.connect(self.mediclaim)
        self.btn1.setMinimumHeight(60)
        self.btn1.setMinimumWidth(80)
        self.btn2 = QtGui.QPushButton("Documents")
        self.btn2.clicked.connect(self.documents)
        self.btn2.setMinimumHeight(60)
        self.btn2.setMinimumWidth(80)
        self.btn3 = QtGui.QPushButton("GST")
        self.btn3.clicked.connect(self.CarInsurance)
        self.btn3.setMinimumHeight(60)
        self.btn3.setMinimumWidth(80)
        self.btn4 = QtGui.QPushButton("Insurance")
        self.btn4.clicked.connect(self.insurance)
        self.btn4.setMinimumHeight(60)
        self.btn4.setMinimumWidth(80)
        self.btn5 = QtGui.QPushButton("IT Return")
        self.btn5.clicked.connect(self.itreturn)
        self.btn5.setMinimumHeight(60)
        self.btn5.setMinimumWidth(80)
        self.btn6 = QtGui.QPushButton("Event")
        self.btn6.clicked.connect(self.events)
        self.btn6.setMinimumHeight(60)
        self.btn6.setMinimumWidth(80)
        self.btn7 = QtGui.QPushButton("Resale Car/Bike")
        self.btn7.clicked.connect(self.BikeInsurance)
        self.btn7.setMinimumHeight(60)
        self.btn7.setMinimumWidth(80)
        
        self.layout.addWidget(self.btn1, 2, 1)
        self.layout.addWidget(self.btn2, 2, 3)
        self.layout.addWidget(self.btn3, 2, 5)
        self.layout.addWidget(self.btn4, 3, 3)
        self.layout.addWidget(self.btn5, 4, 1)
        self.layout.addWidget(self.btn6, 4, 3)
        self.layout.addWidget(self.btn7, 4, 5)



    def TableView(self,text,text1):
        self.clear()
        self.dbase=text
        self.data=text1 
        
        self.sortbyLabel = QtGui.QLabel("Sort By")
        
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("First_Name")
        self.comboBox.addItem("Last_Name")
        self.comboBox.addItem("Email_Id")
        self.comboBox.addItem("Age")
        self.comboBox.addItem("Start_Date")
        self.comboBox.addItem("End_Date")
        self.comboBox.move(50, 250)
        self.comboBox.activated[str].connect(self.clicked)
        
        
        self.btn= QLabel(self)
        self.btn.setText(text1)
        self.btn.setStyleSheet("color:red")
        self.btn1 = QPushButton("Load")
        self.btn1.clicked.connect(self.load)
        self.btn2 = QPushButton("Add Row")
        self.btn2.clicked.connect(self.openWindow)
        self.btn3 = QPushButton("Delete Row")
        self.btn3.clicked.connect(self.deleteWindow)
        self.btn4 = QPushButton("Change Value")
        self.btn4.clicked.connect(self.changeWindow)
        self.table = QTableWidget(self)
        self.table.setFixedSize(825,400)
        self.db 	= QSqlDatabase.addDatabase("QMYSQL")

        self.db.setHostName("localhost")
        self.db.setDatabaseName(text)
        self.db.setUserName("root")
        self.db.setPassword("admin123")

        if (self.db.open()==False):     
            QMessageBox.critical(None, "Database Error",
		    self.db.lastError().text())   
        self.sql1= "SELECT * FROM "
        self.sql1+=text1

        self.edit = QtGui.QLineEdit(self)
        self.button = QtGui.QPushButton('Search', self)
        self.button.clicked.connect(self.search)
        self.layout.addWidget(self.table,3,0)
        self.table.verticalHeader().hide()
        self.layout.addWidget(self.btn, 1, 0)
        self.layout.addWidget(self.edit, 2, 0)
        self.layout.addWidget(self.button, 2, 1)
        self.layout.addWidget(self.sortbyLabel, 2, 4)
        self.layout.addWidget(self.comboBox,2,5)
        self.layout.addWidget(self.btn1, 4,0)
        self.layout.addWidget(self.btn2, 4, 5)
        self.layout.addWidget(self.btn3, 5, 5)
        self.layout.addWidget(self.btn4, 6,5)
        win.showMaximized()

    def search(self):
        self.find = self.edit.text()
        self.load()
        items = self.table.findItems(
            self.find, QtCore.Qt.MatchExactly)           


        if items:
            for item in items:
                m=item.row()
                n=item.column()
                self.y=[]
                self.k=[]
                self.y.append(m)
                self.k.append(n)
                self.table.item(m,n).setBackground(QtGui.QColor(125,125,125))
        else:
            results = 'Found Nothing'
            QtGui.QMessageBox.information(self, 'Search Results', results)
            self.edit.clear()



    def insurance(self):

        self.clear()
        
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.home)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)
        self.label11 = QtGui.QLabel("Select Insurance")
        self.label11.setStyleSheet("color:red")
        self.layout.addWidget(self.label11, 0, 3)
        

        
        self.btn1 = QtGui.QPushButton("Health Insurance")
        self.btn1.clicked.connect(self.healthinsurance)
        self.btn1.setMinimumHeight(60)
        self.btn1.setMinimumWidth(80)
        self.btn2 = QtGui.QPushButton("Life Insurance")
        self.btn2.clicked.connect(self.lifeinsurance)
        self.btn2.setMinimumHeight(60)
        self.btn2.setMinimumWidth(80)
        self.btn3 = QtGui.QPushButton("Workmen Insurance")
        self.btn3.clicked.connect(self.workmeninsurance)
        self.btn3.setMinimumHeight(60)
        self.btn3.setMinimumWidth(80)
        self.btn4 = QtGui.QPushButton("Travel Insurance")
        self.btn4.clicked.connect(self.travelinsurance)
        self.btn4.setMinimumHeight(60)
        self.btn4.setMinimumWidth(80)
        self.btn5 = QtGui.QPushButton("Fire Insurance")
        self.btn5.clicked.connect(self.fireinsurance)
        self.btn5.setMinimumHeight(60)
        self.btn5.setMinimumWidth(80)
        self.btn6 = QtGui.QPushButton("Home Insurance")
        self.btn6.clicked.connect(self.homeinsurance)
        self.btn6.setMinimumHeight(60)
        self.btn6.setMinimumWidth(80)
        self.btn7 = QtGui.QPushButton("Marine Insurance")
        self.btn7.clicked.connect(self.marineinsurance)
        self.btn7.setMinimumHeight(60)
        self.btn7.setMinimumWidth(80)
        
        self.layout.addWidget(self.btn1, 1, 3)
        self.layout.addWidget(self.btn2, 2, 3)
        self.layout.addWidget(self.btn3, 3, 3)
        self.layout.addWidget(self.btn4, 4, 3)
        self.layout.addWidget(self.btn5, 5, 3)
        self.layout.addWidget(self.btn6, 6, 3)
        self.layout.addWidget(self.btn7, 7, 3)
        

    
    def load(self):
        print(self.sql1)
        self.query = QSqlQuery (self.sql1)
        self.table.setColumnCount(self.query.record().count())
        self.table.setRowCount(self.query.size())
        self.table.setHorizontalHeaderLabels(['Policy No', 'Fisrt Name', 'Last Name', 'Start Date', 'End Date',
                                              'Email Id','Age','Phone No'])
        index=0
        while (self.query.next()):
                self.table.setItem(index,0,QTableWidgetItem(str(self.query.value(0))))
                self.table.setItem(index,1,QTableWidgetItem(str(self.query.value(1))))
                self.table.setItem(index,2,QTableWidgetItem(str(self.query.value(2))[::-1]))
                self.table.setItem(index,3,QTableWidgetItem(str(self.query.value(3))[::-1]))
                self.table.setItem(index,4,QTableWidgetItem(str(self.query.value(4))))
                self.table.setItem(index,5,QTableWidgetItem(str(self.query.value(5))))
                self.table.setItem(index,6,QTableWidgetItem(str(self.query.value(6))))
                self.table.setItem(index,7,QTableWidgetItem(str(self.query.value(7))))
                index = index+1
        self.table.show()

    def load1(self):
        print(self.sql)
        index=0
        while (self.query.next()):
                self.table.setItem(index,0,QTableWidgetItem(str(self.query.value(0))))
                self.table.setItem(index,1,QTableWidgetItem(str(self.query.value(1))))
                self.table.setItem(index,2,QTableWidgetItem(str(self.query.value(2))[::-1]))
                self.table.setItem(index,3,QTableWidgetItem(str(self.query.value(3))[::-1]))
                self.table.setItem(index,4,QTableWidgetItem(str(self.query.value(4))))
                self.table.setItem(index,5,QTableWidgetItem(str(self.query.value(5))))
                self.table.setItem(index,6,QTableWidgetItem(str(self.query.value(6))))
                self.table.setItem(index,7,QTableWidgetItem(str(self.query.value(7))))
                index = index+1
        self.table.show()


    def clicked(self,text):
        a=text
        b=self.data
        self.sorting(a,b)

    def sorting(self,text,text1):
        self.sql = 'select * from  '
        self.sql+=text1
        m = ' order by '
        self.sql+=m
        self.sql+=text
        self.query = QSqlQuery (self.sql)
        self.load1()

    def lifeinsurance(self):
        text="insurance"
        text1="Life_Insurance"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.insurance)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)
        

    def homeinsurance(self):
        text="insurance"
        text1="Home_Insurance"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.insurance)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)

    def workmeninsurance(self):
        text="insurance"
        text1="Workmen_Insurance"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.insurance)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)


    def travelinsurance(self):
        text="insurance"
        text1="Travel_Insurance"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.insurance)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)


    def fireinsurance(self):
        text="insurance"
        text1="Fire_Insurance"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.insurance)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)


    def marineinsurance(self):
        text="insurance"
        text1="Marine_Insurance"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.insurance)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)


    def healthinsurance(self):
        text="insurance"
        text1="Health_Insurance"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.insurance)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)

    def BikeInsurance(self):
        text="insurance"
        text1="BikeInsurance"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.home)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)

    def mediclaim(self):
        text="insurance"
        text1="Mediclaim"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.home)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)



    def CarInsurance(self):
        text="insurance"
        text1="CarInsurance"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.home)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)


    def documents(self):
        text="insurance"
        text1="Documents"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.home)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)

    def itreturn(self):
        text="insurance"
        text1="It_Return"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.home)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)

    def events(self):
        text="insurance"
        text1="Events"
        self.TableView(text,text1)
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('Images/back.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.home)
        self.layout.addWidget(self.toolButton, 0, 0)
        self.toolButton1 = QToolButton(self)
        self.toolButton1.setIcon(QtGui.QIcon('Images/quit.png'))
        self.toolButton1.setCheckable(True)
        self.toolButton1.toggled.connect(self.close)
        self.layout.addWidget(self.toolButton1, 0, 8)



    
app = QtGui.QApplication(sys.argv)
win = QtGui.QWidget()
GUI =Window()
GUI.begin()
win.show()
sys.exit(app.exec_())
