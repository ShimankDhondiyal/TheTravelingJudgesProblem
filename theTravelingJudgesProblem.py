"FIND PATH OF LEAST COST GIVEN WEIGHTED GRAPH"
import networkx as nx

def makeGraph(numberCities, graph):
    for city in range(1, numberCities + 1):
        graph.add_node(city)

def makeEdge(city1, city2, distance, graph):
    graph.add_edge(city1, city2, weight = distance)
    
def testMethod(graph, line, destination):
    numberJudges = line[0]
    cities = []
    line = line[2:]
    #keep track of all initial cities
    for city in line.split():
        cities.append(int(city))
    #see if any non-starting cities can meet with starting cities, pick best one = steinerNode
    steinerDistance = 0
    steinerNode = None
    for node in graph:
        if cities.__contains__(node) or node == destination:
            continue
        #see if this node can reach all the startingCities
        totalDistance = 0
        for city in cities:
            path = list(nx.shortest_path(graph, node, city))
            distance = nx.shortest_path_length(graph, node, city, weight = 'weight')
            totalDistance += distance
        if steinerDistance == 0:
            steinerDistance = totalDistance
            steinerNode = node
            continue
        if totalDistance < steinerDistance:
            steinerDistance = totalDistance
            steinerNode = node

    #Print the paths
    iteration = 1
    totalCost = 0
    for city in cities:
        #get path/distance from startingCity to steinerNode
        path = list(nx.shortest_path(graph, city, steinerNode))
        cost = nx.shortest_path_length(graph, city, steinerNode, weight = 'weight')
        pathSD = list(nx.shortest_path(graph, steinerNode, destination))
        if iteration == 1:
            totalCost += cost
            totalCost += nx.shortest_path_length(graph, steinerNode, destination, weight = 'weight')
            for t in cities:
                if t == city:
                    continue
                totalCost += nx.shortest_path_length(graph, t, steinerNode, weight = 'weight')
            print("distance =", totalCost)
            print("   ", end = '')
            count = 0
            for node in path:
                if count == 0:
                    print(str(node), end='')
                    count += 1
                    continue
                print("-" + str(node), end = '')
            for node in pathSD:
                if node == steinerNode:
                    continue
                print("-" + str(node), end = '')
            iteration += 1
        else:
            print()
            print("   ", end = '')
            count = 0
            for node in path:
                if count == 0:
                    print(str(node), end='')
                    count += 1
                    continue
                print("-" + str(node), end = '')
            for node in pathSD:
                if node == steinerNode:
                    continue
                print("-" + str(node), end = '')

def main():
    #create a file
    file = open("input.txt", "w")
    #add text to the file
    file.write("8 6 11\n")
    file.write("1 8 1\n")
    file.write("1 5 2\n") 
    file.write("2 3 1\n")
    file.write("2 7 1\n")
    file.write("3 4 3\n")
    file.write("3 8 2\n")
    file.write("4 6 3\n")
    file.write("4 8 2\n")
    file.write("5 6 1\n")
    file.write("6 7 2\n")
    file.write("6 8 2\n")
    file.write("3 1 4 3\n")
    file.write("\n")
    
    file.write("4 4 3\n")
    file.write("1 3 1\n")
    file.write("2 3 2\n") 
    file.write("3 4 2\n")
    file.write("2 1 2\n")
    file.write("\n")

    file.write("5 3 5\n")
    file.write("1 2 1\n")
    file.write("2 3 2\n")
    file.write("3 4 3\n")
    file.write("4 5 1\n")
    file.write("2 4 2\n")
    file.write("2 5 1\n")
    file.write("-1\n")

    file.close()

    f= open("input.txt", "r")
    line = f.readline()
    graph = nx.Graph()
    case = 1
    isFirstline = True
    iteration = 1
    while line != "-1\n":
        #if were on blank line, read next
        if line == "\n":
            line = f.readline()
        #first line, get info
        if isFirstline:
            numberCities = 0
            destination = 0
            numberRoads = 0
            for a in line.split():
                if numberCities == 0:
                    numberCities = int(a)
                elif destination == 0:
                    destination = int(a)
                else:
                    numberRoads = int(a)
            makeGraph(numberCities, graph)
            isFirstline = False
            line = f.readline()
            continue
        #middle lines, get edges
        if iteration <= numberRoads:
            city1 = int(line[0])
            city2 = int(line[2])
            distance = int(line[4])
            makeEdge(city1, city2, distance, graph)
            iteration += 1
            line = f.readline()
            continue
        #last line, print
        else:
            print("Case ", str(case) + ":")
            testMethod(graph, line, destination)
            iteration = 1
            case += 1
            print("\n")
            isFirstline= True
            graph.clear()
            line = f.readline()

main()