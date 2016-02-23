import os


class CpResultParser:
    """
    Parse Energy policy copy result
    """    
    def __init__(self):
        print 'init'
        
        
    def load(self, file_path):
        print 'loading ...'
        #self.file_buffer = []
        
        print_next_line = False
        try:
            with open(file_path, "r") as file_handler:
                lines = file_handler.readlines()
                for line in lines:
                    if print_next_line:
                        print line.rstrip()
                    #self.file_buffer.append(line)
                    print_next_line = self.parse_line(line)
                    
        except IOError:
            print 'File ' + self.config_file_path\
                   + ' does not exist, please create one.'
    
    def parse_line(self, line):
        print_next_line = False
        if line:
#             print line
            if line == 'The following accounts must be copied down to the appropriate region\n':
                print_next_line = True
        
        return print_next_line
                
#         if line:
#             line_array = line.split('@@', 1 )
#             file =  self.path_leaf(line_array[0])
#             filename, file_extension = os.path.splitext(file)
#             
#             if file_extension == '.java':
#                 if filename not in self.file_set:
#                     self.file_set.add(filename)
            #print filename, file_extension
            
                   
    def print_all(self):
        i = 1
        for line in self.file_set:
            print i, line
            i+=1
            
        
def run(file_name):
    parser = CpResultParser()
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(current_directory, '../data')
        
    parser.load(os.path.join(data_directory, file_name))
#     parser.print_all()
    
if __name__=='__main__':
    #file_name = sys.argv[1]
    run('cp_result_2.txt')