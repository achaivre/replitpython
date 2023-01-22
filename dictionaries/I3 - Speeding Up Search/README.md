# Dictionary - Intro 3: Speeding Up Search

In this exercise you will complete a program that allows the user to look up album reviews data from pitchfork.com.

In particular, you will write three functions:

- `build_title_review_dict`: This function takes in a `List[Review]` and produces a `Dict[str, Review]` where the keys are the titles of the reviews and the values are the `Review` objects.
- `find_review_by_title_dict`: This function returns a `Review` with the same title as the provided `title`. If a review with that title does not exist, the program should return `None`.
- `find_review_by_title_list`: This function returns a `Review` with the same title as the provided `title`. If a review with that title does not exist, the program should return `None`.

_Pay careful attention to the timing information printed after finding a review._ Is there a difference in performance between looking up a the review using a list vs using a dictionary? If there is a difference, how big is the difference? How does the difference depend on what the inputs are (i.e. which title)?

## Rubric

- [ ] Required functions pass provided test cases
  - `build_title_review_dict`
  - `find_review_by_title_dict`
  - `find_review_by_title_list`

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
