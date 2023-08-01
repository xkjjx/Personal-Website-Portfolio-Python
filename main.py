from helper import *
import os

def readProjects():
    projects = [x for x in os.listdir("Projects") if x[0] != "."]
    ProjectsList = []
    for project in projects:
        name = project
        skills = []
        with open("Projects/{}/description.txt".format(name)) as d:
            description = d.read()

        with open("Projects/{}/shortDescription.txt".format(name)) as d:
            shortDescription = d.readlines()[0]

        with open("Projects/{}/skills.txt".format(name)) as s:
            for line in s.readlines():
                skills.append(line.strip())

        p = Project(name,description,shortDescription,skills)
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





