import os

class Project():

    def __init__(self, projectName, useGit) -> None:
        print('super init called')
        self.path = 'C:\\users\\evan\\coding\\python\\'
        self.projectName = projectName
        self.useGit = useGit

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
                    return
                    
            else:
                print('Project Creation Cancelled')
                return

        # makes the project directory
        os.mkdir(os.path.join(root, self.projectName))

        # updates root value to keep up 
        root = os.path.join(root, self.projectName)
        return root

    def addGitRepo(self, path, gitignoreFiles, otherFileList):
        with open(path + '\\.gitignore', 'w') as f:
            f.writelines('\n'.join(gitignoreFiles))

        for file in otherFileList:
            print(file)
            f = open(path + '\\' + file, 'w')
            f.close()

        os.system(f'cmd /c "cd {path} & git init & git add --all"')

    def create_project() -> bool:
        pass

    def delete_project() -> bool:
        pass

    def rename_project() -> bool:
        pass

