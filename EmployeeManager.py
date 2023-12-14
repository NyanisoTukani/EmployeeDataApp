import sqlite3
con = sqlite3.connect("Employee.db")
print(str(con)+" is connected")

def createTable():
    con.execute(
        '''
        CREATE TABLE EMPLOYEE_TABLE
        (
        EMP_ID INT PRIMARY KEY NOT NULL,
        NAME VARCHAR2(30),
        SURNAME VARCHAR2(30),
        SALARY DOUBLE
        );
        '''
    )
def storeData(id , name, surname,salary):
    con.execute(
        "INSERT INTO EMPLOYEE_TABLE "
        "VALUES ('"+str(id)+"','"+name+"','"+surname+"','"+str(salary)+"')"
    );
    con.commit()
def updateData(id,surname,salary):
    con.execute(
        "UPDATE EMPLOYEE_TABLE "
        "SET SURNAME = '"+surname+"', SALARY = '"+str(salary)+"' "
        "WHERE EMP_ID = '"+str(id)+"'"
    );
    con.commit()
def getEmployee(id):
    cursor = con.execute("SELECT * FROM EMPLOYEE_TABLE "
                "WHERE EMP_ID = '"+str(id)+"'");
    return cursor

    con.commit()
def getAll():

    cursor = con.execute("SELECT * FROM EMPLOYEE_TABLE ");
    return cursor
    con.commit()


