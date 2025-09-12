import winreg
import sys

try: 
    # Open the box where Windows keeps its name and version
    box = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")


# Peek inside and read notes
    name, _ = winreg.QueryValueEx(box, "ProductName")
    version, _ = winreg.QueryValueEx(box, "CurrentVersion")
    build, _ = winreg.QueryValueEx(box, "CurrentBuild")


    print("Hello! Here is your Windows info:")
    print(f" Name: {name}")
    print(f" Version: {version}")
    print(f" Build: {build}")

    winreg.CloseKey(box)


except PermissionError: 
    print("I can't open the box. Try running info me as an Administratior.")
    sys.exit(1)

except Exception as e: 
    print(f"Oops! Something went wrong: {e}")
    sys.exit(1)
