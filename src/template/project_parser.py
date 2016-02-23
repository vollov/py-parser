import os


class ProjectParser:
    """
    Parse IBM ClearCase query result
    
    ct find . -type f -version "created_since(01-May)" > result.txt
    """    
    def __init__(self):
        print 'init'
        
        
    def load(self, file_path):
        print 'loading ...'
        self.file_buffer = []
        try:
            with open(file_path, "r") as file_handler:
                lines = file_handler.readlines()
                for line in lines:
                    self.file_buffer.append(line)
        except IOError:
            print 'File ' + self.config_file_path\
                   + ' does not exist, please create one.'
                   
    def parse_line(self, line):
        print 'parse line ', line
        

    def write_file(self, buffer, file_path):
        #remove the old file before generate the new one
        if os.path.isfile(self.local_psf_path):
            os.remove(self.local_psf_path)
        try:
            with open(file_path, "a") as file_handler:
                file_handler.writelines(buffer)
        except IOError:
            print 'File ' + self.config_file_path\
                   + ' does not exist, please create one.'
        
def run(file_name):
    parser = ProjectParser()
    
    parser.loadFile(file_name)
    parser.printEnums()
    
if __name__=='__main__':
    #file_name = sys.argv[1]
    run('eweb.project')