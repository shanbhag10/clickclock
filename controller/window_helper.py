from AppKit import NSWorkspace

def get_current_window():
    active_app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    return active_app_name
