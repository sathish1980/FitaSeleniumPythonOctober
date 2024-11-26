import mysql.connector
from mysql.connector import Error


class connectdb():
    connection ='null'
    cursor='null'
    def connect(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                 database='fitapython',
                                                 user='root',
                                                 password='Admin@123')
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
        """finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("MySQL connection is closed")"""

    def CreateTable(self):

        try:
            mySql_Create_Table_Query = """CREATE TABLE FitaCourse ( 
                                         Id int(11) NOT NULL,
                                         Description varchar(250) NOT NULL,
                                         Status varchar(250) NOT NULL) """

            cursor = self.connection.cursor()
            result = cursor.execute(mySql_Create_Table_Query)
            print("Fita Course Table created successfully ")

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        """finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("MySQL connection is closed")"""

    def InsertcourseIntoDB(self):

        try:
            mySql_insert_query = """INSERT INTO fitacourse
                                       VALUES 
                                       (2, 'Python','Active') """

            cursor = self.connection.cursor()
            cursor.execute(mySql_insert_query)
            self.connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Laptop table")
            cursor.close()
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("MySQL connection is closed")


    def InsertcourseIntoDBmultipleValue(self,id,coursename,status):

        try:
            mySql_insert_query = """INSERT INTO fitacourse
                                               VALUES 
                                               (%s, %s,%s) """

            record = (id,coursename,status)
            self. cursor = self.connection.cursor()
            self.cursor.execute(mySql_insert_query,record)
            self.connection.commit()
            print(self.cursor.rowcount, "Record inserted successfully into Laptop table")
            self.cursor.close()
        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        """finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("MySQL connection is closed")"""

    def UpdatecourseIntoDB(self):

        try:
            sql_update_query = """Update fitacourse set Description = 'PYTHON' where id = 100"""
            self.cursor.execute(sql_update_query)
            self.connection.commit()
            print("Record Updated successfully ")

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        """finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("MySQL connection is closed")"""

    def UpdatecourseIntoDBmultipleValue(self,coursename,id):

        try:
            sql_update_query = """Update fitacourse set Description = %s where id = %s"""
            record =(coursename,id)
            self.cursor.execute(sql_update_query,record)
            self.connection.commit()
            print("Record Updated successfully ")

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))
        """finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("MySQL connection is closed")"""

    def FetchCourse(self):

        sql_select_Query = "select * from fitacourse where status ='Active'"
        cursor = self.connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        for eachRow in records:
            print(eachRow)
            print("Id = ", eachRow[0], )
            print("coursename = ", eachRow[1])
            #print("status  = ", eachRow[2])"""


    def closeConnection(self):

        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")




obj= connectdb()
obj.connect()
#obj.UpdatecourseIntoDBmultipleValue()
"""obj.UpdatecourseIntoDBmultipleValue("JAVA",1)
obj.UpdatecourseIntoDBmultipleValue("REACT",4)
obj.UpdatecourseIntoDBmultipleValue("SELENIUM",6)"""
obj.FetchCourse()
#obj.CreateTable()
#obj.InsertcourseIntoDB()
"""obj.InsertcourseIntoDBmultipleValue(3,'SQL','InActive')
obj.InsertcourseIntoDBmultipleValue(4,'React','Active')
obj.InsertcourseIntoDBmultipleValue(5,'DEVOPS','Active')
obj.InsertcourseIntoDBmultipleValue(6,'Selenium','InActive')"""
obj.closeConnection()
