employees = {
    "Alice": {"role": "Developer", "salary": 80000},
    "Bob": {"role": "Designer", "salary": 75000}
}

print(employees["Alice"]["role"])
employees["Bob"]["salary"] = 78000

employees["Charlie"] = {"role" : "Manager", "salary" : 90000}

print(employees)