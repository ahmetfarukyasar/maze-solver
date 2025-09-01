# Maze Solver

A Python implementation of pathfinding algorithms for maze solving, featuring both Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms with visualization capabilities.

## Features

- **Multiple Search Algorithms**: Choose between DFS and BFS for different solving strategies
- **Maze Generation**: Create random mazes with customizable dimensions
- **Visual Output**: Generate PNG images showing the solution path and explored areas
- **Performance Metrics**: Track the number of states explored during solving
- **Flexible Input**: Support for custom maze files or generated mazes

## Installation

### Prerequisites
- Python 3.6 or higher
- PIL (Pillow) for image generation

### Setup
```bash
# Clone the repository
git clone https://github.com/ahmetfarukyasar/maze-solver.git
cd maze-solver

# Install dependencies
pip install Pillow
```

## Usage

### Generating a Maze
Create a random maze with specified dimensions:

```bash
python creator.py <width> <height>
```

**Examples:**
```bash
python creator.py 21 21    # Creates a 21x21 maze
python creator.py 41 31    # Creates a 41x31 maze
```

This generates a `maze.txt` file in the current directory.

### Solving a Maze
Solve an existing maze using DFS or BFS:

```bash
python maze.py <maze_file> [algorithm]
```

**Parameters:**
- `maze_file`: Path to the maze text file
- `algorithm`: Optional. Choose `dfs` (default) or `bfs`

**Examples:**
```bash
python maze.py maze.txt        # Solve using DFS (default)
python maze.py maze.txt dfs    # Solve using DFS explicitly
python maze.py maze.txt bfs    # Solve using BFS
```

## Maze File Format

Maze files should be text files with the following characters:
- `A`: Start position (exactly one required)
- `B`: Goal position (exactly one required)
- `#` or any non-space character: Walls
- ` ` (space): Open paths

**Example maze file:**
```
#################
#A      #       #
##### # # ##### #
#   # #   #   # #
# # ##### # # # #
# #       # # # #
# ####### ### # #
#         #   # #
####### ### ### #
#     #   #   # #
# ### ### # ### #
# #   #   #   # #
# # ### ##### # #
# #   #       # #
# ### ######### #
#   #           B#
#################
```

## Algorithm Comparison

| Algorithm | Strategy | Optimal Solution | Memory Usage | Exploration Pattern |
|-----------|----------|------------------|--------------|-------------------|
| **DFS** | Depth-First | ❌ No | Lower | Deep exploration |
| **BFS** | Breadth-First | ✅ Yes | Higher | Level-by-level |

### DFS (Depth-First Search)
- Explores as far as possible along each branch before backtracking
- Uses a stack (LIFO) data structure
- Generally faster but may not find the shortest path
- Lower memory usage

### BFS (Breadth-First Search)
- Explores all neighbors at the current depth before moving deeper
- Uses a queue (FIFO) data structure
- Guarantees the shortest path (optimal solution)
- Higher memory usage

## Output

The program provides:

1. **Console Output**:
   - Original maze visualization
   - Algorithm selection confirmation
   - Number of states explored
   - Solved maze with solution path marked by `*`

2. **Image Output**:
   - `maze.png`: Visual representation with color coding
   - **Red**: Start position (A)
   - **Green**: Goal position (B)
   - **Yellow**: Solution path
   - **Light Red**: Explored areas
   - **Dark Gray**: Walls
   - **Light Gray**: Open paths

## Code Structure

### Core Classes

- **`Node`**: Represents a state in the search tree
- **`StackFrontier`**: LIFO frontier for DFS
- **`QueueFrontier`**: FIFO frontier for BFS  
- **`Maze`**: Main maze class with solving capabilities

### Key Methods

- `Maze.solve(algorithm)`: Solves the maze using specified algorithm
- `Maze.neighbors(state)`: Returns valid neighboring positions
- `Maze.print()`: Displays maze in console
- `Maze.output_image()`: Generates visual PNG output
- `generate_maze()`: Creates random maze using recursive backtracking

## Examples

### Quick Start
```bash
# Generate a maze and solve it with BFS
python creator.py 25 25
python maze.py maze.txt bfs
```

### Comparing Algorithms
```bash
# Generate a maze
python creator.py 31 31

# Solve with DFS
python maze.py maze.txt dfs

# Solve with BFS  
python maze.py maze.txt bfs
```

## Performance Notes

- **DFS** typically explores fewer states but may find longer paths
- **BFS** explores more states but guarantees the shortest path
- Larger mazes will show more pronounced differences between algorithms
- The `show_explored=True` parameter in image output helps visualize the search patterns

## Contributing

Feel free to submit issues and enhancement requests. When contributing:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Acknowledgments

This implementation is inspired by classic AI pathfinding algorithms and educational materials (CS50) on search algorithms in artificial intelligence.