#Ben Masi, Strongly Connected Component Program
time = 0
def increment():
    global time
    time = time+1

z = 0
def incrementZ():
    global z
    z = z+1

global AdjList 
AdjList = []

largestIndex = 10 #Please insert vertex with the highest int value
with open("myfile.txt") as textFile:#Put input file on this line
        lines = [line for line in textFile]
        for line in lines:
            AdjList.append([])
            colon = line.find(':')
            beforeColon = int(line[:colon])
            attachedVertices = line[colon+1:len(line)-1]
            newVertices = attachedVertices.split(',')
            varints = int(line[:colon])
            AdjList[len(AdjList)-1].append(int(line[:colon]))
            for x in newVertices:
                AdjList[len(AdjList)-1].append(int(x))

global RevAdjList
RevAdjList = []
i = 1
while i <= largestIndex:
    RevAdjList.append([i])
    i = i+1
for x in AdjList:
    for i in x[1:]:
        RevAdjList[i-1].append(x[0])

global visited 
visited = []

global modified_visited 
modified_visited = []

global components 
components = []

global component 
component = []

global finish_times 
finish_times = [0] * largestIndex

global sourceVertices 
sourceVertices = list(range(1, largestIndex+1))

global endVertices
endVertices = []

def DFSvisit(v):
    increment()
    visited.append(v)
    for i in RevAdjList[v-1][1:]:
        if i not in visited:
            DFSvisit(i)
    increment()
    finish_times[v-1] = time

def DFSreverse():
    for x in RevAdjList:
        if x[0] not in visited:
            DFSvisit(x[0])

def SCC(x):
    f = open ('SCC.txt','w')#Put output file on this line
    for i in x:
        print i
        f.write("{}\n".format(','.join([str(n) for n in i])))
    f.close()

def DFSModifiedVisit(v):
    modified_visited.append(v)
    for i in AdjList[v-1][1:]:
        if i not in modified_visited and i in AdjList[v-1][1:]:
            component.append(i)
            DFSModifiedVisit(i)
            incrementZ()
        components.append(component[z:])

def DFSModified():
    for i in orderedSourceVertices:
        if i not in modified_visited:
            component.append(i)
            DFSModifiedVisit(AdjList[i-1][0])
            incrementZ()

DFSreverse()
extra_finish_times = finish_times
temp = zip(finish_times, sourceVertices)
temp.sort(reverse = True)
orderedSourceVertices = [sourceVertices for finish_times, sourceVertices in temp]
print orderedSourceVertices
temp = zip(extra_finish_times, endVertices)
temp.sort(reverse = True)
orderedEndVertices = [endVertices for extra_finish_times, endVertices in temp]
DFSModified()
purifyComponents = []
finalizedComponents = []
for i in components:
    if set(i[0:]).isdisjoint(purifyComponents):
        finalizedComponents.append(i[0:])
        purifyComponents.extend(i[0:])
SCC(finalizedComponents)
