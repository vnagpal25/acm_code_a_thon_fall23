"""
My solution to 'Comrade Connector'
Utilizes Depth First Search (DFS) based graph traversal
"""
from collections import defaultdict

def dfs(graph, node1, node2):
    """
    Returns True if node1 and node2 have a path between them
    Iterative Approach to DFS as the maximum depth of 10^4 overflows the stack
    """
    
    # keep track of visited nodes, prevents cycles from forming
    visited = set()
    
    # DFS relies on a implemented stack in the iterative implementation instead of the call stack
    # pushing first node to stack
    stack = [node1]

    # keep traversing until stack is empty
    while stack:
        # pop off most recently explored node
        current_node = stack.pop()

        # hooray! we have reached the goal node, and there thus exists a path betwen the two nodes
        if current_node == node2:
            return True

        # only consider nodes that haven't been seen
        if current_node not in visited:
            # mark node as visited
            visited.add(current_node)
            
            # push all of the unvisited neighbor nodes of the new node to the stack
            stack.extend(neighbor for neighbor in graph.get(current_node, []) if neighbor not in visited)
    
    # Since DFS is complete, the goal node is in a disconnected component, so return false
    return False


def get_graph_input():
    """Reads terminal input and returns in the form of a graph"""
    # get the number of edges(friendships)
    num_edges = int(input())
    
    # graph will be a dictionary that maps names to lists of friends
    # each friend in a list represents an edge
    graph = defaultdict(list)
    
    # fill out graph edge by edge
    for _ in range(num_edges):
        name1, name2 = input().split()
        graph[name1].append(name2)
        graph[name2].append(name1)
    
    return num_edges, graph    


def main():
    """Main Function"""
    num_edges, friendship_graph = get_graph_input()
    
    # number of test cases
    num_tests = int(input())
    
    # perform DFS to determine if two friends have a path of mutuals connecting them
    for _ in range(num_tests):
        name1, name2 = input().split()
        print(1 if dfs(friendship_graph, name1, name2) else 0)
    
    # vacuous case
    if num_edges == 0:
        print(0)


if __name__=='__main__':
    main()
