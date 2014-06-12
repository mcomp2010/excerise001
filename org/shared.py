
class Utils(object):

    @staticmethod
    def summation(list_of_objects, func_item=None, func_total=None):
        '''
        Function used to find summation of lists

        Args:
            list_of_objects: list of objects
            func_item: function to individual item
            func_total: function for whole sum
        Returns:
            The sum
        '''
        if not func_item:
            func_item = lambda x: float(x)
        if not func_total:
            func_total = lambda x: float(x)

        total = 0.0
        for item in list_of_objects:
            total = total + float(func_item(item))
        return func_total(total)
    
    @staticmethod
    def read_file(file_path, process_line_callback, skip=True):
        '''
        Function used to read file

        Args:
            file_path: path of the file
            process_line_callback: function for callback
            skip: If True skip first line of file

        Exceptions:
            IOError
        '''
        with open(file_path, 'r') as f:
            for line in f.readlines():                
                if skip:
                    skip = False
                else:
                    if hasattr(process_line_callback, '__call__'):
                        process_line_callback(line.strip())

class Parser(object):
    '''
    Class is used to parse list of urls
    '''

    def __init__(self, file_name, data_object):
        '''
        Constructor
        '''
        self.file_name = file_name
        self.data_object = data_object
        self.line_number = 0
        self.limit = 0
        

    def process(self):
        '''
        Method used to process file
        '''
        Utils.read_file(self.file_name, self._process_line, False)

    def _process_line(self, line):
        '''
        Helper Function
        '''
        if self.line_number == 0:
            self.limit = float(line)
        else:
            if self.line_number <= self.limit:
                line_split_list = line.split(' ')
                try:
                    self.data_object.add(line_split_list)
                except:
                    pass
        self.line_number = self.line_number + 1
        