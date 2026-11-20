accounts = {
    "Elton": {"password": "1234", "balance": 1500},
    "Ali": {"password": "5678", "balance": 800},
    "Aysel": {"password": "9999", "balance": 2500}
}

username = input("Istifadeci adi daxil et: ")

#user_exists = 

if username not in accounts:
    print("istifadeci tapilmadi")

password = accounts[username]["password"]
check_user_pass = accounts



