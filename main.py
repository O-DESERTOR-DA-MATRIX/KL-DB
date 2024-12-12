import sys  # Para adicionar o caminho da área de trabalho ao path
import os   # Para manipular caminhos de arquivos

# Importa o banco de dados de comandos
from db import commands

def main_menu():
    while True:
        print("\nSelect the operating system:")
        print("1. Linux")
        print("2. Windows")
        print("3. Nmap")
        print("4. test")        
        print("E. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            os_menu("linux")
        elif choice == "2":
            os_menu("windows")
        elif choice == "3":
            os_menu("nmap")    
            os_menu("windows")
        elif choice == "4":
            os_menu("test")                      
        elif choice.upper() == "E":
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def os_menu(os_type):
    while True:
        print(f"\nCommands for {os_type.capitalize()}:")
        for key, value in commands[os_type].items():
            print(f"{key}. {value['description']}")
        print("E. Return to main menu")

        choice = input("\nEnter the number of your choice: ").strip()

        if choice in commands[os_type]:
            show_commands(os_type, choice)
        elif choice.upper() == "E":
            break
        else:
            print("Invalid choice. Try again.")

def show_commands(os_type, choice):
    command = commands[os_type][choice]
    print(f"\nSelected command: {command['description']}\n")

    # Display commands dynamically based on the keys present
    for key, value in command.items():
        if key == "description":
            continue
        if os_type == "linux":
            print(f"🔴 Bash ({key.capitalize()}): {value} \n")  # Red
        elif os_type == "windows":
            print(f"🔵 {key.capitalize()}: {value} \n")  # Blue
        elif os_type == "nmap":
            print(f"⚪ {key.capitalize()}: {value} \n")  # White
        elif os_type == "test":
            print(f"⚪ {key.capitalize()}: {value} \n")  # White            

    # Next action
    while True:
        print("\nWhat would you like to do next?")
        print("1. Return to the OS menu")
        print("2. Return to the main menu")
        print("3. Exit")

        next_choice = input("\nEnter your choice: ").strip()

        if next_choice == "1":
            break  # Return to OS menu
        elif next_choice == "2":
            main_menu()
            return  # Exit this function to restart the main menu
        elif next_choice == "3":
            print("Exiting the tool. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

# Run the tool
if __name__ == "__main__":
    main_menu()
