
import networkx as nx

def analyze_graph(G):

    # Total websites
    total_nodes = G.number_of_nodes()

    # Total connections
    total_edges = G.number_of_edges()

    # In-degree
    in_degree = dict(G.in_degree())

    # Out-degree
    out_degree = dict(G.out_degree())

    # Degree centrality
    degree_centrality = nx.degree_centrality(G)

    # PageRank
    pagerank = nx.pagerank(G)

    # Prepare results
    results = []

    for website in G.nodes():

        results.append({
            "Website": website,
            "In-Degree": in_degree[website],
            "Out-Degree": out_degree[website],
            "Degree Centrality": round(
                degree_centrality[website], 3
            ),
            "PageRank": round(pagerank[website], 4)
        })

    return total_nodes, total_edges, results
