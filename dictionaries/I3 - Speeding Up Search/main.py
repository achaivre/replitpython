from csv import DictReader
from dataclasses import dataclass, asdict
from datetime import date
from typing import List, Dict, Optional
from functools import wraps
import time


def print_time_taken(f):
    @wraps(f)
    def _f(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        stop = time.time()
        ms_taken = (stop - start) * 1000
        print(f"---- Time Taken by {f.__name__}: {ms_taken:.4f}ms")
        return result

    return _f


@dataclass
class Review:
    title: str
    artist: str
    url: str
    score: float
    best_new_music: bool
    author: str
    author_type: str
    pub_date: date


def build_title_review_dict(reviews: List[Review]) -> Dict[str, Review]:
    reviews_dict = {}
    for review in reviews:
        reviews_dict[review.title] = review
    return reviews_dict


@print_time_taken
def find_review_by_title_dict(
    reviews_dict: Dict[str, Review],
    title: str,
) -> Optional[Review]:
    if title in reviews_dict:
        return reviews_dict[title]
    else:
        return None


@print_time_taken
def find_review_by_title_list(
    reviews_list: List[Review],
    title: str,
) -> Optional[Review]:
    for review in reviews_list:
        if title == review.title:
            return review
    return None


### DO NOT EDIT THE CODE BELOW
### Of course, feel free to read it =)


def row_to_review(row: Dict[str, str]) -> Optional[Review]:
    try:
        return Review(
            title=row["title"],
            artist=row["artist"],
            url=row["url"],
            score=float(row["score"]),
            best_new_music=row["best_new_music"] == "1",
            author=row["author"],
            author_type=row["author_type"],
            pub_date=date.fromisoformat(row["pub_date"]),
        )
    except ValueError:
        print("Invalid Row:", row)
        return None


def load_reviews() -> List[Review]:
    with open("reviews.txt") as f:
        return list(filter(None, map(row_to_review, DictReader(f))))


def input_action() -> str:
    while True:
        action = input("Search by [title-dict], [title-list], or [quit]> ")
        if action in ("title-dict", "title-list", "quit"):
            return action
        else:
            print("Please choose a valid action.")


def print_review(review: Review) -> None:
    print("\n".join(f"    {field}: {value}" for field, value in asdict(review).items()))


def main() -> None:
    reviews = load_reviews()
    title_review_dict = build_title_review_dict(reviews)
    while True:
        action = input_action()
        if action == "title-dict":
            title = input("title> ").lower()
            review = find_review_by_title_dict(title_review_dict, title)
            if review is None:
                print(f"No review found for {title}")
            else:
                print_review(review)
        elif action == "title-list":
            title = input("title> ").lower()
            review = find_review_by_title_list(reviews, title)
            if review is None:
                print(f"No review found for {title}")
            else:
                print_review(review)
        elif action == "quit":
            break
        else:
            print("Please choose a valid action.")


if __name__ == "__main__":
    main()
