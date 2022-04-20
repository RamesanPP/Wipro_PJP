from os.path import exists


class Employee:
    Empid=0
    Ename=""
    Sal=0
    Deptno=0 
    def __init__(self, Empid, Ename, Sal, Deptno, count):
        self.Empid = Empid
        self.Ename = Ename
        self.Sal = Sal
        self.Deptno = Deptno



def Add_Emp():
    # Get empid from user and check if valid
    empid=int(input("Enter the Empid: "))
    if (len(str(empid))<3):
        print("Should be 3 or more digits")
        return
    if exists("Project/emp.txt"):
        with open("Project/emp.txt", 'r') as f:
            l = f.readlines()
            l = [x.strip() for x in l]
            for line in l:
                if line.startswith("Empid") and line.endswith(str(empid)):  
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
    dep=int(input("Enter the DeptNo: "))
    if dep!=10 and dep!=20 and dep!=30:
        print("Should be either 10, 20 or 30")
        return


    # Write employee to file
    file = open("Project/emp.txt", "a")
    s="Empid = "+str(empid)+"\nEname = "+ename+"\nSal = "+str(sal)+"\nDeptno = "+str(dep)+'\n'
    file.write(s)
    file.close()



def Display_Emp():
    if exists("Project/emp.txt"):
        with open("Project/emp.txt") as f:
            contents = f.read()
            print (contents)
    else:
        print("No Employees")


def Separate_Data():
    if exists("Project/emp.txt"):
        with open("Project/emp.txt") as f:
            l = f.readlines()
            l = [x.strip() for x in l]
            lines = []
            for line in l:
                lines.append(line)
                if line.startswith("Deptno") and line.endswith("10"):
                    file = open("Project/emp_10.txt","a")
                    for s in lines:
                        file.write(s + "\n")
                    file.close
                    lines.clear()
                elif line.startswith("Deptno") and line.endswith("20"):
                    file = open("Project/emp_20.txt","a")
                    for s in lines:
                        file.write(s + "\n")
                    file.close
                    lines.clear()
                elif line.startswith("Deptno") and line.endswith("30"):
                    file = open("Project/emp_30.txt","a")
                    for s in lines:
                        file.write(s + "\n")
                    file.close
                    lines.clear()

    else:
        print("No data")

  
# Display Menu and get choice
t = True
while t:
    ch = int(input("1. Add_emp \n2. Display_emp \n3. Separate_data \n4. Exit \n"))
    if ch == 1:
        Add_Emp()
    elif ch == 2:
        Display_Emp()
    elif ch == 3:
        Separate_Data()
    else:
        t = False

