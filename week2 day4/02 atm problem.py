def calculate_total_balance():
    denominations = [2000, 500, 200, 100]  # Available denominations
    total_balance = 0

    for i in range(4):
        denomination = int(input(f"Enter the {i+1} Denomination: "))
        num_notes = int(input(f"Enter the {i+1} Denomination number of notes: "))
        total_balance += denomination * num_notes

    print(f"Total Available Balance in ATM: {total_balance}")

# Example usage:
calculate_total_balance()
