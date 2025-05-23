# Problem 3: Find Center of Star Graph

def find_center(edges):
    # check first two edges
    a, b = edges[0]
    c, d = edges[1]

    # return the common node
    if a == c or a == d:
        return a
    else:
        return b
