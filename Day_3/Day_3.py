def deliveryMap():
    with open("Advent_Of_Code_2015/Day_3/input.txt") as file:
        directions = file.read().strip()

    # Initialize starting position and visited houses set
    robotX, robotY = 0, 0
    santaX, santaY = 0, 0
    x, y = 0, 0
    visited_houses = {(x, y)}

    # Map directions to coordinate changes
    move_map = {
        '^': (0, 1),
        'v': (0, -1),
        '>': (1, 0),
        '<': (-1, 0)
    }
    for i, direction in enumerate(directions):
        if i % 2 == 0:  # Santa's turn
            dx, dy = move_map[direction]
            santaX += dx
            santaY += dy
            visited_houses.add((santaX, santaY))
        else:  # Robot's turn
            dx, dy = move_map[direction]
            robotX += dx
            robotY += dy
            visited_houses.add((robotX, robotY))
    return len(visited_houses)

if __name__ == "__main__":
    total_houses = deliveryMap()
    print(f"Total unique houses that received at least one present: {total_houses}")