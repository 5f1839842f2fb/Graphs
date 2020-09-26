
def earliest_ancestor(ancestors, starting_node):
    # tree = dict(ancestors) # wont work because making a dict from tuples overwrites keys intead of adding additional values when key is used again
    tree = {}
    for pair in ancestors:
        if pair[1] not in tree:
            tree[pair[1]] = {pair[0]}
        else:
            tree[pair[1]].add(pair[0])
    #print(tree)
    
    if starting_node not in tree:
        return -1

    lineages = []
    visited = set()
    paths = [[starting_node]]
    while len(paths) > 0:
        path = paths.pop(0)
        node = path[-1]
        if node not in tree:
            lineages += [path]
        elif node not in visited:
            visited.add(node)
            for edge in tree[node]:
                paths += [path + [edge]]
    lineages.sort(key=lambda element: (len(element), -element[-1])) # sorts lineages by last node value (reversed) and length
    return lineages[-1][-1]
if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1), (12, 2)]
    print(earliest_ancestor(test_ancestors, 6))