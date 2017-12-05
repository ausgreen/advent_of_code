'''
You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location
marked 1 and then counting up while spiraling outward. For example, the first
few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must
 be carried back to square 1 (the location of the only access port for this
 memory system) by programs that can only move up, down, left, or right. They
 always take the shortest path: the Manhattan Distance between the location of
 the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your
 puzzle input all the way to the access port?

Initital Thoughts:
The first two gave me the input I needed to operate on.  First thing I will need
to do will to make a method that generates the grid.  I should store it in a 2x2
array.  Calculating the number of steps is a simple distance function on the
index of the array, this array could get big.

However, there may be an easier way, possible some mathematical correlation
between index and spiral levels/position... Looking at the example, the bottom
right cornwill always be a square number - the levels are square. The values of
the bottom right corners are.
Spiral level    max value       equiv val       steps from origin
0               1               1^2             0
1               9               3^2             2
2               25              5^2             4
3               49              7^2             6
...

Pattern looks like I could figure out the "spiral level" my number belongs in
then calculate the distance where that number sits relative to the corner.
Each level is:
    level*2 + 1 numbers wide
by  level*2 + 1 numbers tall    with the origin in the center

so if I can figure out which level it is contained in, I can pinpoint my numbers
location, and the number of steps from origin.

This one gave me a lot of trouble, I'm not going to lie.  I also feel like my
code would not be clear to my future self, or anybody else.,

so to lay out my process,
1. get the number of layers between the origin and my number -> spiral_levels
2. calculate the manhatten distance to a corner on that layer -> corner_distance
3. get values of the corners
4. find the minimum absolute difference (MAD) between mynumber and the corner
    values, my numbers manhatten distance will always be the difference between
    corner_distance and MAD
'''

def get_spiral_level(number):
    '''Calculates the spiral level of the input: number'''
    from math import sqrt, floor, ceil
    return(ceil(floor(sqrt(number))/2))


def get_corners(spiral_level):
    '''
    gets the values of each corner
    returns tuple of corner values (topright, topleft, botleft, botright)
    '''
    bot_right = (spiral_level*2 + 1)**2
    bot_left = bot_right - (spiral_level*2)
    top_left = bot_left - (spiral_level*2)
    top_right = top_left - (spiral_level*2)
    return((top_right, top_left, bot_left, bot_right))


def get_corner_distance(spiral_level):
    '''corner distance is 2*spiral level - 1'''
    return(2*spiral_level)


def day_03(input):
    if input == 1:
        return(0)

    spiral_level = get_spiral_level(input)
    corner_vals = get_corners(spiral_level)
    corner_distance = get_corner_distance(spiral_level)
    print("corner distance : ", corner_distance)
    print("corner vals : ", corner_vals)
    print("spiral level : ", spiral_level)

    # get the distance from the closest corner
    abs_vals = []
    for val in corner_vals:
        abs_vals.append(abs(val - input))
    return(corner_distance - min(abs_vals))


if __name__ == '__main__':
    # Your Puzzle Input : 312051
    print(day_03(312051))



