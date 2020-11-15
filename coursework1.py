'''student name: Farhan Bhatti
Student id: 3712356
student email: bhattif3@lsbu.ac.uk
'''
ID=[] #list to add ID
employees = [] #a list to store the employee name emtered by the user
designation_field = [] #{} a list to store the designation feild
department_field = []#{} a list to store the department
status_field = []#{} a list to store their status
joining_date_field = []#{}''' a list to store their joining date
text = 'Employee Database' #text to put into the database
text2= 'ID' #puts the text in the file as a header
text3= 'name' #puts the text in the file as a header
text4 = 'Department' #puts the text in the file as a header
text5 = 'Designation' #puts the text in the file as a header
text6 = 'Joining date' #puts the text in the file as a header
text7 = 'Employee status' #puts the text in the file as a header
file = open('employee_database.csv','w+') #will read and write to the file
try:
    for line in file:
        employee_details = line.split(",") #splits the employee data
        value = employee_details[1]
        if (value != ""):
            ID.append(employee_details[0]) #add to the file
            employees.append(employee_details[1]) #add to file
            designation_field.append(employee_details[2]) #add to the list
            department_field.append(employee_details[3]) #add to the list
            status_field.append(employee_details[4]) # add to the list
            joining_date_field.append(employee_details[5]) # add to the list
            break
except IndexError: #prevents a index error
    
        #opens file to create the file if not exist and going to write to file
        file = open('employee_database.csv','w')
        file.write(text.title()+", "+" ") #writes this text to the file
        file.write('\n')
        #prints the text in  single line
        file.write(text2+", "+text3+", "+text4+", "+text5+", "+text6+", "+text7+"\n")
        file.close() #to close the file afer the data has beeen written to the file
else:
    file = open('employee_database.csv','w') #writes to the file
    file.write(text.title()+", "+" ") #writes this text to the file
    file.write('\n')
        #prints the text in  seperate cells
    file.write(text2+", "+text3+", "+text4+", "+text5+", "+text6+", "+text7+"\n")
    file.close() #to close the file


def add(): #fucntion to add employee details
    employee_id = input('Enter their ID number: ') #takes the id of the employee
    name = str(input("Enter the name of the employee to add: ")) #take the employee name
    designation = str(input("Enter the designation of the employee: ")) #takes designation
    department = str(input("Enter the department of the employee: ")) #department they work in
    status = str(input("Enter the status of the employee (active/inactive): ")) # the employee status
    joining_date = str(input("Enter the joining date of the employee (dd/mm/yy): ")) # the date the employee joined
    while True:
        if employee_id in ID: #checks to ensure entered ID is not already in the database
            employee_id = input('That ID is already exists. Please enter another ID number: ')
        elif (name == " ") or (name == "name"): #checks the name is valid
            name = str(input("That name is not valid. Enter the name of the employee to add: ")) #take the employee name
        else:
            break
    ID.append(employee_id)#add to the list
    employees.append(name) #add the employee name to the interface
    designation_field.append(designation)#adds to the list
    department_field.append(department)#add to the list
    status_field.append(status)# adds to the list
    joining_date_field.append(joining_date)#adds to the list

    file = open('employee_database.csv','w+') #open the file to read and write
    #file.write(text2+", "+text3+", "+text4+", "+text5+", "+text6+", "+text7+"\n")
    file.write(text.title()+", "+" ") #writes this text to the file
    file.write('\n')#adds a newline to the file to add texts below
    file.write(text2+", "+text3+", "+text4+", "+text5+", "+text6+", "+text7+"\n")
    for i in range(len(employees)): #checks the legnth of the employee
        #writes the data to the file
        file.write("{}, {}, {}, {}, {}, {}\n".format(ID[i], employees[i], designation_field[i], department_field[i], status_field[i], joining_date_field[i]))
    file.close() #to close the file afer the data has beeen written to the file
    menu() # re opens the main menu 

    
def remove():
    file = open('employee_database.csv','r') #read the file
    remove_employee=str(input('Enter the ID of the employee you would like to remove: '))
     #takes the name of the employee to remvoe from the system
    employee_found = False
    for line in file:
        employee_details =line.split(",")
        ID = employee_details[0]
        if remove_employee in ID: #checks the employee to remove is in the database
            print('found employee')
    #file.close()
    #file = open('employee_database.csv','w')
    for remove_employee in file:
        #checks the condition
        if remove_employee in file and status_feild =='active' in file:
            #if employee is still active will display msg below and not remove employee
            print('Can not remove employee as they are still active!')
        elif remove_employee in file and status_feild =='inactive' in file:
            #checks both conditions
            print('you can remove the employee')
            #file.close()
            file = open('employee_database.csv','w')
            #for i in range(len(remove_employee)):
            emp=remove_employee.join(remove_employee)#join the string togethor
                #remove_employee.remove(ID[i], employees[i], designation_field[i], department_field[i], status_field[i], joining_date_field[i])
                #remove(emp)
                #file = open('employee_database.csv','w')
            remove(emp)
            file.write("")               
            '''employee.remove(remove_employee) #if the employee is inactive their details can be removed
            designation_field.remove(remove_employee)
            department_field.remove(remove_employee)
            status_field.remove(remove_employee)
            joining_date_field.remove(remove_employee)'''
            print('Employee removed') #prints the statement
        elif remove_employee in file and status_feild =='unactive' in file:
            #checks the statement
            print('employee removed')
            employee.remove(remove_employee) #if the employee is unactive their details can be removed
            designation_field.remove(remove_employee)
            department_field.remove(remove_employee)
            status_field.remove(remove_employee)
            joining_date_field.remove(remove_employee)
        else:
            print('Employee does not exist') #prints if employee does not exist
        file.close()
        main() #return to the main menu

    
