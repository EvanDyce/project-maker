import os, sys

class Project():

    def __init__(self, directory, projectName) -> None:
        self.path = f'C:\\users\\evan\\coding\\{directory}\\'
        self.projectName = projectName

    def makeStructure(self):
        '''Checks if the directory already exists. If it does
        prompt the user if they want to overwrite. If yes, delete directory
        make a new directory and returns the path to it
        '''
        root = os.path.abspath(self.path)

        # check if the directory already exists
        # if it does give the option to delete it, else end program
        if os.path.exists(os.path.join(root, self.projectName)):
            answer = input('Replace existing folder?(y/n)')

            if answer == 'y':
                try:
                    # os.system(f'cmd /c "cd {root} & rmdir -rf .git"')
                    os.system(f'cmd /c "cd {root} & rmdir /s /q {self.projectName}"')
                    # shutil.rmtree(os.path.join(root, self.projectName))
                except(PermissionError):
                    print('File cannot be accessed it is being used by another process')
                    sys.exit(0)
                    
            else:
                print('Project Creation Cancelled')
                sys.exit(0)

        # makes the project directory
        os.mkdir(os.path.join(root, self.projectName))

        # updates root value to keep up 
        root = os.path.join(root, self.projectName)
        return root

    def addGitRepo(self, path, gitignoreFiles, otherFileList):
        with open(path + '\\.gitignore', 'w') as f:
            f.writelines('\n'.join(gitignoreFiles))

        for file in otherFileList:
            f = open(path + '\\' + file, 'w')
            f.close()

        os.system(f'cmd /c "cd {path} & git init & git add --all"')
