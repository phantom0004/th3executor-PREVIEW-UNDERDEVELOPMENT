def windows_sys_info():
    try:
        system_info_output = process_command("systeminfo")
        if "Error" in system_info_output:
            raise ValueError()
    except:
        return "no_information"
    
    output = []
    patterns = {
        'Hostname': r"Host Name:\s+([^\r\n]+)",
        'OS Name': r"OS Name:\s+([^\r\n]+)",
        'OS Version': r"OS Version:\s+([^\r\n]+)",
        'OS Manufacturer': r"OS Manufacturer:\s+([^\r\n]+)",
        'Registered Owner': r"Registered Owner:\s+([^\r\n]+)",
        'Registered Organization': r"Registered Organization:\s+([^\r\n]+)",
        'System Manufacturer': r"System Manufacturer:\s+([^\r\n]+)",
        'System Directory': r"System Directory:\s+([^\r\n]+)",
        'Domain': r"Domain:\s+([^\r\n]+)",
        'Logon Server': r"Logon Server:\s+\\\\([^\r\n]+)",
        'IP Address': r"IP address\(es\)\s+[^:]+:\s+([0-9]{1,3}(?:\.[0-9]{1,3}){3})"
    }

    for key, value in patterns.items():
        system_output = re.search(value, system_info_output, re.MULTILINE)
        if system_output:
            output.append(f"{key}: {system_output.group(1)}")
        else:
            output.append(f"No information found for {key}")
    
    if not isinstance(output,list):
        return "no_information"
    else:
        return output 
