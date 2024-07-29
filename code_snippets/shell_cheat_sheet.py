def shell_cheat_sheet():
    print(colored("S H E L L  C H E A T  S H E E T  M E N U", attrs=["bold"]))
    print(colored("WINDOWS COMMANDS", "blue", attrs=['bold', 'dark']))

    win = {
        "ipconfig": "Enumerate network configuration",
        "tasklist": "List all running processes",
        "systeminfo": "Display detailed system information",
        "netstat -an": "Display all active connections and listening ports",
        "whoami": "Display the current user",
        "net user": "List all user accounts",
        "net localgroup": "List all local groups",
        "sc query": "Display the status of services",
        "dir": "List directory contents",
        "attrib": "Display or change file attributes"
    }
    for cmd, desc in win.items():
        print(f"> {cmd:<20} - {desc}")

    print("\n\t\t    >-------------<")
    
    print(colored('LINUX COMMANDS', 'blue', attrs=['bold', 'dark']))
    lin = {
        "ifconfig": "Enumerate network configuration",
        "ps aux": "List all running processes",
        "uname -a": "Display detailed system information",
        "netstat -an": "Display all active connections and listening ports",
        "whoami": "Display the current user",
        "cat /etc/passwd": "List all user accounts",
        "cat /etc/group": "List all groups",
        "systemctl status": "Display the status of services",
        "ls -la": "List directory contents",
        "chmod": "Change file permissions"
    }
    for cmd, desc in lin.items():
        print(f"> {cmd:<20} - {desc}")
