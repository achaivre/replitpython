from dataclasses import dataclass


@dataclass
class Counter:
    count: int


# ======= COUNTING FUNCTIONS =========
def inc(count: Counter) -> None:
    count.count += 1


def dec(count: Counter) -> None:
    count.count -= 1


# ======== INPUT HELPER =============


def inputhelper(choice) -> bool:
    if choice in ["inc", "dec", "quit"]:
        return True
    else:
        return False


# ========== OPTIONS ================


def options(choice, count: Counter) -> ...:
    if choice == "inc":
        inc(count)
    elif choice == "dec":
        dec(count)


# ========= MAIN =====================


def main() -> None:
    value = Counter(0)
    while True:
        print("Count: ", value.count)
        prompt = input("[inc], [dec], [quit]>").lower()
        if inputhelper(prompt):
            options(prompt, value)
            if prompt == "quit":
                break
        else:
            print("Invalid Input.")


if __name__ == "__main__":
    main()
