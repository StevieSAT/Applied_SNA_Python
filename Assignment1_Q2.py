## Assignment 1: Question 2 

def answer_two():
    
    # YOUR CODE HERE
    with open('Employee_Movie_Choices.txt', 'r') as f:
        edges = [line.strip().split('\t') for line in f.readlines()[1:]]

    # Create a bipartite graph from the edge list
        G = nx.Graph()
        G.add_edges_from(edges)

    # Add the node attributes to distinguish between employees and movies
        #employees = {node for edge in edges for node in edge if 'E' in node}
        #movies = {node for edge in edges for node in edge if 'M' in node}
        
        G.add_nodes_from(employees, bipartite='0', type='employee')
        G.add_nodes_from(movies, bipartite='1', type='movie')
        node_type = nx.get_node_attributes(G, "type")
        return G
        
    raise NotImplementedError()
    
#plot_graph(answer_two())
#answer_two()
