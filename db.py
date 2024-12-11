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
