class School:
    class_dict = {}
    student_name = set()
    def __init__(self):
        pass

    def add_student(self, name, grade):
        if name not in self.student_name:
            grade_exists = grade in self.class_dict
            if grade_exists:
                self.class_dict[grade].append(name)
                self.student_name.add(name)
            else:
                self.class_dict[grade] = [name]
                self.student_name.add(name)
        else:
            pass

    def roster(self):
        students = []
        for grade in sorted(self.class_dict.key()):
            students += sorted(self.class_dict[grade])
        return sorted(students)

    def grade(self, grade_number):
        student_in_grade = []
        if grade_number in self.class_dict:
            student_in_grade.extend(self.class_dict[grade_number])
        return sorted(student_in_grade)

    def added(self):
        pass

import operator
class School(object):
    def __init__(self):
        self.Roster = dict()

    def add_student(self, name, grade):
        self.Roster[name] = grade

    def roster(self):
        sorted_roster = sorted(self.Roster.items(), key = lambda x : (x[1], x[0]))
        ans = []
        for (i, j) in sorted_roster:
            ans.append(i)
        return ans

    def grade(self, grade_number):
        ans = []
        for key, val in self.Roster.items():
            if(val == grade_number):ans.append(key)
        ans.sort()
        return ans