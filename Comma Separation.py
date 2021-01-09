import pyperclip, sys

try:
    option = sys.argv[1]
except:
    option = None
    
lines = pyperclip.paste().split()
new_list = [li for li in lines if "@" in li]
new_list = [li for li in new_list if "@name.com" not in li]

if option == "-c" or option is None: #default
    pyperclip.copy(", ".join(new_list))
elif option == "-n":
    pyperclip.copy("\n".join(new_list))
else:
    raise Exception("choose -c for comma separation or -n for new line separation. ")
