""" Kindergarten Garden"""
class Garden:
    """
    input: daigram, student_name
    return: list of plants
    """
    myplant = {
    "C" : "Clover",
    "G" : "Grass",
    "R" : "Radishes",
    "V" : "Violets"
    }

    students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve',
        'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students = students, myplant = myplant):
        self.diagram = diagram.split('\n')
        self.students = sorted(students)
        self.myplant = myplant

    def plants(self, student_name):
        """
        input : studen_name
        return: name of the plants
        """
        index = self.students.index(student_name) * 2
        mylist = []
        for i in self.diagram[0][index: index+ 2]:
            mylist.append(self.myplant[i])
        for i in self.diagram[1][index: index+2]:
            mylist.append(self.myplant[i])
        return mylist
