"""
Find no of semesters it would take for finishing up all subjects

"""

from typing import List


def minNumberOfSemesters(n: int, dependencies: List[List[int]], k: int) -> int:
    count = 0

    if not dependencies:
        q, r = divmod(n, k)
        if r != 0:
            return q + 1
        else:
            return q

    res = dependencies[0]

    subject = set()

    for i in dependencies[1:]:
        subject.add(i[1])

        if i[0] in res:
            ind = res.index(i[0])
            res.insert(ind+1, i[1])
        elif i[1] in res:
            ind = res.index(i[1])
            res.insert(ind - 1, i[0])
        else:
            res.extend(i)

    j = 0
    for i in range(len(res)):
        j += 1

        if res[i] in subject:
            count += 1
            q, r = divmod(j - 1, k)
            if r != 0:
                count = count + q + 1
            else:
                count += q

            j = 0
    print(count)

# minNumberOfSemesters(4, [[2,1],[3,1],[1,4]], 2)
minNumberOfSemesters(5, [[3,1]], 4)