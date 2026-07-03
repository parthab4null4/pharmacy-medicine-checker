def medicine_paracetamol():
    return "Available"

def exit_command():
    return True

medicines = {
    "paracetamol": medicine_paracetamol,
    "exit": exit_command
    }

while True:
    medicine = input("Enter medicine name: ").strip().lower()

    if medicine in medicines:
        result = medicines[medicine]()

        if result is True:
            print("See you soon!")
            break

        elif result is not None:
            print(result)

    else: 
        print("Not available")