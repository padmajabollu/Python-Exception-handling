"""
IN THIS PROGRAM DATA COLLECTED BY USER AND STORED IN DICTIONARY AND ALSO DEFINE 
MODULES FOR OPERATIONS.

"""
from PRNException import PRN
class Student(object): # START OF Student CLASS
    
    

    def __init__(self,prn, name, dob, email, contact): # CONSTRUCTOR CALLED WHEN OBJECT OF Student CLASS IS CREATED. USE FOR INITIALIZATION PURPOSE.
        # ATTRIBUTES
        self.prn = prn
        self.name = name
        self.dob = dob
        self.email = email
        self.contact = contact
    
    # DESTRUCTOR DELETES THE ALL OBJECTS BEFORE PROGRAM GET TERMINATE 
    def __del__(self):
        print("\nDestructor Called.")

    #string method for display object
    def __str__(self):
        return "\n"+self.prn+"\t        "+self.name+"\t    "+self.dob+"\t     "+self.email+\
        "\t      "+self.contact

    	    

    
    # GETTER AND SETTER METHODS FOR DISPLAYING AND ASSIGNING DATA TO ATTRIBUTES
    #FOR NAME
    @property
    def name(self):
        return self.__name 

    @name.setter
    def name(self,name):
        while True:
            try:
                if name.isnumeric()==False and name!="" and len(name)!=1: # VALIDTION OF INPUT
                    self.__name = name
                    break

                else:
                    raise Exception("\nError: Enter Valid Name : ")
                    
            except Exception as e:
                print(e)
                name=input()
                continue


    #FOR PRN
    @property
    def prn(self):
        return self.__prn

    @prn.setter
    def prn(self, prn):
        while True:
            try:
                    
            
                if len(prn) != 10 or prn.isnumeric() == False or prn == None: # VALIDTION OF INPUT
                    raise PRN(" Enter 10 DIGIT PRN Number")
                    
                else:
                    self.__prn = prn
                    break
                

            except PRN as e:
                print(e)
                prn = input()
                continue
      

    #FOR CONTACT
    @property
    def contact(self):
        return self.__contact
    
    @contact.setter        
    def contact(self, contact):
        while True:
            try:
                    
                if len(contact) != 10 or contact.isnumeric() == False or contact=="": # VALIDTION OF INPUT
                    raise Exception("\nError: Enter 10 DIGIT Contact Number : ")
                else:
                    self.__contact = contact
                    break

            except Exception as e:
                print(e)
                contact=input()
                continue
    #FOR EMAIL
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        while True:
            try:
                if email[-13:] != '@mitaoe.ac.in' or email==None: # VALIDTION OF INPUT
                    
                    raise Exception("\nEnter valid Mail ID like *********@mitaoe.ac.in : ")
                    
                else:
                    self.__email = email
                    break

            except Exception as e:
                print(e)
                email=input()
                continue

    # FOR DOB
    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self,dob):
        while True:
            try:
                if len(dob)==10 and dob!=None: # VALIDTION OF INPUT
                    self.__dob = dob
                    break
                    
                else:
                    raise Exception("\nEnter valid DOB like dd/mm-yyyy or dd-mm-yyyy : ")
            except Exception as e:
                print(e)
                dob=input()
                continue         

    #METHOD FOR DISPLAY RECORDS OF SLISTS           
    @staticmethod
    def display1(list):
        print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number")
        print("\n",list.prn,"\t    ",list.name,"\t",list.dob,"\t",list.email,"\t",list.contact)

