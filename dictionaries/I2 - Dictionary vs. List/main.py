roster = {}


def student_input() -> None:
    command = ""
    while command.lower() != "q":
        command = input(
            """Please provide the students names and then q to quit
  > """
        )
        if command.lower() != "q":
            roster[command] = False


def inputhelper_checkin() -> str:
    options = ["check", "sign", "q"]
    command = ""
    while command not in options:
        command = input(
            """[check] sign ins, [sign] in, or [q]uit:
> """
        ).lower()
    return command


def check_in() -> None:
    for student in roster:
        if roster[student]:
            print(f"{student}: Y")
        else:
            print(f"{student}: N")


def sign_in() -> None:
    command = input("> ")
    for student in roster:
        if command.lower() == student.lower():
            roster[student] = True
            return None
    print("Student not found.")


def main() -> None:
    student_input()
    if roster != {}:
        command = ""
        while command != "q" and roster != {}:
            command = inputhelper_checkin()
            if command == "sign":
                sign_in()
            elif command == "check":
                check_in()
    else:
        print("No students were provided.")


if __name__ == "__main__":
    main()
