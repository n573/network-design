from graphs import Graph

g = None


def createNetwork():
    global g

    network = {"a": ["c"],
               "b": ["c", "e"],
               "c": ["a", "b", "d", "e"],
               "d": ["c"],
               "e": ["c", "b"],
               "f": []
               }

    g = Graph(network)


def runAlgorithms():
    global g

    print("List of Isolated Networks")
    print(g.find_isolated_vertices())

    print("Path from Network a to e")
    print(g.find_path("a", "e"))

    print("Find all Paths from Network a to e")
    print(g.find_all_paths("a", "e"))

if __name__ == "__main__":
    createNetwork()
    runAlgorithms()
