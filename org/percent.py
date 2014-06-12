        
class Students(object):
    def __init__(self):
        self.students = {}
    
    def _between_0_100(self, number):
        if number >= 0 and number <= 100:
            return True
        else:
            return False
        
    def add(self, list_split):
        if len(list_split) != 4:
            raise Exception('ERROR: Number of Parameters Violation')
        
        cur =  {}
        
        try:
            cur = {'Maths': float(list_split[1]),
                   'Physics': float(list_split[2]),
                   'Chemistry': float(list_split[3])}
        except:
            raise Exception('ERROR: Error converting string into float')
        
        if (self._between_0_100(cur.get('Maths')) and
            self._between_0_100(cur.get('Physics')) and
            self._between_0_100(cur.get('Chemistry'))):
            self.students[list_split[0]] = cur
        else:
            raise Exception('ERROR: Marks Constraint Violation')
    
    def get_student_average(self, student):
        count = 0
        suma = 0
        for class_name, grade in self.students[student].items():
            count = count + 1.0
            suma = suma + grade;
            
        return '%.2f' % float(suma / count) 
         
    def __str__(self):
        output = ''
        
        for student, grades in self.students.items():
            output = output + ('%s %.2f %.2f %.2f\n' % (student,
                                            grades.get('Maths'),
                                            grades.get('Physics'),
                                            grades.get('Chemistry'))) 
        return output
            

if __name__ == '__main__':
    students_mgr = Students()
    #Parser('data3.txt', students_mgr).process()    
    #print(str(students_mgr))
    
    a = 0
    valid_input = False
    while valid_input == False:
        try:
            a = int(input('Enter number of students:'))
            
            if a >= 2 and a <= 10:
                valid_input = True
            else:
                print('ERROR: N Constraint Violation - Need to be between 2 and 10')
        except ValueError as e:
            print('ERROR: Please enter a number')
    
    counter = 1
    while counter <= a:
        student_format = 'Name Maths Physics Chemistry'
        student = input('Enter student {%s} (%s/%s): ' % (student_format,
                                                          counter,
                                                          a))        
        try:
            students_mgr.add(student.split(' '))
            counter = counter + 1
        except Exception as e:
            print(e)
    
    
    student_name = input('Type in Student Name to get average: ')

    valid_input = False
    while valid_input == False:
        try:
            print(students_mgr.get_student_average(student_name))
            valid_input = True
        except Exception as e:
            print(e)
        
            
    """
    Output:
    Enter number of students:2
    Enter student {Name Maths Physics Chemistry} (1/2): Manny
    ERROR: Number of Parameters Violation
    Enter student {Name Maths Physics Chemistry} (1/2): Manny 90 95 99
    Enter student {Name Maths Physics Chemistry} (2/2): Kevin 90 80 100
    Type in Student Name to get average: Manny
    94.67
    """
                                                    
       
        
    