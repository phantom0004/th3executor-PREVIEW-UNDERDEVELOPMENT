def linux_sys_info():
    output = []
    system_info = {
        "Hostname": process_command("hostname"),
        "OS Name": process_command("cat /etc/os-release | grep PRETTY_NAME | cut -d '=' -f2- | tr -d '\"'"),
        "OS Version": process_command("lsb_release -r | cut -f2"),
        "System Manufacturer": process_command("cat /sys/devices/virtual/dmi/id/sys_vendor"),
        "Kernel Version": process_command("uname -r"),
        "Domain": process_command("domainname"),
        "Logon Server": process_command("echo $SSH_CONNECTION | awk '{print $3}'"),
        "IP Address": process_command("hostname -I"),
        "Shell Used": process_command("printenv")
    }

    for key, value in system_info.items():
        if "Permission denied" in value:
            value = "Requires Sudo Privileges"
        elif "Error" in value or not value:
            value = "Unable to Extract Detail"
        
        if key == "Shell Used":
            shell_value = re.search(r"(?<=SHELL=)[^\s]+", value)
            if shell_value:
                value = shell_value.group(0)
                    
        output.append(f"{key}: {value}")
    
    if isinstance(output, list):
        return output
    else:
        return "no_information"
