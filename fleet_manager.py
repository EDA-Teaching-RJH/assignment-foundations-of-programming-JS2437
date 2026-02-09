def main():
    names, ranks, divisions, ids = init_database()
    uName = input("Please enter your full name: ")

    print(uName, " logged in!")






def init_database():
    n = ["Picard", "Riker", "Data", "Worf", "Zeph"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Cadet"]
    d = ["Command", "Command", "Operations", "Security", "Sciences"]
    i = ["1", "2", "3", "4", "5"]

    return n, r, d, i
