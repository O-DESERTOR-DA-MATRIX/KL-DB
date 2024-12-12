import sys  # Para adicionar o caminho da área de trabalho ao path
import os   # Para manipular caminhos de arquivos



# Importa o banco de dados de comandos
from db import commands

def main_menu():
    while True:
        print("\nSelect the operating system:")
        print("1. Linux")
        print("2. Windows")
        print("E. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            os_menu("linux")
        elif choice == "2":
            os_menu("windows")
        elif choice.upper() == "E":
            print("Exiting...")
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
    print(f"\nSelected command: {command['description']} \n")

    # Display commands for the selected OS
    if os_type == "linux":
        if 'bash' in command:
            print(f"🔴 Bash: {command['bash']} \n")
        if 'bash_alt' in command:
            print(f"🔴 Bash (alternative): {command['bash_alt']} \n")
        if 'bash_extra' in command:
            print(f"🔴 Bash (extra): {command['bash_extra']} \n")
        if 'bash_another' in command:
            print(f"🔴 Bash (another): {command['bash_another']} \n")
        if 'bash_final' in command:
            print(f"🔴 Bash (final): {command['bash_final']} \n")

    elif os_type == "windows":
        if 'cmd' in command:
            print(f"🔵 CMD: {command['cmd']} \n")
        if 'powershell' in command:
            print(f"🔵 PowerShell: {command['powershell']} \n")

    # Next action
    while True:
        print("\nWhat would you like to do next?")
        print("1. Return to the OS menu")
        print("2. Return to the main menu")
        print("3. Exit")

        next_choice = input("\nEnter your choice: ").strip()

        if next_choice == "1":
            os_menu(os_type)
            break
        elif next_choice == "2":
            main_menu()
            break
        elif next_choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the tool
main_menu()
