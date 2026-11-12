
from pathlib import Path
import sys
import pandas as pd

# Main project folder path
BASE_DIR = Path(__file__).resolve().parent

# Allow Python to access the src folder
sys.path.insert(0, str(BASE_DIR))

# Import our project modules
from src.graph_builder import build_graph
from src.graph_analysis import analyze_graph
from src.visualization import draw_graph

# Dataset path
DATA_PATH = BASE_DIR / "dataset" / "web_links.csv"

# Output folder and file paths
OUTPUT_DIR = BASE_DIR / "output"
GRAPH_PATH = OUTPUT_DIR / "web_graph.png"
CSV_PATH = OUTPUT_DIR / "graph_analysis.csv"

def main():

    print("\n===================================")
    print(" WEB GRAPH STRUCTURE ANALYSIS")
    print("===================================")

    # Check whether dataset exists
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        )

    # Create output folder
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: Build the graph
    print("\nStep 1: Building Web Graph...")

    data, G = build_graph(DATA_PATH)

    print("Graph created successfully!")

    # Step 2: Analyze the graph
    print("\nStep 2: Analyzing Web Graph...")

    total_nodes, total_edges, results = analyze_graph(G)

    # Display graph details
    print("\nTotal Websites:", total_nodes)
    print("Total Connections:", total_edges)

    print("\nWebsites:")
    print(list(G.nodes()))

    print("\nWebsite Connections:")
    print(list(G.edges()))

    # Display analysis table
    results_df = pd.DataFrame(results)

    print("\nWebsite Analysis Results:")
    print(results_df.to_string(index=False))

    # Find the most connected website
    degree_values = dict(G.degree())
    most_connected = max(
        degree_values,
        key=degree_values.get
    )

    print("\nMost Connected Website:", most_connected)

    # Save analysis results
    results_df.to_csv(CSV_PATH, index=False)

    # Step 3: Draw and save graph
    print("\nStep 3: Creating Graph Visualization...")

    draw_graph(G, GRAPH_PATH)

    print("\nAnalysis results saved to:", CSV_PATH)
    print("Graph image saved to:", GRAPH_PATH)

    print("\n===================================")
    print(" PROJECT COMPLETED SUCCESSFULLY!")
    print("===================================")

if __name__ == "__main__":
    main()