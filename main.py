commands = {
    "linux": {
        "1": {
            "description": "User and group enumeration",
            "bash": "cat /etc/passwd",
            "bash_alt": "cat /etc/group"
        },
        "2": {
            "description": "File permission enumeration",
            "bash": "ls -l /path/to/directory",
            "bash_alt": "find / -type f -exec ls -l {} \\\""
        },
        "3": {
            "description": "Sudoers configuration",
            "bash": "cat /etc/sudoers",
            "bash_alt": "sudo -l"
        },
        "4": {
            "description": "Kernel information",
            "bash": "uname -r",
            "bash_alt": "dmesg | grep -i 'vulner'"
        },
        "5": {
            "description": "Services and processes",
            "bash": "ps aux",
            "bash_alt": "systemctl list-units --type=service",
            "bash_extra": "netstat -tuln"
        },
        "6": {
            "description": "Vulnerable modules and packages",
            "bash": "lsmod",
            "bash_alt": "dpkg -l",
            "bash_extra": "rpm -qa",
            "bash_another": "apt list --upgradable"
        },
        "7": {
            "description": "SUID/SGID files",
            "bash": "find / -type f -perm /4000",
            "bash_alt": "find / -type f -perm /2000"
        },
        "8": {
            "description": "Configuration files and passwords",
            "bash": "cat /etc/passwd",
            "bash_alt": "cat /etc/shadow",
            "bash_extra": "cat /etc/sudoers"
        },
        "9": {
            "description": "Network interfaces and services",
            "bash": "ifconfig",
            "bash_alt": "ip a",
            "bash_extra": "route -n",
            "bash_another": "netstat -tuln",
            "bash_final": "nmap"
        },
        "10": {
            "description": "Logs and command history",
            "bash": "cat /var/log/auth.log",
            "bash_alt": "cat /var/log/syslog",
            "bash_extra": "history"
        },
        "11": {
            "description": "Cron jobs and scheduled tasks",
            "bash": "crontab -l",
            "bash_alt": "ls -la /etc/cron*",
            "bash_extra": "cat /etc/crontab"
        },
        "12": {
            "description": "Software vulnerabilities",
            "bash": "searchsploit <software>",
            "bash_alt": "apt-cache search <software>",
            "bash_extra": "rpm -q --changelog <package>"
        },
        "13": {
            "description": "User capabilities",
            "bash": "getcap -r / -v",
            "bash_alt": "capsh --print"
        }
    },
    "windows": {
        "1": {
            "description": "User information",
            "cmd": "net user",
            "powershell": "Get-LocalUser | ft Name,Enabled,Description,LastLogon"
        },
        "2": {
            "description": "List running processes",
            "cmd": "tasklist",
            "powershell": "Get-Process | ft Name,ID,CPU"
        },
        "3": {
            "description": "Check system info",
            "cmd": "systeminfo",
            "powershell": "Get-ComputerInfo"
        },
        "4": {
            "description": "List services",
            "cmd": "net start",
            "powershell": "Get-Service | ft Name,Status"
        },
        "5": {
            "description": "List network configurations",
            "cmd": "ipconfig",
            "powershell": "Get-NetIPAddress | ft IPAddress,InterfaceAlias"
        },
        "6": {
            "description": "List open ports",
            "cmd": "netstat -an",
            "powershell": "Get-NetTCPConnection | ft LocalAddress,LocalPort,State"
        },
        "7": {
            "description": "Scheduled tasks",
            "cmd": "schtasks",
            "powershell": "Get-ScheduledTask | ft TaskName,State"
        },
        "8": {
            "description": "System logs",
            "cmd": "eventvwr",
            "powershell": "Get-WinEvent -LogName 'System' | select TimeCreated,Message -First 10"
        },
        "9": {
            "description": "Installed programs",
            "cmd": "wmic product get name",
            "powershell": "Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | select DisplayName"
        },
        "10": {
            "description": "Environment variables",
            "cmd": "set",
            "powershell": "Get-ChildItem Env:"
        },
        "11": {
            "description": "Check firewall rules",
            "cmd": "netsh advfirewall show allprofiles",
            "powershell": "Get-NetFirewallRule | ft DisplayName,Enabled,Action"
        },
        "12": {
            "description": "List drivers",
            "cmd": "driverquery",
            "powershell": "Get-WmiObject Win32_PnPSignedDriver | select DeviceName,DriverVersion"
        }
    }
}

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

        choice = input("Enter the number of your choice: ").strip()

        if choice in commands[os_type]:
            show_commands(os_type, choice)
        elif choice.upper() == "E":
            break
        else:
            print("Invalid choice. Try again.")

def show_commands(os_type, choice):
    command = commands[os_type][choice]
    print(f"\nSelected command: {command['description']}")

    # Display commands for the selected OS
    if os_type == "linux":
        if 'bash' in command:
            print(f"🔴 Bash: {command['bash']}")
        if 'bash_alt' in command:
            print(f"🔴 Bash (alternative): {command['bash_alt']}")
        if 'bash_extra' in command:
            print(f"🔴 Bash (extra): {command['bash_extra']}")
        if 'bash_another' in command:
            print(f"🔴 Bash (another): {command['bash_another']}")
        if 'bash_final' in command:
            print(f"🔴 Bash (final): {command['bash_final']}")

    elif os_type == "windows":
        if 'cmd' in command:
            print(f"🔵 CMD: {command['cmd']}")
        if 'powershell' in command:
            print(f"🔵 PowerShell: {command['powershell']}")

    # Next action
    while True:
        print("\nWhat would you like to do next?")
        print("1. Return to the OS menu")
        print("2. Return to the main menu")
        print("3. Exit")

        next_choice = input("Enter your choice: ").strip()

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
