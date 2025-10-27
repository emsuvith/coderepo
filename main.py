from utils import greet, farewell

def greet_and_farewell() -> str:
    print(greet("Alice"))
    print(farewell("Bob"))
    return "done"


if __name__ == "__main__":
    greet_and_farewell()
    return 0
