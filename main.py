def paracetamol_medicine():
    return "Available"

medicines = {
    "paracetamol": paracetamol_medicine
}

def search_medicines():
    medicine = input("Enter medicine's name: ").strip().lower()
    
    if medicine in medicines:
        print(medicines[medicine]())

    else:
        print("Not available.")
    
def exit_program():
    print("See you soon!")
    return True

menu = {
    "1": search_medicines,
    "2": exit_program
}

while True:
    print("\nPharmacy Medicine Checker.")
    print("Click <1> for Search Medicines.")
    print("Click <2> for Exit")

    choice = input("Enter your option: ").strip()

    if choice in menu:
        result = menu[choice]()

        if result is True:
            break

    else: 
        print("Invalid option taken.")





    


    