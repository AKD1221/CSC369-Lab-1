import json

#with open('2022-12-21-23.json', encoding='utf8', errors='ignore') as myfile:
#    fileContents = json.load(myfile)

#print(fileContents)

data = [json.loads(line) for line in open('2022-12-21-23.json', 'r', encoding='utf-8')]


Repo = {}
User = {}
EventType = {}

mypartitions = [[], [], [], [], [], [], [], [], [], []]

#change range to range(len(data))
for x in range(5):
    myline = data[x]

    #check which partition to put our data line
    part = hash(myline["id"]) % 10
    mypartitions[part].append(myline)

    mytype = myline["type"]
    if mytype in EventType.keys():
        EventType[mytype] += 1
    else:
        EventType[mytype] = 1

    username = myline["actor"]["login"]
    if username in User.keys():
        User[username].append(myline["id"])
    else:
        User[username] = [myline["id"]]
    
    myRepo = myline["repo"]["name"]
    if myRepo in Repo.keys():
        Repo[myRepo].append(myline["id"])
    else:
        Repo[myRepo] = [myline["id"]]
    

print(mypartitions)
print(Repo)
print(EventType)
print(User)

