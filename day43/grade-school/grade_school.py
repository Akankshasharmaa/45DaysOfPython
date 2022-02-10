"""Grade School"""
class School:
    """Class School"""
    def __init__(self):
        """Initialising"""
        self.class_list = []
        self.action = []

    def add_student(self, name, grade):
        """
        input: name, grade
        appening in the list
        """
        pair = (grade, name)
        for (_, class_name) in self.class_list:
            if class_name == name:
                self.action.append(False)
                return
        self.class_list.append(pair)
        self.class_list.sort(key=lambda pair: (pair[0], pair[1]))
        self.action.append(True)

    def roster(self):
        """Return: name of all students"""
        return [name for (_, name) in self.class_list]

    def grade(self, grade_number):
        """Return: name of all student in the given grade"""
        return [name for (grade, name) in self.class_list if grade == grade_number]

    def added(self):
        """Return: action recorded when adding or not adding a name in the list"""
        return self.action
