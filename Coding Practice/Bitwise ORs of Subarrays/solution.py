class Solution(object):
    def subarrayBitwiseORs(self, A):
        solution = set()
        current = {0}
        for item in A:
            current = {item | y for y in current} | {item}
            print("c ", current)
            solution |= current
            print("s ", solution)
        return len(solution)

if __name__ == "__main__":
    test_list = [1,2,3,4]
    r = Solution().subarrayBitwiseORs(test_list)
    print(r)