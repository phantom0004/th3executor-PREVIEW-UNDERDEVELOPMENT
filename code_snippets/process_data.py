def process_and_check_recieved_data(received_data, data_size):
    if isinstance(data_size, str):
        log_activity(f"Supposed to recieve the data size but got type 'str' instead, output : {data_size}", "error")
        return (f"[-] Error when getting file data {data_size}. Please try again.") # An error occured, print it
    
    # Check data integrity
    if len(received_data) != data_size:
        log_activity(f"Received data size ({len(received_data)}) does not match the expected size ({data_size}).", "error")
        return "Received data size does not match the expected size."
    
    # If all data is received properly, process it
    decrypted_data = decrypt_message(received_data)
    if decrypted_data is None:
        log_activity("Failed to decrypt screenshot or else data is corrupted. Try again in a little moment.", "error")
        return "Data is corrupted or else is in an invalid format"
    
    return decrypted_data
