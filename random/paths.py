import sys
import os
import inspect


def find_paths():
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    print("Current path: ", currentdir)
    print("Parent path: ", parentdir)
    text_file(currentdir)
    
    
def text_file(currentdir):
    with open(f"{currentdir}/text_file.txt", "a") as f:
        f.write("Hello, this is a text document\n")
        f.close()


if __name__ == "__main__":
    find_paths()
