# Dataclass - Intro 3.1: Counting Machine

In this exerise you will reimplement a solution to the "Counting Machine" intro exercise from Module 3. However, this time you will use a dataclass model the counter state and a pair of functions to handle the logic for incrementing and decrenting the counter's state.

> In this you will implement a state machine that tracks a single integer. The state machine allows users to increment the number (add 1) or decrement the number (subtract 1).
>
> **Example:**

> ```
> Count: 0
> [inc], [dec], [quit]> inc
> Count: 1
> [inc], [dec], [quit]> inc
> Count: 2
> [inc], [dec], [quit]> inc
> Count: 3
> [inc], [dec], [quit]> inc
> Count: 4
> [inc], [dec], [quit]> dec
> Count: 3
> [inc], [dec], [quit]> dec
> Count: 2
> [inc], [dec], [quit]> dec
> Count: 1
> [inc], [dec], [quit]> dec
> Count: 0
> [inc], [dec], [quit]> dec
> Count: -1
> [inc], [dec], [quit]> quit
> ```

## Rubric

- [ ] `Counter`, `inc`, and `dec` implemented and used correctly.
  - `Counter` should be a dataclass that has contains the appropriate field(s) to model the state for the Counting Machine.
  - `inc(counter: Counter) -> None` should increase the counter's state by one.
  - `dec(counter: Counter) -> None` should decrease the counter's state by one.
- [ ] The user can increment the count
- [ ] The user can decrement the count
- [ ] The user can quit the program
- [ ] Display an error message when the user provides an invalid action.
- [ ] Use a single `while` loop

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
