'''
One solution to the Google foobar zombit_infection challenge.
Created on Feb 10, 2015

@author: sql.sith
'''


def answer(population, x, y, strength):
    # i wish i had a better solution than this.
    # it seems kind of brute-force ... and it uses recursion.
    #
    # if population[x][y] <= strength:
    #   kill that rabbit
    #   try to infect "north/south/east/west", but only within array bounds
    #
    # one comment: i noticed you said x is the column and y is the row,
    # which seems to imply that the population list is addressed as
    # population[y][x], and not as population[x][y]. The test cases given
    # in the readme do not clarify this, as either interpretation would
    # yield the same results. this is not the usual meaning of "row"
    # and "column" in a 2d array. i hope that was deliberate, because
    # i'm going to rewrite this as population[y][x], which seems really
    # odd.

    if population[y][x] <= strength and population[y][x] != -1:
        population[y][x] = -1

        max_y = len(population) - 1
        max_x = len(population[0]) - 1

        # infect west, but try to minimize calls:
        if x - 1 >= 0:
            if population[y][x-1] <= strength and population[y][x-1] != -1:
                population = answer(population, x-1, y, strength)

        # infect east:
        if x + 1 <= max_x:
            if population[y][x+1] <= strength and population[y][x+1] != -1:
                population = answer(population, x+1, y, strength)

        # infect north:
        if y - 1 >= 0:
            if population[y-1][x] <= strength and population[y-1][x] != -1:
                population = answer(population, x, y-1, strength)

        # infect south:
        if y + 1 <= max_y:
            if population[y+1][x] <= strength and population[y+1][x] != -1:
                population = answer(population, x, y+1, strength)

    return(population)

population = [[1, 2, 3],
              [2, 3, 4],
              [3, 2, 1]]
x = 0
y = 0
strength = 2
print(answer(population, x, y, strength))

population = [[6, 7, 2, 7, 6],
              [6, 3, 1, 4, 7],
              [0, 2, 4, 1, 10],
              [8, 1, 1, 4, 9],
              [8, 7, 4, 9, 9],
              [4, 5, 1, 2, 8]]
x = 2
y = 1
strength = 5

print(answer(population, x, y, strength))
