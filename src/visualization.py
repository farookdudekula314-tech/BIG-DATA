
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

def draw_graph(G, output_path):

    # Create output folder if not available
    Path(output_path).parent.mkdir(
        parents=True, exist_ok=True
    )

    # Set graph size
    plt.figure(figsize=(12, 8))

    # Calculate node positions
    pos = nx.spring_layout(G, seed=42)

    # Draw graph
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        edge_color="gray",
        node_size=2500,
        font_size=10,
        font_weight="bold",
        arrows=True,
        arrowsize=20
    )

    plt.title("Web Graph Structure Analysis")
    plt.axis("off")

    # Save graph image
    plt.savefig(output_path, dpi=300, bbox_inches="tight")

    plt.close()

    print("Graph image saved successfully!")

def draw_large_graph(G, output_path):

    import networkx as nx
    import matplotlib.pyplot as plt
    from pathlib import Path

    print("Creating Large Graph Visualization...")

    # Select only 300 websites for visualization
    nodes = list(G.nodes())[:300]

    small_G = G.subgraph(nodes)

    plt.figure(figsize=(14, 10))

    pos = nx.spring_layout(
        small_G,
        seed=42,
        k=0.3
    )

    nx.draw_networkx_nodes(
        small_G,
        pos,
        node_size=20,
        node_color="skyblue"
    )

    nx.draw_networkx_edges(
        small_G,
        pos,
        alpha=0.2,
        arrows=False
    )

    plt.title("Large Web Graph Visualization (300 Website Sample)")
    plt.axis("off")

    Path(output_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    plt.savefig(
        output_path,
        dpi=120,
        bbox_inches="tight"
    )

    plt.close()

    print("Large Graph Visualization Saved!")
