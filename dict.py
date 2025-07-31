users = {"Tramiya": 25, "bob" : 30}

#Print value for "alice"
print(users["Tramiya"])

# safely get value for "charlie"
print(users.get('charlie', "Not found"))

# Add a new user
users["charlie"] = 28

print(users)