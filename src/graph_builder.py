
import pandas as pd
import networkx as nx

def build_graph(file_path):

    # Read dataset
    data = pd.read_csv(file_path)

    # Check required columns
    if not {"source", "target"}.issubset(data.columns):
        raise ValueError("CSV must contain source and target columns")

    # Create directed graph
    G = nx.DiGraph()

    # Add website connections
    for _, row in data.iterrows():
        G.add_edge(row["source"], row["target"])

    return data, G