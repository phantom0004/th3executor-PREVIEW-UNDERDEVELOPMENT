if not shutdown_signal or shutdown_signal == "connection_not_closed":
    print(colored("[-] Target did not terminate the connection on their end", "red"))
    print(colored("[!] This can be due to a network problem, please wait a few moments before re-connecting", "yellow"))
    
    log_activity("Exited th3executor, connection was not terminated on targets end.", "error")
elif shutdown_signal == "shutdown_confirmed":
    print(colored("[+] Connection terminated successfully on targets end", "green"))
    
    log_activity("Exited th3executor, connection terminated normally between both parties.", "info")
else:
    print(colored("[-] Unknown shutdown code retireved, unable to parse output. Connection is probably still open", "red"))
    print(colored("[!] This can be due to a network problem, please wait a few moments before re-connecting", "yellow"))
    
    log_activity("Unknown shutdown code retireved, unable to parse output. Connection is probably still open.", "error")
