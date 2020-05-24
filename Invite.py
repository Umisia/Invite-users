import pyperclip
import time
import keyboard

print("Press Ctrl+C to interrupt. \n\n")

clipboard = pyperclip.paste()
lines = clipboard.splitlines() 

if clipboard == "":
    print("Clipboard empty. Press Enter to close.")
    #input()
else:
    for line in lines:
        time.sleep(1)

        if line != "":
            if "owner" in line.lower():
                account_type = "Owner"
            elif "admin" in line.lower():
                account_type = "Admin"
            else:
                account_type = "Editor"            
            for element in line.split():
                if "@" in element:
                    email_address = element  
                    print("Invite ", email_address, " as ", account_type)                
                    pyperclip.copy(email_address) 
                    time.sleep(1)
                    keyboard.wait("ctrl+v")
                    print("\n")
                    break
            else:
                print("No email address found in: ", line, ". Skipped!")
    else:
        print("List ended. Press Enter to close")
        pyperclip.copy("")
        #input()

    
