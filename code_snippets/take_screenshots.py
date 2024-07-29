def take_screenshot(conn_obj):
    screenshot = ImageGrab.grab()
    screenshot_buffer = io.BytesIO()
    screenshot.save(screenshot_buffer, format='PNG')
    screenshot_data = screenshot_buffer.getvalue()

    data_size = len(screenshot_data)
    conn_obj.sendall(str(data_size).encode() + b'\n')

    return screenshot_data 
