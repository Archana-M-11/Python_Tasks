'''
Create Project class with projectId and projectName
defne constructor
defne a method displayProjectDetails
'''
class Project:
    def __init__(self,projectId,projectName):
        self.projectId=projectId
        self.projectName=projectName
    def displayProjectDetails(self):
        print('Project ID:', self.projectId)
        print('Project Name:', self.projectName)