import random
import sys

def generate_maze(width=41, height=21, seed=None):
    if seed is not None:
        random.seed(seed)
    if width % 2 == 0: width += 1
    if height % 2 == 0: height += 1

    maze = [["#" for _ in range(width)] for _ in range(height)]
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    def carve(y, x):
        maze[y][x] = " "
        stack = [(y, x)]
        while stack:
            cy, cx = stack[-1]
            neighbors = []
            for dy, dx in directions:
                ny, nx = cy + dy, cx + dx
                if 1 <= ny < height-1 and 1 <= nx < width-1 and maze[ny][nx] == "#":
                    neighbors.append((ny, nx, dy // 2, dx // 2))
            if neighbors:
                ny, nx, wy, wx = random.choice(neighbors)
                maze[cy + wy][cx + wx] = " "
                maze[ny][nx] = " "
                stack.append((ny, nx))
            else:
                stack.pop()

    start = (1, 1)
    carve(*start)
    goal = (height-2, width-2)
    maze[start[0]][start[1]] = "A"
    maze[goal[0]][goal[1]] = "B"

    return ["".join(row) for row in maze]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python creator.py <width> <height>")
        sys.exit(1)

    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    except ValueError:
        print("Error: width and height must be integers.")
        sys.exit(1)

    maze_lines = generate_maze(width=width, height=height)

    with open("maze.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(maze_lines))

    print(f"Maze ({width}x{height}) has been saved to 'maze.txt'.")