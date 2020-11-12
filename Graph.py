# Do not change the name of this file or the class name.
class Graph:

    def __init__(self, file_path):
        self.graph_repr = self.store_graph(file_path)
        self.n_nodes = len(self.graph_repr)

    def store_graph(self, file_path):
        """Store graph as an adjacency matrix or adjacency list.

        Arguments:
            file_path (str): path of file storing graph in the following format:
            The first line contains the number of vertices (|V |). The vertices
            are numbered 1 through |V |. Each subsequent line contains a pair of
            vertices such that each such pair defines an edge.

        Returns:
            graph_repr (list of list of int): an adjacency matrix or adjacency
            list storing graph
        """

        #open file and store data in adjacency list

        with open(file_path, "r") as file:
            numVertices = int(file.readline().strip());
            adjList = [[] for _ in range(numVertices)];
            for line in file:
                numbers = line.split();
                num1 = int(numbers[0])
                num2 = int(numbers[1])
                if num2 not in adjList[num1 - 1]:
                    adjList[num1 - 1].append(num2)
                if num1 not in adjList[num2 - 1]:
                    adjList[num2 - 1].append(num1)
        file.close()
        return adjList


    def check_2colorable(self):
        """Determine whether or not the graph is 2-colorable and return colors.

        Returns:
            colors (list of int): a list containing colors of the nodes if
            graph is 2-colorable. The color of each node needs to be one of the
            values 0 or 1. We are not asking for all different possible
            colorings of the graph and the coloring is fine as long as
            nodes of the same color don't share an edge. If graph is not
            2-colorable, return [].
        """

        colorList = [-1] * self.n_nodes;
        queue = [];

        for root in range(self.n_nodes):

            if colorList[root] == -1:

                colorList[root] = 0;
                queue.append(root);

                while len(queue) != 0:

                    u = queue.pop(0);

                    for i in range(len(self.graph_repr[u])):
                        v = self.graph_repr[u][i] - 1;

                        if colorList[v] == -1:

                            if colorList[u] == 0:
                                colorList[v] = 1;
                            elif colorList[u] == 1:
                                colorList[v] = 0;
                            queue.append(v);

                        elif colorList[u] == colorList[v]:
                            return False, [v];

        return True, colorList;


def main():
    #Main function, you can edit as needed
    #Extra import may also be made locally in this function

    graph = Graph('data/smallgraph');
    colors = graph.check_2colorable();
    #print(colors);


if __name__ == '__main__':
    main()
