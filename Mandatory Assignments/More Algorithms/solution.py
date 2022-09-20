from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic_req ={
            e:[]
            for e in range(numCourses)
        }

        for r in prerequisites:
            dic_req.setdefault(r[0], []).append(r[1])
            
        
        flag = True
        courses = []
        courses_set = set()

        while flag:
            flag = False
            for c, pr in dic_req.items():
                if (all(elem in courses_set for elem in pr) or pr == []) and (c not in courses_set):
                    courses.append(c)
                    courses_set.add(c)
                    flag = True
            if len(courses) == numCourses:
                return courses
        return []
