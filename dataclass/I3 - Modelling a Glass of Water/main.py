from dataclasses import dataclass


@dataclass
class Glass:
    capacity: int
    current_amount: int


# |  Pour In Function Defined for Glass1  |


def pour_in(glass: Glass, wateradded) -> int:
    newamount = glass.current_amount + int(wateradded)
    if glass.capacity >= newamount:
        glass.current_amount = newamount
    else:
        glass.current_amount = glass.capacity


# | Pour Out Function Defined for Glass1 |


def pour_out(glass: Glass, waterremoved) -> int:
    newamount = glass.current_amount - int(waterremoved)
    if newamount < 0:
        glass.current_amount = 0
    else:
        glass.current_amount = newamount


# | Console output - Asking for capacity, water added/removed |

# | Input Helper Function |
if __name__ == "__main__":
    glass = Glass(0, 0)
    while True:
        glass.capacity = input("Capacity? ")
        if glass.capacity.isdigit():
            glass.capacity = int(glass.capacity)
            break
        else:
            print("Invalid Input.")
    while True:
        print("Glass capacity:", glass.capacity)
        print("Glass amount:", glass.current_amount)
        choice = input("Pour [in], pour [out], or [quit]?")
        # | Choice branches |
        if choice == "in":
            # | Attempt at User Validation Loop in Choice Branch |
            while True:
                added = input("Amount? ")
                if added.isdigit() == False:
                    print("Invalid user input.")
                elif int(added) > 0:
                    pour_in(glass, added)
                    break
                else:
                    print("Invalid user input.")
        elif choice == "out":
            while True:
                removed = input("Amount? ")
                if removed.isdigit() == False:
                    print("Invalid user input.")
                elif int(removed) > 0:
                    pour_out(glass, removed)
                    break
                else:
                    print("Invalid user input.")
        elif choice == "quit":
            break
        else:
            print("Invalid user input.")

# # Above code passes 2 tests. Reattempt below.hmmmmm.
