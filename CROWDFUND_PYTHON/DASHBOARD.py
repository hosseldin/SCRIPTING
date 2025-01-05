# Hossam Mahmoud
# Creating a Crowd Funding Application

from SIGN_UP_API import *
from SIGN_IN_API import *
from CREATE_PROJECT_API import *

def dashboardMsg():
    print("\nHosa Crowd Funding App\nDashboard")

def showMainMenu():
    print("\nMENU:")
    print("1. Create a Project")
    print("2. View Project")
    print("3. Edit Project")
    print("4. Delete Project")
    print("5. Search")
    print("6. Back to Main Menu")

def userDashboard(userData):
    menuItems = []  # List to store items
    while True:
        showMainMenu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print("\nYou'll be directed to setup your project...")
            projectMsg()
            createProject(userData)
            
        elif choice == '2':
            print("\nView your Projects...")
            projectMsg()
            createProject(userData)
            
        elif choice == '3':
            print("\nEdit a Project...")
            projectMsg()
            createProject(userData)
            
        elif choice == '4':
            print("\nDelete a Project...")
            projectMsg()
            createProject(userData)
            
        elif choice == '5':
            print("\nSearch for a Project...")
            projectMsg()
            createProject(userData)
            
        elif choice == '6':
            print("\nHeading back to the Main Menu...")
            signInMsg()
            signInAPI()
        else:
            print("\nInvalid Choice")

# Run the program
# dashboardMsg()
# userDashboard(userData)