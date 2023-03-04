'''
Question 12
Suppose you want to prevent communication flow from the node that you found in question 11 to node 10. What is the smallest number of nodes you would need to remove from the graph (you're not allowed to remove the node from the previous question or 10)?

This function should return an integer.
'''

def answer_twelve():
    # YOUR CODE HERE
    G = answer_six()
    g_11 = '97'  #I think `answer_eleven()[0]` may be fine. 
    node = '10'
    return len(nx.minimum_node_cut(G, g_11, node))

    raise NotImplementedError()
    

ans_twelve = answer_twelve()
