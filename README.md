# Dijkstra Algorithm
## Input type
Dictionary

    "A": {"B": 5, "D": 3},
    "B": {"C": 1},
    "C": {"D": 1},
    "D": {"B": 2}
    
## How to use
Ufortunately, I hadn't implemented user input into the algorithm.
Only way to load own graph is to edit main.py file. Inputing 
vertices by letters, not numbers.
Add line:

    load_file('filename.json')
    dijkstra(loaded_graph, start_node, end_node)

## Technologies
* Python 3.8
* PyCharm IDE
