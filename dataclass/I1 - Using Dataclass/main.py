from dataclasses import dataclass


@dataclass
class Cat:
    name: str
    is_hungry: bool


# -------- CAT SOUNDS -----------


def cat_sound(cat: Cat) -> str:
    if cat.is_hungry:
        return cat.name + " says hiss"
    else:
        return cat.name + " says meow"


# --------- FEED CAT ------------


def feed_cat(cat: Cat) -> None:
    cat.is_hungry = False


# ------- INPUT HELPER -------


def inputhelper(prompt) -> bool:
    if prompt.lower() != "kit" and prompt.lower() != "kat" and prompt.lower() != "quit":
        return False
    return True


# -------- MAIN -----------


def main() -> None:
    kit = Cat("Kit", True)
    kat = Cat("Kat", True)
    print(cat_sound(kit))
    print(cat_sound(kat))
    prompt = input("Feed [Kit], Feed [Kat], [quit]? ")
    while prompt.lower() != "quit":
        if inputhelper(prompt):
            if prompt.lower() == "kit":
                feed_cat(kit)
            elif prompt.lower() == "kat":
                feed_cat(kat)
        else:
            print("Please provide a valid cat name or quit.")
        print(cat_sound(kit))
        print(cat_sound(kat))
        prompt = input("Feed [Kit], Feed [Kat], [quit]? ")


main()
