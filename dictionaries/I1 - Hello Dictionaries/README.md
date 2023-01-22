# Dictionary - Intro 1: Hello Dictionary

In this exercise you will write a program that tells the user who authored a requested book.

```
view [books], show [author], [quit]> books
- Harry Potter
- Effective Testing with RSpec 3
- Automate the Boring Stuff
- Quiet
- Peak
view [books], show [author], [quit]> author
book> Harry Potter
JK Rowling
view [books], show [author], [quit]> author
book> Automate the Boring Stuff
Al Sweigart
view [books], show [author], [quit]> quit
```

## Related Videos

- [Hello Dictionary](https://www.youtube.com/watch?v=3Llx4ZMDw6c&list=PL6xuclUa80Qhn2Roxw9RPmDEatrJdg09S&index=1)
- [Keys Vs Values Vs Items](https://www.youtube.com/watch?v=_3wM_-UKCz0&list=PL6xuclUa80Qhn2Roxw9RPmDEatrJdg09S&index=2)
- [Typing Dicts](https://www.youtube.com/watch?v=k4jZtRYmd7Q&list=PL6xuclUa80Qhn2Roxw9RPmDEatrJdg09S&index=3)

## Related Resources

- [Real Python - Dictionaries in Python](https://realpython.com/python-dicts/)
- [Python Docs - Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## Rubric

- [ ] The user can view the known books
- [ ] The user can view the author of a specific book
- [ ] The user can quit

### Style Guide

- [ ] Code should be formatted with black.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker.
