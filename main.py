from utils import greet, farewell

def run_app() -> int:
    print(greet("Alice"))
    print(farewell("Bob"))
    return "done"


if __name__ == "__main__":
    run_app()
