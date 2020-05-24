import pyperclip


lines = pyperclip.paste().splitlines() 
new_list = [li for li in lines if li !=""]

pyperclip.copy(", ".join(new_list))
