import os
import webbrowser

p = input("What do you want to open? ").lower()

if "notepad" in p:
    os.system("notepad")
elif "chrome" in p:
    os.system("start chrome")
elif "email" in p or "gmail" in p:
    webbrowser.open("https://mail.google.com")
elif "vs code" in p or "vscode" in p:
    os.system('code')
elif "word" in p:
    os.system("start winword")
elif "jupyter" in p or "notebook" in p:
    os.system(
        r'start "" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Jupyter Notebook.lnk"')
else:
    print("Sorry, I can't open that right now.")
