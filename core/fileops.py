from PyQt6.QtWidgets import QFileDialog
import os

# ============================================================================
# File Operation Class
# ============================================================================
class FileOps:
    """ This Class Handle File Operations """
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # File dialog filters
        self.file_filter = (
            "All Files (*.*);;"
            "Python Files (*.py);;"
            "C++ Files (*.cpp);;"
            "C Files (*.c);;"
            "QSS Files (*.qss);;"
            "Java Files (*.java);;"
            "JavaScript Files (*.js);;"
            "HTML Files (*.html);;"
            "Markdown Files (*.md)"
        )

    def read_file(self,file_path):
        """ This Method Reads a File And Returns Its Content """
        try:
            with open(file_path,"r",encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError as e:
            print(e)
            return False
        else:
            return content
        
    def write_file(self,file_path,content):
        """ This Method Writes a File """
        try:
            with open(file_path,"w",encoding="utf-8",newline="") as f:
                f.write(content)
        except FileNotFoundError as e:
            print(e)
            return False
        
        return True

    def open_file(self, file_path = None, file_name = None):
        """This Method Open File"""
        
        if not file_path and not file_name:
            file_path, _ = QFileDialog.getOpenFileName(
                self.parent,
                "Open File",
                "",
                self.file_filter
            )
        file_name = os.path.basename(file_path)

        if not file_path:
            return
        
        text = self.read_file(file_path)
        if text is not None:
            self.parent.tabs.open_tab(file_name, file_path, text)


    def open_folder(self):
        """This Method Open Folder"""

        file_path = QFileDialog.getExistingDirectory(self.parent, "Open Folder")
        if not file_path:
            return

        self.parent.mk_tree(file_path)

    def new_file(self):
        name = "Untitled.py"
        text = ""

        path = os.path.join(self.parent.current_working_dir,name)

        counter = 1
        while path in self.parent.tabs.open_tabs:
            path = os.path.join(self.parent.current_working_dir, f"Untitled-{counter}.py")
            counter += 1

        self.parent.tabs.open_tab(os.path.basename(path), path, text)

    def save_file(self,file_path=None,content=None):
        """This Method Saves the File"""
        if file_path is None:
            file_path = self.parent.tabs.get_path()

        if content is None:
            content = self.parent.tabs.get_text()

        if not content:
            return

        save = self.write_file(file_path,content)
        if save :
            print("File Saved ✅")

    def save_as(self):

        content = self.parent.tabs.get_text()
        file_path, _ = QFileDialog.getSaveFileName(self.parent, "", "Untitled.py")

        if not file_path:
            return
        
        self.save_file(file_path,content)