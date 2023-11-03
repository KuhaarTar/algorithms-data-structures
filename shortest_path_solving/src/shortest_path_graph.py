def read_input(filename):
    """Reads the input file and returns the start point,
    end point, rows, columns, and adjacency matrix.

    Args:
        filename: The name of the input file.

    Returns:
        A tuple containing the start point, end point, rows, columns, and adjacency matrix.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    start_point = tuple(map(int, lines[0].strip().split(",")))
    end_point = tuple(map(int, lines[1].strip().split(",")))

    rows, cols = map(int, lines[2].strip().split(","))

    matrix = []
    for line in lines[3:]:
        row = list(map(int, line.strip()[1:-1].split()))
        matrix.append(row)

    return start_point, end_point, rows, cols, matrix


def find_shortest_path_or_return_none(file_name):
    """Finds the shortest path from the start point
        to the end point in the given graph, or returns None if no path exists.

    Args:
        file_name: The name of the input file.

    Returns:
        The shortest path from the start point to the end point, or None if no path exists.
    """
    s, t, rows, cols, matrix = read_input(file_name)

    visited = [False] * (rows * cols)

    queue = []

    s_index = s[0] * cols + s[1]
    queue.append((s_index, 0))
    visited[s_index] = True

    while queue:
        (s_index, d) = queue.pop(0)

        s_row = s_index // cols
        s_col = s_index % rows

        if (s_row, s_col) == t:
            return d

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = s_row + dr, s_col + dc
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and not visited[new_row * cols + new_col]
            ):
                queue.append((new_row * cols + new_col, d + 1))
                visited[new_row * cols + new_col] = True

    return None


if __name__ == "__main__":
    print(find_shortest_path_or_return_none("../test/input.txt"))
