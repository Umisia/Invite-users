import pyperclip, sys

try:
    option = sys.argv[1]
except:
    option = None
    
lines = pyperclip.paste().replace('(', ' (').split()

new_list = [li for li in lines if "@" in li]
new_list = [li for li in new_list if "@name.com" not in li]
new_list2 = []
for el in new_list:
    el = el.replace("<","").replace(">","")
    if ")" in el:
        el= el[el.index(")")+1:]
        new_list2.append(el)
    else:
        new_list2.append(el)

if option == "c" or option is None: #default
    pyperclip.copy(", ".join(new_list2).replace(',,', ','))
elif option == "n":
    pyperclip.copy("\n".join(new_list2).replace(',,', ',').replace(',', ''))
else:
    raise Exception("choose c for comma separation or n for new line separation. ")


