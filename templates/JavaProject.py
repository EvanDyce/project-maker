from templates.Project import Project
import os

class JavaProject(Project):
    def __init__(self, projectName) -> None:
        super().__init__('java', projectName)
        self.projectName = projectName
        self.makeStructure()

    def makeStructure(self):
        root = super().makeStructure()

        groupID = input('Enter a GroupID, usually com.projectname: ')
        mavenCommand = f'''mvn archetype:generate -DgroupId={groupID} -DartifactId={self.projectName} -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false''' 


        os.system(f'cmd /c "cd {root} & {mavenCommand}"')

        gitignoreFiles = ['out', 'server', 'node_modules', '*.vsix', '.DS_Store', '.vscode-test', 'undefined', 'target', 'dist', 'bin/', '.settings', '.classpath', '.project', 'test/resources/projects/**/.vscode', 'test/resources/projects/maven/salut/testGradle']
        otherFiles = ['README.md', 'outline.txt']

        super().addGitRepo(root, gitignoreFiles, otherFiles)