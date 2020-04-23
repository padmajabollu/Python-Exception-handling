#ALL NECCESSARY PACKAGES ARE IMPORTED 
from PRNException import PRN

import operator
from ass7submodule import Student
from operator import itemgetter
from collections import OrderedDict
from FileHandling import *

class Marks(Student):#inherited the Student class
    #constructor
    def __init__(self, prn, name, dob, email, contact, marks):
        Student.__init__(self, prn, name, dob, email, contact)#call to base class constructor
        self.marks = marks
    #destructor
    def __del__(self):
        print("\nDestructor Called")
    #string method for display object
    def __str__(self):
        return Student.__str__(self)+"\t    "+str(self.marks["OOT"])+"\t     "+str(self.marks["ME"])\
        +"\t      "+str(self.marks["EI"])
    #getter and setter methods
    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks):
        try:

            if isinstance(marks,dict):
                self.__marks = marks
                
            else:
                raise TypeError("Invalid Object is passed")

        except TypeError:
            print(TypeError)

    #override the display method
    @staticmethod
    def display1(list):
        grade=""
        
        per=((int(list[5])+int(list[6])+int(list[7]))*100)/300
        if per<=100 and per>=75:
            grade="A"
        elif per<=74 and per>=65:
            grade="B"
        elif per<=64 and per>=55:
            grade="C"
        elif per<=54 and per>=45:
            grade="D"
        elif per<=44 and per>0:
            grade="F"
        else:
            pass
                
        print("\n",list[0],"\t    ",list[1],"\t",list[2],"\t",list[3],"\t",list[4],"\t",\
        list[5],"\t",list[6],"\t ",list[7],"\t",per,"\t",grade)

