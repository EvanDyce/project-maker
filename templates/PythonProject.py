import os
import shutil
from templates.Project import Project

class PythonProject(Project):
    def __init__(self, projectName) -> None:
        super().__init__(projectName)
        self.makeStructure()

    def makeStructure(self):
        root = super().makeStructure()

        f = open(root + '\\outline.txt', 'w')
        f.close()
        
        # makes package directory
        self.makePackage(root)
        self.makeTests(root)
        # os.mkdir(os.path.join(root, self.projectName))
        gitignoreLines = ['*.pyc', 'test']
        otherFiles = ['README.md', 'outline.txt']
        super().addGitRepo(root, gitignoreLines, otherFiles)

    def makePackage(self, path):
        package_root = os.path.join(path, self.projectName)

        # make the package directory with smae name as parent
        os.mkdir(package_root)
        # create file __init__.py in the package
        f = open(package_root + '\\__init__.py', 'w')
        f.close()

        # create src_root for src directory within package directory
        src_root = os.path.join(package_root, 'src')
        # make directory src
        os.mkdir(src_root)
        # create file main.py within src
        f = open(src_root + '\\main.py', 'w')
        f.close()
        
    def makeTests(self, path):
        test_root = os.path.join(path, 'test')

        # make test directory
        if os.path.exists(test_root):
            shutil.rmtree(test_root)
        
        os.mkdir(test_root)

        f = open(test_root + '\\test.py', 'w')
        f.close()





