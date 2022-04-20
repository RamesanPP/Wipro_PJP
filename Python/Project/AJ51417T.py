from multiprocessing.pool import TERMINATE


class Employee:
    count=0
    Empid=0
    Ename=""
    Sal=0
    Deptno=0 
    def __init__(self, Empid, Ename, Sal, Deptno):
        self.Empid = Empid
        self.Ename = Ename
        self.Sal = Sal
        self.Deptno = Deptno
        Employee.count += 1
    
    
    
def Add_Emp():
    # Get empid from user and check if valid
    empid=int(input("Enter the Empid:"))
    if (len(str(empid))<3):
        print("Should be 3 or more digits")
        return
    if empid==Employee.Empid:
        print("Should have Unique ID")
        return


    # Get name from user and check if valid
    ename=input("Enter the name: ")
    ename=ename.upper()


    # Get Salary from user and check if valid
    sal=int(input("Enter the Salary: "))
    if sal<3000:
        print("Should be more than 3000")
        return


    # Get Deptno from user and check if valid
    dep=int(input("Enter the DeptNo:"))
    if dep!=10 and dep!=20 and dep!=30:
        print("Should be either 10, 20 or 30")
        return


    # Write employee to file
    file = open("Project/emp.txt", "a")
    s="Empid = "+str(empid)+"\nEname = "+ename+"\nSal = "+str(sal)+"\nDeptno = "+str(dep)+'\n'
    file.write(s)
    file.close()



def Display_Emp():
    print("Empid = ",Employee.Empid,"\nEname = ",Employee.Ename,"\nSal = ",Employee.Sal,"\nDeptno = ",Employee.Deptno)


def Separate_Data():
    with open("emp.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
            if line.startswith("Deptno") and line.endswith("10"):
                file = open("emp_10.txt","a")
                file.write(lines)
                file.close
                lines.clear()
            elif line.startswith("Deptno") and line.endswith("20"):
                file = open("emp_20.txt","a")
                file.write(lines)
                file.close
                lines.clear()
            elif line.startswith("Deptno") and line.endswith("30"):
                file = open("emp_30.txt","a")
                file.write(lines)
                file.close
                lines.clear()

  
# Display Menu and get choice
ch = int(input("1. Add_emp \n2. Display_emp \n3. Seperate_data \n4. Exit \n"))
if ch == 1:
    Add_Emp()
elif ch == 2:
    Display_Emp()
elif ch == 3:
    Separate_Data()
else:
    TERMINATE