#methods are defined in MarksData class
class MarksData(object):
    slist = {} # DICTIONARY GETS CREATED
    Delete=0 #TO CALCULATE TOTAL DELETED RECORDS
    Topper={}#TO STORE PERCENTAGE WITH PRN AS KEY
    Total=0
    # static methods 
    @staticmethod

    def addRecord_inslist():
        #file handling to store the data
        file=filehandling("StudentData.txt")
        data=file.readData()
        for i in data:
            mainData=i.strip("\n").split(",")
            ms = {'OOT':int(mainData[5]),'ME':int(mainData[6]),'EI':int(mainData[7])}   
            MarksData.slist[mainData[0]]=Marks(mainData[0],mainData[1],mainData[2],mainData[3]\
            ,mainData[4],\
            ms)
        

    @staticmethod

    def addStudent():
        
        prn = input("\nEnter PRN: ")
        name = input("\nEnter the name: ")
        dob = input("\nEnter Date of Birth: ")
        email = input("\nEnter your email id: ")
        contact = input("\nEnter the contact number: ")
        ms = {'OOT':0,'ME':0,'EI':0}   
        for k,v in ms.items():
           while True:
            try:
                    m= int(input("\n{}:".format(k)))
                    if m>0 and m<=100 and m!=None :
                        ms[k]= m  
                        break  
                    else:
                        continue

            except ValueError as e:
                    print("\nEnter Integer Number only .......")   
                    continue       
        f=0
        for i,j in MarksData.slist.items():
            if j.prn==prn:
                f=1
                break
            else:
                f=0
                continue

        if f==0:

            MarksData.slist[prn]=Marks(prn,name,dob,email,contact,ms)
            MarksData.Total+=1
            #file handling to store the data
            file=filehandling("StudentData.txt")
            open=file.openFile("w")
            for i,j in MarksData.slist.items():
                data=j.prn+","+j.name+","+j.dob+","+j.email+","+j.contact+","+str(j.marks["OOT"])+","+str(j.marks["ME"])\
                +","+str(j.marks["EI"])+","+"\n"
                file.writeData(data)

        else:
            print("\nDuplicate Entry")
            print("\n You want to override, if yes then press Y else N")
            ch=input()
            if ch=="Y":
                MarksData.slist[prn]=Marks(prn,name,dob,email,contact,ms)
                #file handling to store the data
                file=filehandling("StudentData.txt")
                open=file.openFile("w")
                for i,j in MarksData.slist.items():
                    data=j.prn+","+j.name+","+j.dob+","+j.email+","+j.contact+","+str(j.marks["OOT"])+","+str(j.marks["ME"])\
                    +","+str(j.marks["EI"])+","+"\n"
                    file.writeData(data)

            else:
                print(MarksData.slist[prn])
                
        
        

         
        
    @staticmethod

    def update():
        while True:
            print("\n1.Update by PRN\n2.exit")
            ch=int(input())
            if ch==1:
                
                prn=input("\nEnter PRN to Update the marks : ")
                while True:
                    try:
                            
                    
                        if len(prn) != 10 or prn.isnumeric() == False or prn == None: # VALIDTION OF INPUT
                            raise PRN(" Enter 10 DIGIT PRN Number")
                            
                        else:
                            prn = prn
                            break
                        

                    except PRN as e:
                        print(e)
                        prn = input()
                        continue
                for k,v in MarksData.slist.items():
                    
                    if k==prn:
                        sub=(input("\nEnter subject for Update : "))
                        mar=int(input("\nEnter Marks : "))
                        v.marks[sub]=mar
                        print("\nRecord Successfully Updated")
                        
                        break
                    else:
                        continue
                    print("\nInvalid PRN")


                
            elif ch==2:
                break
            
            else :
                print("\nWrong Choice.......")
                #file handling to store the data
        file=filehandling("StudentData.txt")
    
        open=file.openFile("w")
        for i,j in MarksData.slist.items():
            data=j.prn+","+j.name+","+j.dob+","+j.email+","+j.contact+","+str(j.marks["OOT"])+","+str(j.marks["ME"])\
            +","+str(j.marks["EI"])+","+"\n"
            file.writeData(data)

            
        
    @staticmethod

    def search():
        while True:
            print("\n1.Search by PRN\n2.exit")
            ch=int(input())
            if ch==1:
                
                p=input("\nEnter PRN to Search the marks : ")
                for k,v in MarksData.slist.items():
                    
                    if k==p:
                        print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number \t OOT\t ME\t\t EI")

                        print("\n",k,"\t    ",v.name,"\t",v.dob,"\t",v.email,"\t",v.contact,"\t",v.marks['OOT'],"\t",v.marks['ME'],"\t",v.marks['EI'])
                        break
                    else:
                        continue
                    print("\nInvalid PRN")


                
            elif ch==2:
                break
            
            else :
                print("\nWrong Choice.......")

    
    @staticmethod

    def delete():

        while True:
            print("\n1.Delete by PRN\n2.exit")
            ch=int(input())
            if ch==1:
                
                prn=input("\nEnter PRN to Delete the Entry : ")
                while True:
                    try:
                            
                    
                        if len(prn) != 10 or prn.isnumeric() == False or prn == None: # VALIDTION OF INPUT
                            raise PRN(" Enter 10 DIGIT PRN Number")
                            
                        else:
                            prn = prn
                            break
                        

                    except PRN as e:
                        print(e)
                        prn = input()
                        continue
                for k,v in MarksData.slist.items():
                    
                    if k==prn:
                        del MarksData.slist[k]
                        print("\nRecord Successfully Deleted")
                        MarksData.Delete+=1
                        break
                    else:
                        continue
                    print("\nInvalid PRN")


                
            elif ch==2:
                break
            
            else :
                print("\nWrong Choice.......")
        print("\nTotal entries Deleted : {}".format(MarksData.Delete))
        #file handling to store the data
        file=filehandling("StudentData.txt")

        open=file.openFile("w")
        for i,j in MarksData.slist.items():
            data=j.prn+","+j.name+","+j.dob+","+j.email+","+j.contact+","+str(j.marks["OOT"])+","+str(j.marks["ME"])\
            +","+str(j.marks["EI"])+","+"\n"
            file.writeData(data)
    
    @staticmethod

    def noofentries():
        total=0
        for i,j in MarksData.slist.items():
            total+=1

        print("\nTotal Entries : {}".format(total)) 
    

    @staticmethod

    def display():
        
        print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number \t OOT\t ME\t\t EI\tPercentage\tGrade")
        #file handling to store the data
        file=filehandling("StudentData.txt")
        data=file.readData()
        for i in data:
            mainData=i.strip("\n").split(",")
            Marks.display1(mainData)
        
                
    @staticmethod

    def topper():
        
        print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number \t OOT\t ME\t\t EI\tPercentage\tGrade")
        i=0
        for k,v in MarksData.slist.items():
            per=((v.marks['OOT']+v.marks['ME']+v.marks['EI'])*100)/300
            MarksData.Topper[k]=per   
        sorted_x = sorted(MarksData.Topper.items(), key=itemgetter(1),reverse=True)
        for k in sorted_x:
            if i==0:
                
                for a,b in MarksData.Topper.items():
                    if a==k[0]:
                        for p,q in MarksData.slist.items():
                            if p==a :
                                if b<=100 and b>=75:
                                    grade="A"
                                elif b<=74 and b>=65:
                                    grade="B"
                                elif b<=64 and b>=55:
                                    grade="C"
                                elif b<=54 and b>=45:
                                    grade="D"
                                elif b<=44 and b>0:
                                    grade="F"
                                else:
                                    grade=""

                                if (q.marks['OOT']>=40) and (q.marks['ME']>=40) and (q.marks['EI']>=40):
                                    
                    
                                    print("\n",p,"\t    ",q.name,"\t",q.dob,"\t",q.email,"\t",q.contact,"\t",q.marks['OOT'],"\t",q.marks['ME'],"\t",q.marks['EI'],"\t",b,grade) 
                                    i+=1
                                    break
                            else:
                                continue
           

    @staticmethod

    def threetopper():
        i=1
        for k,v in MarksData.slist.items():
            per=((v.marks['OOT']+v.marks['ME']+v.marks['EI'])*100)/300
            MarksData.Topper[k]=per   
        sorted_x = sorted(MarksData.Topper.items(), key=itemgetter(1),reverse=True)
        #print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number \t OOT\t ME\t\t EI\tPercentage")
        print("\n PRN    \t     Name\tDate of Birth\t   Email ID\t      Contact Number \t OOT\t ME\t\t EI\tPercentage\tGrade")

        for k in sorted_x:
            if i!=4:
                
                for a,b in MarksData.Topper.items():
                    if a==k[0]:

                        for p,q in MarksData.slist.items():
                            if p==a :
                                if b<=100 and b>=75:
                                    grade="A"
                                elif b<=74 and b>=65:
                                    grade="B"
                                elif b<=64 and b>=55:
                                    grade="C"
                                elif b<=54 and b>=45:
                                    grade="D"
                                elif b<=44 and b>0:
                                    grade="F"
                                else:
                                    grade=""

                                
                                #for k,v in MarksData.slist.items():
                                if (q.marks['OOT']>=40) and (q.marks['ME']>=40) and (q.marks['EI']>=40):
                                                
                                    print("\n",p,"\t    ",q.name,"\t",q.dob,"\t",q.email,"\t",q.contact,"\t",q.marks['OOT'],"\t",q.marks['ME'],"\t",q.marks['EI'],"\t",b,"\t",grade) 
                                    i+=1
                                    break
                                else:
                                    continue
                

