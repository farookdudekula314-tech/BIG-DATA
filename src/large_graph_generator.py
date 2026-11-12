
import networkx as nx
import random
import pandas as pd
from pathlib import Path

def generate_large_graph():

    print("Generating Large Web Graph...")

    # Generate 5000 websites
    G = nx.barabasi_albert_graph(
        5000,
        3,
        seed=42
    )

    # Convert to directed graph
    D = nx.DiGraph()

    for u, v in G.edges():
        D.add_edge(f"Website_{u}", f"Website_{v}")

        if random.choice([True, False]):
            D.add_edge(f"Website_{v}", f"Website_{u}")

    # Save connections
    output_path = (
        Path(__file__).resolve().parent.parent
        / "output"
        / "large_web_graph.csv"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    data = pd.DataFrame(
        D.edges(),
        columns=["source", "target"]
    )

    data.to_csv(output_path, index=False)

    print("Large Graph Generated Successfully!")
    print("Total Websites:", D.number_of_nodes())
    print("Total Connections:", D.number_of_edges())
    print("Saved to:", output_path)

if __name__ == "__main__":
    generate_large_graph()
