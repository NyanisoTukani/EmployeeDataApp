#This code is created by Nyaniso Tukai
#Contact details : 0680304748
#Email : xolilizwenyaniso7@gmail.com
#Linkedin Link : https://www.linkedin.com/in/nyaniso-tukani-18898827b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BH%2BqWgfWWQSW%2BkfPBMSfAdQ%3D%3D

import EmployeeManager as emp

choice = int(input("Enter choice :"))
while choice != 6:
    if choice == 1:
        emp.createTable()
        print("Table created successfully")
    elif choice == 2:
        empId = int(input("Enter the employee ID : "))
        name = input("Enter the employee name : ")
        surname = input("Enter the employee surname : ")
        salary = float(input("Enter the employee salary : "))
        emp.storeData(empId,name,surname,salary)
        print("Data stored successfully")
    elif choice == 3:
        empId = int(input("Enter the employee ID : "))
        surname = input("Enter the employee surname : ")
        salary = float(input("Enter the employee salary : "))
        emp.updateData(empId,surname,salary)
        print("Data updated successfully")
    elif choice == 4:
        empId = int(input("Enter the employee ID : "))
        cursor = emp.getEmployee(empId)
        for row in cursor:
            print("EMPLOYEE ID\tNAME\tSURNAME\t    SALARY")
            print(str(row[0])+"\t        "+row[1]+"\t"+row[2]+"\t"+str(row[3]))
    elif choice == 5:
        cursor = emp.getAll()
        for row in cursor:
            print("EMPLOYEE ID\tNAME\tSURNAME\t    SALARY\n"+
                  str(row[0]) + "\t        " + row[1] + "\t" + row[2] + "\t" + str(row[3])+"\n")

    else:
        print("Invalid choice Please re-enter")
    choice = int(input("Enter choice :"))
print("Goodbye!!!!!!!!!!!!!!!!!!!!!!")
