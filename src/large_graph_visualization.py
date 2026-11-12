
import pandas as pd
import networkx as nx
from pathlib import Path


from visualization import draw_large_graph

# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = BASE_DIR / "output" / "large_web_graph.csv"

# Image output path
IMAGE_PATH = BASE_DIR / "output" / "large_web_graph.png"

# Read large graph dataset
data = pd.read_csv(DATA_PATH)

# Build directed graph
G = nx.from_pandas_edgelist(
    data,
    source="source",
    target="target",
    create_using=nx.DiGraph()
)

# Create visualization
draw_large_graph(G, IMAGE_PATH)

print("Total Websites:", G.number_of_nodes())
print("Visualization completed successfully!")