def edit():
    file = open('employee_database.csv','r') #open the file in read mode
    employee=input("Please enter the employee you would like to edit: ") # takes input
    employee_found = False
    for line in file:
        employee_details = line.split(",")#splits the data
        ID = employee_details[0]
        if employee in ID: #check if employee in the database if so asks what to edit
           # print(employee_details[0],employee_details[1],employee_details[2],employee_details[3],employee_details[4],employee_details[5])
            print('Employee found')
    file.close()#closes the file
    f2 = open('employee_database.csv','w') #opens the file
    option=input('What would you like to edit? \n1.Name\n2.Designated feild\n3.Department\n4.Status\n5.Joining date\n6.Return to Menu\n')
    if option == "1":
        employee_name = input("Enter the new name of the employee: ")#takes input
        employee_name=employee_details[1]
        file.read()#read the file
        new1=file.replace(name,employee_name) #replaces the current name for new name
        file.write(new1)#write to the file
    elif option =="2":
        new_des_feild = input("Enter the new designation field of the employee: ")
        new_feild=employee_details[2]
        file.read()
        new2=file.replace(new_feild,new_des_feild)
        #replace old feild with new feild
        file.write(new2)
    elif option == "3":
        new_depart = input("Enter the new department of the employee: ")#takes input
        #new_depart=employee_details[3]
        new3=file.replace(employee_details,new_depart)
        #replace old depart with new department
        file.write(new3)
    elif option == "4":
        new_status = input("Enter the new status of the employee: ") #takes input
        new_status=employee_details[4]
        file.write(new_status)#writes the new employee status
    elif option == "5":
        new_date = input("Enter the new joinging date of the employee: ") #takes input
        new_date=employee_details[5]
        file.write(new_date) #write the new join date
    elif option == "6":
        menu()#return to the main menu
    else:
        print("Not valid") # if option by user does not match
        employee_found = True #if
    print('The new details are',employee_details[0],employee_details[1],employee_details[2],employee_details[3],employee_details[4],employee_details[5])
    #displays the employees new data
    if employee_found == False:
        print('Employee does not exist!') #displays if employee not found
    menu() #return to main menu
        
def employee_finder(employee):
    file = open('employee_database.csv','r') #will read the file
    employee_found = False
    for line in file:
        employee_details = line.split(",") #splits the employee data
        ID = employee_details[0]
        if employee in ID:
            #prints the employee details if they are found
            print(employee_details[0],employee_details[1],employee_details[2],employee_details[3],employee_details[4],employee_details[5])
            employee_found = True #if
    if employee_found == False:
        print('Employee does not exist!') #prints if the employee not found
    menu()

    
def search():
    #employee_found = False
    #file = open('employee_database.csv','r') 
    employee_search=input("Please enter the id of the employee you would like to search for: ")
    employee_finder(employee_search) #passes the employee to the employee_finder function
        

def menu():
    while True: #a loop that will keep running
        print('\t\t\tMenu') #prints in the console
        #options for user to pick from
        option = input('Select a option:\n\n1.Add employee\n2.Remove employee\n3.Edit details\n4.Search for user\n5.Quit\n')
        if option == "1":
            add() # take the user to add an employee
        elif option =="2":
            remove() # take the user to remove an employee
        elif option == "3":
            edit() # take the user to edit an employee details
        elif option == "4":
            search() # takes the user to search for an employee
        elif option == "5":
            quit() # exit the application
        else:
            print("Not valid") # if option by user does not match
    

def login(user, password):
    if user=="farhan" and password == "chelsea" : #checks condition
        print('Welcome Farhan') #print statement
        menu() #takes user to menu
    elif user == "guest" or password == "guest": #check if input is guest
        print('Welcome guest') #prints guest as statement
        menu() #takes user to menu
    else:
        print('not valid')
        #if no match prints this statement and repeat asking for input

def main():
    while True:
        print('\t\t\tWelcome to the interface') #prints statement
        user= str(input('Enter your login: '))# takes user input
        password = str(input('Enter your password: '))#takes user input
        login(user, password) #passes both arguments to teh login function

if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    main()