class StudentData(object):

    deleted = 0 # USED FOR CALCULATE DELETED STUDENT OBJECTS
    
    last_roll=1 # USED AS A KEY IN DICTIONARY , ALSO USED TO CALCULATE NO OF STUDENTS
    slist = {} # DICTIONARY GETS CREATED
  
    # DECLARE ALL STATIC MODULES
    @staticmethod
    def addStudent(): # FOR ADDING STUDENT OBJECT TO DICTIONARY
        
        roll=StudentData.last_roll
        prn = input("\nEnter 10 Digit PRN Number : ")
        name = input("\nEnter the Name: ")
        dob = input("\nEnter valid DOB like dd/mm-yyyy or dd-mm-yyyy : ")
        email = input("\nEnter valid Mail id like *********@mitaoe.ac.in : ")
        contact = input("\nEnter the contact number: ")
        StudentData.slist[roll] = StudentData(prn,name,dob,email,contact) # OBJECT GETS CREATED
        StudentData.last_roll += 1
               
        
    @staticmethod
    def search(): # FOR SEARCH THE DATA IN DICTIONARY
        # MENUS ARE GIVEN FOR SEARCH
        print("\nSelect option:\n1. Search by Name\n2. Search by Contact Number")
        print("3. Search by PRN\n")
        opt = int(input())
        # SEARCH USING NAME
        if opt == 1:
            nm = input("\nEnter the name to search: ")
            ct = 1
            while ct == 1:
                for k,v in StudentData.slist.items():
                    
                    if StudeStudentDatant.slist[k].name == nm:
                        print("\nRoll Number\t     PRN\t       Name\t\tDOB\t\t\temail id\t\t    contact")
                        for k,v in StudentData.slist.items():
                            print("\n",k,"\t        ",v.prn,"\t     ",v.name,"\t    ",v.dob,"\t     ",v.email,"\t      ",v.contact)
                        ct = 0
                        break
                    else:
                        print("\nInvalid Input")
                        nm = input("\nEnter the Valid Name to search: ")
                        continue
                
        # SEARCH USING CONTACT NUMBER
        elif opt == 2:
            cn = (input("\nEnter the Contact Number to search: "))
            ct = 1
            while ct == 1:
                for k,v in StudentData.slist.items():
                    if StudentData.slist[k].contact == cn:
                        print("\nRoll Number\t     PRN\t       Name\t\tDOB\t\t\temail id\t\t    contact")
                        
                        for k,v in StudentData.slist.items():
                            print("\n",k,"\t        ",v.prn,"\t     ",v.name,"\t    ",v.dob,"\t     ",v.email,"\t      ",v.contact)
                        ct = 0
                        break
                    else:
                        
                        print("\nInvalid Input")
                        cn = (input("\nEnter the Contact Number to search: "))
                        continue
        
        # SEARCH USING PRN NUMBER

        elif opt == 3:
            pn = input("\nEnter the PRN to search: ")
            ct = 1
            while ct == 1:
                for k,v in StudentData.slist.items():
                    if StudentData.slist[k].prn == pn:
                        print("\nRoll Number\t     PRN\t       Name\t\tDOB\t\t\temail id\t\t    contact")
                        for k,v in StudentData.slist.items():
                            print("\n",k,"\t        ",v.prn,"\t     ",v.name,"\t    ",v.dob,"\t     ",v.email,"\t      ",v.contact)
                        ct = 0
                        break
                    else:
                        print("\nInvalid Input")
                        pn = input("\nEnter the PRN to search: ")
                        continue
        # EXECUTES IF SELECT THE CHOICE WHICH IS NOT GIVEN IN MENU
        else :
            print("\nWrong Choice.......")
    
   

    @staticmethod
    def delStudent(): # FOR DELETE THE DATA IN DICTIONARY
        # MENUS ARE GIVEN FOR DELETE
        print("Select option:\n1) Delete by name.\n2) Delete by Roll no.")
        print("3) Delete by PRN.\n4) Delete all.")
        opt = int(input())
        # DELETE USING NAME
        if opt == 1:
            nm = input("\nEnter the name to delete: ")
            ct = 1
        
            while ct == 1:
                for k, v in StudentData.slist.items():
                    com=v 
                    if StudentData.slist[k].name == nm:
                    
                        del StudentData.slist[k]
                        ct = 0
                        print("\nDELETED")
                        StudentData.deleted += 1
                        break
                    else:
                        pass
                        print("\nInvalid Input")
                        nm = input("\nEnter the name to delete: ")
           
        # DELETE USING ROLL NUMBER
        elif opt == 2:
            rl = int(input("\nEnter the Roll Number to delete: "))
            ct = 1
            while ct == 1:
                for k, v in StudentData.slist.items():
                    print(k)
                    if k == rl:
                        del StuStudentDatadent.slist[k]
                        print("\nDELETED")
                        ct = 0
                        StudentData.deleted += 1
                        break
                    else:
                        
                        print("\nERROR: This roll number dosen't exist.")
                        rl = int(input("\nEnter the Roll Number to delete: "))
        
        # DELETE USING PRN NUMBER
        elif opt == 3:
            pn = input("\Enter the PRN to delete: ")
            ct = 1
            while ct == 1:
                for k, v in StudentData.slist.items():
                   
                    if StudentData.slist[k].prn == pn:
                        del StudentData.slist[k]
                        print("\nDELETED")
                        StudentData.deleted += 1
                        ct=0
                        break
                    else:
                        pass
                        print("\nInvalid Input")
                        pn = input("\nEnter the PRN to delete: ")
        
        #DELETE ALL ENTRIES IN DICTIONARY
        elif opt == 4:
            StudentData.slist.clear()
            StudentData.deleted += 1
            print("\nDELETED")

        # EXECUTES IF SELECT THE CHOICE WHICH IS NOT GIVEN IN MENU
        else:
            print("\nWrong choice ............")
        
        print("\nNo of deleted entries : ",StudentData.deleted)

    @staticmethod
    
    def update(): # FOR UPDATE THE DATA IN DICTIONARY
        
        # MENUS ARE GIVEN FOR UPDATE
        print("\nSelect option:\n1. Update by Name\n2. Update by Contact Number")
        print("3. Update by PRN\n4. Update by mail id\n5. Update by Date of Birth \n")
        opt = int(input())

        
        # UPDATE USING NAME
        if opt == 1:
            nm = input("\nEnter the name : ")
            ct = 1
            while ct == 1:
                r=int(input("\nEnter Roll Number to be Updated : "))
                    
                for k,v in StudentData.slist.items():
                    if r==k:
                        
                        if StudentData.slist[k].name == nm:
                            s = StudentData.slist[k]
                            s.name = input("\nEnter Name to Update : ")
                            ct = 0
                            break
                        else:
                            print("\nInvalid Input")
                            nm = input("\nEnter the Valid Name to update: ")
                            continue
                    
        # UPDATE USING CONTACT NUMBER
        elif opt == 2:
            r=int(input("\nEnter Roll Number to be Updated : "))
                    
            cn = (input("\nEnter the Contact Number : "))
            ct = 1
            while ct == 1:
                for k,v in StudentData.slist.items():
                    if r==k:
                        if StudentData.slist[k].contact == cn:
                            s = StudentData.slist[k]
                            s.contact = input("\nEnter Contact Number to update: ")
                            ct = 0
                            break
                        else:
                            
                            print("\nInvalid Input")
                            cn = (input("\nEnter the Contact Number to update: "))
                            continue
            
        # UPDATE USING PRN NUMBER

        elif opt == 3:
            r=int(input("\nEnter Roll Number to be Updated : "))
                    
            pn = input("\nEnter the PRN : ")
            ct = 1
            while ct == 1:
                for k,v in StudentData.slist.items():
                    if r==k:
                        if StudentData.slist[k].prn == pn:
                            s = StudentData.slist[k]
                            s.prn = input("\nEnter prn to update: ")
                            ct = 0
                            break
                        else:
                            print("\nInvalid Input")
                            prn = input("\nEnter the PRN to update: ")
                            continue
        # UPDATE USING Mail ID NUMBER
        elif opt == 4:
            r=int(input("\nEnter Roll Number to be Updated : "))
                    
            e = input("\nEnter the Mail ID : ")
            ct = 1
            while ct == 1:
                for k,v in StudentData.slist.items():
                    if r==k:
                        if StudentData.slist[k].email == e:
                            s = StudentData.slist[k]
                            s.email = input("\nEnter Mail to update: ")
                            ct = 0
                            break
                        else:
                            print("\nInvalid Input")
                            prn = input("\nEnter the Mail to update: ")
                            continue
        # UPDATE USING DATE OF BIRTH NUMBER
        elif opt == 5:
            r=int(input("\nEnter Roll Number to be Updated : "))
                   
            d  = input("\nEnter the Date of Birth : ")
            ct = 1
            while ct == 1:
                for k,v in StudentData.slist.items():
                    if r==k:

                        if StudentData.slist[k].dob == d :
                            s = StudentData.slist[k]
                            s.dob = input("\nEnter Date of Birth to update: ")
                            ct = 0
                            break
                        else:
                            print("\nInvalid Input")
                            d = input("\nEnter the Date of Birth to update: ")
                            continue
        # EXECUTES IF SELECT THE CHOICE WHICH IS NOT GIVEN IN MENU
        else :
            print("\nWrong Choice.......")
            
                        
            
    @staticmethod
    def display(): # FOR DISPLAY STUDENT DATA
        print("\nRoll Number\t     PRN\t       Name\t\tDOB\t\t\temail id\t\t    contact")
        for k,v in StudentData.slist.items():
            Student.display1(v)
            print("\n",k,"\t        ",v.prn,"\t     ",v.name,"\t    ",v.dob,"\t     ",v.email,"\t      ",v.contact)

                        
    @staticmethod
    def count(): # FOR COUNTING TOTAL NUMBER OF STUDENT
        print("\nTotal number of students: {}".format(StudentData.last_roll-1))
    
    # END OF Student CLASS
              
def main():
    pass # USE WHEN NOTHING NEED TO WRITE 

if __name__ == "__main__": 
    main() # CALL TO MAIN MODULE
