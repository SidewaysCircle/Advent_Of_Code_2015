def wrappingCalc():
    with open("Advent_Of_Code_2015/Day_2/input.txt") as f:
        dimensions = f.read().strip().splitlines()

    total_paper = 0
    total_ribbon = 0

    for dim in dimensions:
        l, w, h = map(int, dim.split('x'))
        side1 = l * w
        side2 = w * h
        side3 = h * l

        # Calculate wrapping paper needed
        surface_area = 2 * (side1 + side2 + side3)
        extra_paper = min(side1, side2, side3)
        total_paper += surface_area + extra_paper

        # Calculate ribbon needed
        perimeter1 = 2 * (l + w)
        perimeter2 = 2 * (w + h)
        perimeter3 = 2 * (h + l)
        smallest_perimeter = min(perimeter1, perimeter2, perimeter3)
        bow_length = l * w * h
        total_ribbon += smallest_perimeter + bow_length

    return total_paper, total_ribbon

if __name__ == "__main__":
    paper, ribbon = wrappingCalc()
    print(f"Total wrapping paper needed: {paper}")
    print(f"Total ribbon needed: {ribbon}")

