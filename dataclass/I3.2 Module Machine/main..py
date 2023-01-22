from dataclasses import dataclass


@dataclass
class ModuleProgress:
    state: str
    fail: int


# ===== INPUT VALIDATION ======
def inputvalidcomplete(user) -> bool:
    if user == "Complete":
        return True
    else:
        return False


def inputvalidpassfail(user) -> bool:
    if user == "Pass" or user == "Fail":
        return True
    else:
        return False


# ======= REQUIRED FUNCTIONS


def complete_task(m: ModuleProgress) -> None:
    if m.state == "Introductory Exercises":
        m.state = "Project"
    elif m.state == "Project":
        m.state = "Benchmark"


def pass_task(m: ModuleProgress) -> None:
    if m.state == "Benchmark":
        m.state = "Module Complete"
        print("Current State:", m.state)


def fail_task(m: ModuleProgress) -> None:
    if m.state == "Benchmark":
        m.state = "Project"


# =========== MAIN


def main():
    running = True
    m = ModuleProgress("Introductory Exercises", 0)
    print("Current State:", m.state)
    while running:
        user = input("> ")
        if m.state == "Introductory Exercises":
            if inputvalidcomplete(user):
                complete_task(m)
                print("Current State:", m.state)
            else:
                print("Error: Invalid Transition")
                print("Current State:", m.state)
        elif m.state == "Project":
            if inputvalidcomplete(user):
                complete_task(m)
                print("Current State:", m.state)
            else:
                print("Error: Invalid Transition")
                print("Current State:", m.state)
        elif m.state == "Benchmark":
            if inputvalidpassfail(user):
                if user == "Pass":
                    pass_task(m)
                elif user == "Fail":
                    fail_task(m)
                    m.fail += 1
                    if m.fail < 3:
                        print("Current State:", m.state)
                    else:
                        m.state = "Fail"
                        print("Current State:", m.state)
                        running = False
            else:
                print("Error: Invalid Transition")
                print("Current State:", m.state)


main()
