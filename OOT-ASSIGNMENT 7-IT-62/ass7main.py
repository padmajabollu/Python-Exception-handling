"""
DOCSTRING
THIS IS MAIN APPLICATION ,IN WHICH MENU IS GIVEN FOR USER . USER SELECT ONE CHOICE, 
THEN MODULE CALL IS DONE ACCORDING TO  USER SELECTION

"""
from Mark import * # IMPORT THE ASS2SUBMODULE PROGRAM WHICH CONTAINS CODE FOR OPERATIONS

   
def main(): # START OF MAIN MODULE
    MarksData.addRecord_inslist()
    choice=0
    while True: # START OF WHILE LOOP
        print("\n")
        print("Select the option: \n")
        print("1. Add") 
        print("2. Update")
        print("3. Display")
        print("4. Search")
        print("5. Delete")
        print("6. Total Number of Entries")
        print("7. Topper Student of the class")
        print("8. Three Topper Students of the class")
        print("9. Exit\n")
        choice = int(input())
        
        # CHOICE SELECTED BY USER WILL BE COMPARE AND CALL MODULE ACCORDINGLY
        if choice == 1:
            MarksData.addStudent()
        elif choice == 2:
            MarksData.update()
        elif choice == 3:
            MarksData.display()   
        elif choice == 4:
            MarksData.search()   
        elif choice == 5:
            MarksData.delete()   
        elif choice == 6:
            MarksData.noofentries()          
        elif choice == 7:
            MarksData.topper() 
        elif choice == 8:
            MarksData.threetopper()           
        elif choice == 9:
            break
        else:
            print("\nWrong Choice choosed.........") # EXECUTE WHEN USER SELECT THE OTHER OPTION WHICH IS NOT GIVEN IN MENU
    # END OF WHILE LOOP




main() # CALL TO MAIN MODULE