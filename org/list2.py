from shared import Parser
        
class Students(object):
    def __init__(self):
        self.students = []
    
    def add(self, list_split):
        self.students.append([list_split[0], float(list_split[1])])

    def sort(self, asc=False):
        self.students.sort(key=lambda x: x[1],
                           reverse=not asc)
    
    def clean(self):
        self.sort(True)
        lowest = None
        students_temp = []
        
        for student in self.students:
            if not lowest:
                lowest = student[1]
            
            if student[1] == lowest:
                students_temp.append(student)
            
        self.students = students_temp
        
    def __str__(self):
        output = ''
        
        for student in self.students:
            output = output + ('%s %s\n' % (student[0], student[1])) 
        return output
            

if __name__ == '__main__':
    students_mgr = Students()
    Parser('data2.txt', students_mgr).process()
    students_mgr.clean()
    print(str(students_mgr))
    
    
    