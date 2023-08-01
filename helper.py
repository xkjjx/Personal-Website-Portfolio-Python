def encloseTags(tag,text,*attributes):
    outP = "<" + tag
    for attribute in attributes:
        outP += " " + attribute[0] + "=\"" + attribute[1] + "\""
    return outP + ">\n" + text + "\n</" + tag + ">"


class Project():
    def __init__(self,name,description,shortDescription=None,skills=[]):
        self.name = name
        if shortDescription == None:
            self.shortDescription = description
        else:
            self.shortDescription = shortDescription
        self.description = description
        self.skills = skills

    def __str__(self):
        return "\n".join(["Name: " + self.name,"Short description: " + self.shortDescription,"Description: " + self.description])


    def createPage(self):
        with open("base.html","r") as file:
            file = file.readlines()
            file[1] = self.name
            file[3] = '<img id="imgmain" src="Projects/{}/images/main.png">'.format(self.name)
            content = ""
            d = self.description.split("\n")

            for line in d:
                content += encloseTags("p",line)

            file[4] = content

            for skill in self.skills:
                file[6] += encloseTags("li",skill)

            outP = "\n".join(file)
        return outP
    def createCard(self):
        outP = encloseTags("div",'<img src="Projects/{0}/images/main.png" alt = "{0}">'.format(self.name) + encloseTags("h3",self.name) + encloseTags("p",self.shortDescription) + encloseTags("a","View project",["href","{}.html".format(self.name)]),["class","project-card"])
        return outP








