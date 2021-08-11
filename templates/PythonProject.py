import os
import shutil

class PythonProject():
    def __init__(self, projectName, useGit) -> None:
        self.path = 'C:\\users\\evan\\coding\\python\\'
        self.projectName = projectName
        self.useGit = useGit
        self.makeStructure()

    def makeStructure(self):
        root = os.path.abspath(self.path)

        # check if the directory already exists
        # if it does give the option to delete it, else end program
        if os.path.exists(os.path.join(root, self.projectName)):
            answer = input('Replace existing folder?(y/n)')

            if answer == 'y':
                try:
                    # os.system(f'cmd /c "cd {root} & rmdir -rf .git"')
                    print(root)
                    os.system(f'cmd /c "cd {root} & rmdir /s {self.projectName}"')
                    # shutil.rmtree(os.path.join(root, self.projectName))
                except(PermissionError):
                    print('File cannot be accessed it is being used by another process')
                    return
                    
            else:
                print('Project Creation Cancelled')
                return

        # makes the project directory
        os.mkdir(os.path.join(root, self.projectName))

        # updates root value to keep up 
        root = os.path.join(root, self.projectName)

        print('Making Package')
        # makes package directory
        self.makePackage(root)
        self.makeTests(root)
        # os.mkdir(os.path.join(root, self.projectName))
        if self.useGit:
            # TODO add git here
            self.addGitRepo(root)

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
        test_root = os.path.join(path, self.projectName)

        # make test directory
        if os.path.exists(test_root):
            shutil.rmtree(test_root)
        
        os.mkdir(test_root)

        f = open(test_root + '\\test.py', 'w')
        f.close()

    def addGitRepo(self, path):
        fileList = ['.gitignore', 'README.md', ]

        for file in fileList:
            f = open(path + '\\' + file, 'w')
            f.close()

        os.system(f'cmd /c "cd {path} & git init & git add --all"')




