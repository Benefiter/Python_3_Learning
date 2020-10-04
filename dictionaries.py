customer = {
    "name": "John Smith",
    "age": 30, 
    "is_verified": True
}

customer["name"] = "Jack Smith"
print(customer)

customer['birthdate'] = "Jan 1 1980"
print(customer.get("birthdate", "jan 1 1980"))
