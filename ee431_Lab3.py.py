
###########################################################
#
#                 SQL BASIC QUERIES
#
#               @Author: TuringMach1ne
#
###########################################################
import sqlite3

# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database
class DBOperations:
  
  sql_create_table_firsttime = "CREATE TABLE IF NOT EXISTS \
        EmployeeUoB (EmployeeID INTEGER PRIMARY KEY,\
        EmployeeTitle VARCHAR (3) NOT NULL, ForeName VARCHAR (20), SurName VARCHAR (20), Email VARCHAR (30), Salary INTEGER UNSIGNED)"
  
  sql_create_table = "CREATE TABLE 'EmployeeUoB' \
         (EmployeeID INTEGER PRIMARY KEY, EmployeeTitle VARCHAR (3),\
          ForeName VARCHAR (20), SurName VARCHAR (20), Email VARCHAR (30), Salary INTEGER UNSIGNED)"
  
  sql_insert = "INSERT INTO EmployeeUoB (EmployeeID, EmployeeTitle, ForeName, Surname, Email, Salary) VALUES(?,?,?,?,?,?)"
  
  sql_select_all= "SELECT * FROM EmployeeUoB"
  
  sql_search= "SELECT * FROM EmployeeUoB WHERE EmployeeID =?"
  
  sql_update_data = "UPDATE EmployeeUoB SET WHERE EmployeeID = ?"
  
  sql_delete_data = "DELETE FROM EmployeeUoB WHERE EmployeeID =?"
  
  sql_drop_table ="DROP TABLE EmployeeUoB"


  #control_sql = "SELECT COUNT(*) FROM EmployeeUoB WHERE EmployeeID =?"

  def __init__(self):
    try:
      self.conn = sqlite3.connect("MyDataStore.db")
      self.cur = self.conn.cursor()
      self.cur.execute(self.sql_create_table_firsttime)
      self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()
  
  def get_connection(self):
    self.conn = sqlite3.connect("MyDataStore.db")
    self.cur = self.conn.cursor()

  def create_table(self):
    try:
     self.get_connection()
     
     self.cur.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='EmployeeUoB' ''')
     if self.cur.fetchone()[0]==1 : 
	      print("Table exists.")
     
     else:
      self.cur.execute(self.sql_create_table)
      self.conn.commit()
      print("Table created successfully")
    #except sqlite3.OperationalError:
      #print("This table already exists")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_data(self):
    try:
      self.get_connection()
      emp = Employee()
      
      emp.set_employee_id(int(input("Enter Employee ID: ")))
      emp.set_employee_title(str(input("Enter Employee title: ")))
      emp.set_forename(str(input("Enter Employee name: ")))
      emp.set_surname(str(input("Enter Employee surname  : ")))
      emp.set_email(str(input("Enter Employee e-mail address: ")))
      emp.set_salary(int(input("Enter Employee salary: ")))
      print("\n")
      #print(tuple(str(emp)))
      self.cur.execute(self.sql_insert,tuple(str(emp).split("\n")))
      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()
  
  def select_all(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all)
      results = self.cur.fetchall()

      for row in results:
        attributes = ["Employee ID", "Title", "Forename", "Surname", "Email", "Salary"]
        print("\n")
        print(attributes[0]+ "\t" + str(row[0]))
        print(attributes[1]+ "\t"+ str(row[1]))
        print(attributes[2]+ "\t"+ str(row[2]))
        print(attributes[3]+ "\t"+ str(row[3]))
        print(attributes[4]+ "\t"+ str(row[4]))
        print(attributes[5]+ "\t"+ str(row[5]))
        
        
      # think how you could develop this method to show the records

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


  def search_data(self):
    try:
      self.get_connection()
      employeeID = int(input("Enter employee ID: "))
      cur = self.conn.cursor()
      cur.execute("SELECT * FROM EmployeeUoB WHERE EmployeeID =?",(employeeID,))
      rows = cur.fetchall()
      if len(rows) ==0:
        print("\nNo Record\n")
      else:
        print("\n")
        print("Employee ID: "+ str(rows[0][0]))
        print("Employee Title: " + str(rows[0][1]))
        print("Employee Name: " + str(rows[0][2]))
        print("Employee Surname: "+ str(rows[0][3]))
        print("Employee Email: "+ str(rows[0][4]))
        print("Salary: "+ str(rows[0][5]))
    except Exception as e:
      print(e)
    finally:
      self.conn.close()
  
  def update_data(self):
    try:
      self.get_connection()
      updateID = str(input("Enter the Employee ID to update records"))
      print("Which attribute you'd like to update? Please choose 1-6: ")
      print("1->Title\n2->Forename\n3->Surname\n4->Email\n5->Salary\n6->Cancel")
      updateRecord = int(input("Choose 1-6: "))

      if updateRecord == 1:
        updateField = "EmployeeTitle"
        fieldValue = str(input("Enter Employee title: "))
      elif updateRecord == 2:
        updateField = "forename"
        fieldValue = str(input("Enter Employee Forename: "))
      elif updateRecord == 3:
        updateField = "surname"
        fieldValue = str(input("Enter Employee Surname: "))
      elif updateRecord == 4:
        updateField = "email"
        fieldValue = str(input("Enter Employee Email: "))
      elif updateRecord == 5:
        updateField = "salary"
        fieldValue = int(input("Enter Employee Salary: "))
      elif updateRecord == 6:
        return

      field = updateField + "=" + fieldValue
      updating = self.sql_update_data.format(field, updateID)
      self.get_connection()
      self.cur.execute(updating)
      self.conn.commit()


      if self.cur.rowcount !=0:
        result = self.cur.fetchone()
        print(str(result.rowcount)+ "Row(s) affected.")
      else:
        print("Cannot find this record in the database")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  #define delete_data method to delete data from the table. the user will need to input the employee id to delete the corresponding record.
  def delete_data(self):
    try:
      self.get_connection()
      deleteEmployeeID = int(input("Enter the Employee ID to be deleted: "))
      cur = self.conn.cursor()

      cur.execute("SELECT * FROM EmployeeUoB WHERE EmployeeID =?",(deleteEmployeeID,))

      rows = cur.fetchall()

      if len(rows) ==0:
        print("\nNo Record\n")
      else:
        cur.execute('DELETE FROM EmployeeUoB WHERE EmployeeID =?',(deleteEmployeeID,))
        self.conn.commit()
        print("Record deleted successfully ")
        self.conn.close()

    except Exception as error:
        print("Failed to delete record from table", error)
    finally:
        if (self.conn):
            self.conn.close()
            print("connection is closed")

  
  def drop_table(self):
    decision = input("Dropping the data will erase the data will you continue? Y/N")
    if decision == 'Y' or decision == 'y':

      try:
        self.get_connection()
        self.conn.execute(self.sql_drop_table)
        self.conn.commit
        print("Table has been dropped successfully")
      except Exception as e:
        print(e)
      finally:
        self.conn.close()
    else:
      print("Drop cancelled")

class Employee:
  def __init__(self):
    self.employeeID = 0
    self.empTitle = ''
    self.forename = ''
    self.surname = ''
    self.email = ''
    self.salary = 0

  def set_employee_id(self, employeeID):
    self.employeeID = employeeID
  def set_employee_title(self, empTitle):
    self.empTitle = empTitle
  def set_forename(self, forename):
    self.forename = forename
  def set_surname(self, surname):
    self.surname = surname
  def set_email(self, email):
    self.email = email
  def set_salary(self, salary):
    self.salary = salary

  def get_employee_id(self):
    return self.employeeID
  def get_employee_title(self):
    return self.empTitle
  def get_forename(self):
    return self.forename
  def get_surname(self):
    return self.surname
  def get_email(self):
    return self.email
  def get_salary(self):
    return self.salary

  def __str__ (self):
    return str(self.employeeID) + "\n" + self.empTitle + "\n" +    self.forename + "\n" + self.surname + "\n" + self.email + "\n" + str(self.salary)


# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

while True:
  print("\n Menu:")
  print("**********")
  print("1. Create table EmployeeUoB")
  print("2. Insert data into EmployeeUoB")
  print("3. Select all data into EmployeeUoB")
  print("4. Search an employee")
  print("5. Update data some records")
  print("6. Delete data some records")
  print("7. Drop the table")
  print("8. Exit\n")
#while True:
  __choose_menu = int(input("Enter your choice:  "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    db_ops.create_table()
  elif __choose_menu == 2:
    db_ops.insert_data()
  elif __choose_menu == 3:
    db_ops.select_all()
  elif __choose_menu == 4:
    db_ops.search_data()
  elif __choose_menu == 5:
    db_ops.update_data()
  elif __choose_menu == 6:
    db_ops.delete_data()
  elif __choose_menu == 7:
    db_ops.drop_table()
  elif __choose_menu == 8:
    exit(0)
  else:
    print("Invalid Choice")
