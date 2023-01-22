# Dictionary - Intro 2: Has Everyone Signed In Today

In this exercise you will reimplement a previous exercise, but this time you will use a dictionary (instead of a `List[Student]`) as your primary data structure. Here is the previous assignment's description.

> In this exercise you will build a small program for collecting student names and then allowing student to sign in and check if the whole class has arrived yet. Your application should start off collecting names from the user. Once they are finished providing names, you should allow the user to check whether or not each person has signed in, sign in a student, or quit.
>
> **Tip:** You can represent each student with a `Student` dataclass that stores the student's name and whether or not they have checked in yet.
>
> Example:
>
> ```
> Please provide the students names and then q to quit
> > britta
> > jeff
> > abed
> > troy
> > q
> [check] sign ins, [sign] in, or [q]uit:
> > check
> britta: N
> jeff: N
> abed: N
> troy: N
> [check] sign ins, [sign] in, or [q]uit:
> > sign
> > britta
> [check] sign ins, [sign] in, or [q]uit:
> > check
> britta: Y
> jeff: N
> abed: N
> troy: N
> [check] sign ins, [sign] in, or [q]uit:
> > sign
> > abed
> [check] sign ins, [sign] in, or [q]uit:
> > check
> britta: Y
> jeff: N
> abed: Y
> troy: N
> [check] sign ins, [sign] in, or [q]uit:
> > q
> ```
>
> Example:
>
> ```
> Please provide the students names and then q to quit
> > q
> No students were provided
> ```

### Related Videos

- [Dictionaries vs Lists](https://www.youtube.com/watch?v=mB3xrB1iIds&list=PL6xuclUa80Qhn2Roxw9RPmDEatrJdg09S&index=4)

### Rubric

- [ ] User can provide an arbitrary amount of student names
- [ ] User can check in students
- [ ] User can view checkin status
- [ ] Program ends early and prints appropriate message if no students are provided
- [ ] Students and checkins are implemented using a single `Dict[str, bool]`

### Style Guide

- [ ] Code should be formatted with the replit auto-formatter.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker.
