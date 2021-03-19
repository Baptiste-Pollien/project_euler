"""
Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20×20 grid?
"""

def look_position(pos, prec, nb_path, to_look):
    """
    Look for the route from prec to pos.
    Update the number of path and the set of position to look
    """
    if pos in nb_path:
        nb_path[pos] += nb_path[prec]
    else:
        nb_path[pos] = nb_path[prec]
        to_look.append(pos)

def compute_nb_routes(size):
    """
    Compute the number of route for a grid of size
    size x size
    """
    nb_path         = {} # Number of path to a positon
    nb_path[(0, 0)] = 1

    to_look         = [(0, 0)] # Position to look for following position

    for (x, y) in to_look:
        if (x < size):
            look_position((x + 1, y), (x, y), nb_path, to_look)

        if(y < size):
            look_position((x, y+1), (x, y), nb_path, to_look)

    return nb_path[(size,size)]

if __name__ == '__main__':
    res = compute_nb_routes(20)
    print(res)