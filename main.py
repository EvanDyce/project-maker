from templates.PythonProject import PythonProject
from templates.JavaProject import JavaProject


def main():
    typeMap = {
        'java': JavaProject,
        'python': PythonProject
    }
    projectType = input('Project Type: ')

    if projectType not in typeMap.keys():
        print('Please enter a supported project type')
        return

    projectName = input('Project Name: ')

    if type(projectName) != str or projectName.find(' ') != -1:
        print('Invalid Project Name')
        return

    useGit = input('Integrate Git?(y/n)')
    if useGit == 'y':
        typeMap[projectType](projectName, True)
    else:
        typeMap[projectType](projectName, False)


if __name__ == "__main__":
    main()


