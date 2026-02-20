from utils import greet, farewell

ok bug
ok new bug save me
def greet_and_farewell() -> str:
    print(greet("Alice"))
    print(farewell("Bob"))
    return "done"

def printf(a):
    print(a)

def add(a, b):
    return a + b

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr 

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
            left = mid + 1
        else:
            right = mid - 1
    return -1
    
ldkk
knkbvjhsvjgvskvs


jbfjhbkhjbkcbskb kdbfksksj

if __name__ == "__main__":
    greet_and_farewell()
    printf('%D')
    return 0
    # ;jhkhd$%

