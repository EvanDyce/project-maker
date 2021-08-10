import os

class Project():

    def __init__(self, projectType, projectName) -> None:
        self.language = projectType
        self.projectName = projectName
        self.path = f'C:\\users\\evan\\coding\\{self.language}'
        print(self.path)

    def create_project() -> bool:
        pass

    def delete_project() -> bool:
        pass

    def rename_project() -> bool:
        pass

