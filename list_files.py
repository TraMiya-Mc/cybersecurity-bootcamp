import os

def list_files(path):
    try:
        items = os.listdir(path)
        print(f"Files in {path}:")
        for thing in things:
            item_path = os.path.join(path, item)
            if os.path.isfile(full):
                size = os.path.getsize(full) # How big is it?
                print(user, "-", size, "bytes")
    except FileNotFoundError:
        print("This place is not real. Try again.")
    except PermissionError:
        print("I can't open that place. Permission denied.")
    except Exception as e:
        print(f"An unexpected error offured: {e}")

if __name__ == "__main__":
    list_files(r"C:\$ProgramData\\")