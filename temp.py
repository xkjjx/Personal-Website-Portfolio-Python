with open("indexBase.html","r") as file:
    data = file.read()
data = data.replace("\n","")
with open("indexBase.html","w") as file:
    file.write(data)
