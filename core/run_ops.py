from config import PYTHON_EXE_PATH
import os,subprocess

def run_code(self):
    """Run the current Python file"""

    file_path = self.get_path()
    if not file_path: return
        
    file_dir = os.path.dirname(file_path)
    if not file_dir: return

    _, extension = os.path.splitext(file_path)

    if extension == ".py":
        subprocess.Popen(
            ["cmd", "/k", PYTHON_EXE_PATH, file_path], # "/k" means Terminal Stays Open after Running 
            cwd = file_dir, # set the Current Working Directory
            creationflags = subprocess.CREATE_NEW_CONSOLE, # Creats a New Terminal
        )
    else:
        print("Only Python File is Suported ")