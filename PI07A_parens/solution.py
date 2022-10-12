from typing import List

def generate_parens(n: int) -> List[str]:
        all_parens = []
        def generate(combination: str, left: int, right: int):
            if left > 0:         
                generate(combination + '(', left-1, right)
            if right > left:
                generate(combination + ')', left, right-1)
            if not right:
                all_parens.append(combination)
        generate('', n, n)
        return all_parens

if __name__ == "__main__":
    print(generate_parens(4))
                

