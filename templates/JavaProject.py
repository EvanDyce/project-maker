from templates.Project import Project

class JavaProject():
    def __init__(self, projectName) -> None:
        self.projectName = projectName
        super().__init__('java')
        
