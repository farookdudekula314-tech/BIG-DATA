
import pandas as pd
import networkx as nx
from pathlib import Path


def analyze_large_graph():

    print("\nLARGE WEB GRAPH ANALYSIS")

    BASE_DIR = Path(__file__).resolve().parent.parent

    DATA_PATH = BASE_DIR / "output" / "large_web_graph.csv"
    OUTPUT_PATH = BASE_DIR / "output" / "large_graph_analysis.csv"

    # Read generated graph dataset
    data = pd.read_csv(DATA_PATH)

    # Create directed graph
    G = nx.from_pandas_edgelist(
        data,
        source="source",
        target="target",
        create_using=nx.DiGraph()
    )

    print("\nTotal Websites:", G.number_of_nodes())
    print("Total Connections:", G.number_of_edges())

    # Calculate degree values
    in_degree = dict(G.in_degree())
    out_degree = dict(G.out_degree())

    # Calculate PageRank
    pagerank = nx.pagerank(G)

    # Prepare results
    results = []

    for website in G.nodes():

        results.append({
            "Website": website,
            "In-Degree": in_degree[website],
            "Out-Degree": out_degree[website],
            "PageRank": round(pagerank[website], 6)
        })

    # Save analysis
    result_df = pd.DataFrame(results)

    result_df.to_csv(OUTPUT_PATH, index=False)

    print("\nTop 10 Websites by PageRank:")

    print(
        result_df.sort_values(
            by="PageRank",
            ascending=False
        ).head(10).to_string(index=False)
    )

    print("\nAnalysis saved successfully!")
    print("File:", OUTPUT_PATH)


if __name__ == "__main__":
    analyze_large_graph()
