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
        mavenCommand = f'''mvn archetype:generate -DgroupId={groupID} 
                        -DartifactId={self.projectName} -DarchetypeArtificatId-maven-archectype-quickstart 
                        -DinterativeMode=false''' 


        os.system(f'cmd /c "{mavenCommand}"')