def one_edit_away(first: str, second: str) -> bool:
    if len(first) == len(second):
        return one_replecement_away(first, second)
    if len(first) - len(second) == 1 or len(first) - len(second) == -1:
        return one_insertion_away(first, second)
    return False

def one_replecement_away(first: str, second: str) -> bool:
    diff = 0
    for idx in range(len(first)):
        if first[idx] != second[idx]:
            diff += 1
    return diff <= 1 

def one_insertion_away(first: str, second: str) -> bool:
    if len(first) > len(second):
        bigger = first
        lower = second
    else: 
        bigger = second
        lower = first
    ib = 0
    il = 0
    for idx in range(len(lower)):
        if bigger[ib] != lower[il]:
            if ib != il:
                return False
            ib += 1
        else:
            ib += 1
            il += 1
    return True


if __name__ == "__main__":
    first  = str(input("Insert First String: "))
    second = str(input("Insert Second String: "))
    print(one_edit_away(first=first, second=second))