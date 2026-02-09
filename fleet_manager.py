def main():
    names, ranks, divisions, ids = init_database()
    uName = input("Please enter your full name: ")

    print(uName, " succesfully logged in.")
    while True:
        opt = display_menu()
        if op == "1":
            display_roster(names, ranks, divisions, ids)







def init_database():
    n = ["Picard", "Riker", "Data", "Worf", "Zeph"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Cadet"]
    d = ["Command", "Command", "Operations", "Security", "Sciences"]
    i = ["1", "2", "3", "4", "5"]
    return n, r, d, i

def display_menu():
    print("\n--- MENU ---")
    print("1) View Crew Members")
    print("2) Add Crew Member")
    print("3) Remove Crew Member")
    print("4) Update Rank")
    print("5) Search Crew Name")
    print("6) Filter By Division")
    print("7) Calculate Payroll")
    print("8) Count Officers")
    opt = input("Select option: ")
    return opt

def display_roster(n, r, d, i):
    print(f"{'ID':<5} {'Name':<10} {'Rank':>20} {'Division':>20}")
    print("---------------------------------------------------------------------------")

    for id, name, rank, division in zip(i, n, r, d):
        print(f"{id:<5} {name:<10} {rank:>20} {division:>20}")
