def floorFinder():
    with open("Advent_Of_Code_2015/Day_1/input.txt", "r") as file:
        instructions = file.read().strip()

    floor = 0
    count = 0
    for char in instructions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor < 0:
            print(f"Entered basement at instruction position: {count + 1}")
            break
        count += 1
        

    return floor

if __name__ == "__main__":
    final_floor = floorFinder()
    print(f"The final floor is: {final_floor}")