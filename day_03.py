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
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Initital Thoughts:
The first two gave me the input I needed to operate on.  First thing I will need
to do will to make a method that generates the grid.  I should store it in a 2x2
array.  Calculating the number of steps is a simple distance function on the
index of the array

However, there may be an easier way, possible some mathematical correlation
between index and spiral levels/position... Looking at the example, the bottom
right cornwill always be a square number - the levels are square. The values of
the bottom right corners are.
Spiral level    botRt corner     equiv val       steps from origin
0               1               1^2             0
1               9               3^2             2
2               25              5^2             4
3               49              7^2             6
...

Pattern looks like I could figure out the "spiral level" my number belongs in
then calculate the distance where that number sits relative to

'''

def day_03(input):
    pass

if __name__ == '__main__':
    # Your Puzzle Input : 312051
    pass