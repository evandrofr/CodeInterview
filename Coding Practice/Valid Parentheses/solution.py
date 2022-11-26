class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        correct_match = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        openings = correct_match.keys()
        for caracter in s:
            if caracter in openings:
                stack.append(caracter)
            else:
                if stack == []:
                    return False
                top_stack = stack.pop()
                if caracter != correct_match[top_stack]:
                    return False
        if stack != []:
                return False
        return True