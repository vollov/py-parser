import os,ntpath

class ClearCaseQueryParser:
    
    def __init__(self):
        print 'init'
        self.file_set = set()
        
    def load(self, file_path):
        print 'loading ...'
        #self.file_buffer = []
        try:
            with open(file_path, "r") as file_handler:
                lines = file_handler.readlines()
                for line in lines:
                    #self.file_buffer.append(line)
                    self.parse_line(line)
                    
        except IOError:
            print 'File ' + self.config_file_path\
                   + ' does not exist, please create one.'
    
    def print_all(self):
        i = 1
        for line in self.file_set:
            print i, line
            i+=1
              
    def parse_line(self, line):
        if line:
            line_array = line.split('@@', 1 )
            file =  self.path_leaf(line_array[0])
            filename, file_extension = os.path.splitext(file)
            
            if file_extension == '.java':
                if filename not in self.file_set:
                    self.file_set.add(filename)
            #print filename, file_extension
    
    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)


#     def write_file(self, buffer):
#         #remove the old file before generate the new one
#         if os.path.isfile(self.local_psf_path):
#             os.remove(self.local_psf_path)
#         try:
#             with open(file_path, "a") as file_handler:
#                 file_handler.writelines(buffer)
#         except IOError:
#             print 'File ' + self.config_file_path\
#                    + ' does not exist, please create one.'
        
def run(file_name):
    parser = ClearCaseQueryParser()
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(current_directory, '../data')
        
    parser.load(os.path.join(data_directory, file_name))
    parser.print_all()
    
if __name__=='__main__':
    #file_name = sys.argv[1]
    run('cc_log.data')