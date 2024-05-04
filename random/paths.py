import sys
import os
import inspect


def get_path():
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    create_file(currentdir)
    
    
def create_file(current_dir):
    print("current dir: ", current_dir)
    with open(f"{current_dir}/temp_file.txt", "a") as f:
        f.write("Hello\n")
        f.close()
        
        print("write complete.")
        
        
get_path()
