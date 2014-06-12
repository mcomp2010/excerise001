

class ParseXYZN(object):
    def __init__(self, input):
        list_split = input.split(' ')
        
        if len(list_split) != 4:
            raise Exception('ERROR: Number of Parameters Violation')
        
        self.main_dict = {}
        self.main_dict['x'] = list_split[0]
        self.main_dict['y'] = list_split[1]
        self.main_dict['z'] = list_split[2]
        self.main_dict['n'] = list_split[3]
    
    def get_range_x(self):
        return range(0,int(self.main_dict['x'])+1)
    
    def get_range_y(self):
        return range(0,int(self.main_dict['y'])+1)
    
    def get_range_z(self):
        return range(0,int(self.main_dict['z'])+1)
    
    def get_n(self):
        return int(self.main_dict['n'])
    
    def __str__(self):
        return str(self.main_dict)

if __name__ == '__main__':
    xyzn = ParseXYZN('1 1 1 2') 
    new_list = [[x,y,z] for x in xyzn.get_range_x() for y in xyzn.get_range_y() for z in xyzn.get_range_z() if x + y + z != xyzn.get_n()]
    print(new_list)
    
    '''
    Output:
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    '''

    