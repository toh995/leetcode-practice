class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ret = len(students)

        counter = {
            0: 0,
            1: 0,
        }

        for student in students:
            if student == 1:
                counter[1] += 1
            else:
                counter[0] += 1

        for sandwich in sandwiches:
            if counter[sandwich] > 0:
                counter[sandwich] -= 1
                ret -= 1

            else:
                break

        return ret
