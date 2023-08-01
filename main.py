from helper import *
import os

def readProjects():
    projects = [x for x in os.listdir("Projects") if x[0] != "."]
    ProjectsList = []
    for project in projects:
        name = project

        with open("Projects/{}/description.txt".format(name)) as d:
            description = d.readlines()[0]

        with open("Projects/{}/shortDescription.txt".format(name)) as d:
            shortDescription = d.read()

        p = Project(name,description,shortDescription)
        ProjectsList.append(p)
    return ProjectsList

def createIndex(projectList):
    with open("indexBase.html", "r") as file:
        data = file.readlines()

    data[1] = ""

    for p in projectList:
        data[1] += p.createCard()

    with open("index.html", "w") as file:
        file.write("\n".join(data))

def createProjectPages(projectList):
    for p in projectList:
        with open("{}.html".format(p.name), "w") as file:
            file.write(p.createPage())

def fullUpdate():
    projectList = readProjects()
    createIndex(projectList)
    createProjectPages(projectList)

fullUpdate()





