name = "John"
name_len = len(name)
if name_len < 3:
    print("Name must be at least 3 chars")
elif name_len > 50:
    print("Name must be a maximum of 50 chars")
else:
    print("Name looks good")