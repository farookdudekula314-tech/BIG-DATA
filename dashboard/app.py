
from pathlib import Path
import sys
import pandas as pd
import streamlit as st

# Project folder path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# File paths
OUTPUT_DIR = BASE_DIR / "output"
CSV_PATH = OUTPUT_DIR / "graph_analysis.csv"
GRAPH_PATH = OUTPUT_DIR / "web_graph.png"

# Page settings
st.set_page_config(
    page_title="Web Graph Analysis",
    page_icon="🌐",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #101827;
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
[data-testid="stMetric"] {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #334155;
}
</style>
""", unsafe_allow_html=True)

# Dashboard heading
st.title("🌐 Web Graph Structure Analysis")
st.write("Website Connections and Network Analysis Dashboard")

st.divider()

# Check analysis file
if not CSV_PATH.exists():
    st.error("Analysis file not found. First run: python main.py")
    st.stop()

# Load results
df = pd.read_csv(CSV_PATH)

# Summary cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Websites", len(df))
col2.metric("Total Connections", int(
    df["In-Degree"].sum()
))

col3.metric(
    "Highest PageRank",
    df.loc[df["PageRank"].idxmax(), "Website"]
)

st.divider()

# Website analysis
st.header("📊 Website Analysis")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# Degree analysis
st.header("📈 Degree Analysis")

degree_data = df.set_index("Website")[
    ["In-Degree", "Out-Degree"]
]

st.bar_chart(degree_data)

# PageRank analysis
st.header("⭐ PageRank Comparison")

pagerank_data = df.set_index("Website")[["PageRank"]]

st.bar_chart(pagerank_data)

# Graph visualization
st.header("🕸️ Website Network Graph")

if GRAPH_PATH.exists():
    st.image(
        str(GRAPH_PATH),
        caption="Web Graph Structure",
        use_container_width=True
    )
else:
    st.warning("Graph image not found. Run python main.py first.")

# Website details
st.header("🔍 Explore a Website")

website = st.selectbox(
    "Select a website",
    df["Website"].tolist()
)

selected = df[df["Website"] == website].iloc[0]

a, b, c = st.columns(3)

a.metric("In-Degree", int(selected["In-Degree"]))
b.metric("Out-Degree", int(selected["Out-Degree"]))
c.metric("PageRank", selected["PageRank"])

st.divider()

st.success("Dashboard Loaded Successfully!")
st.caption("Web Graph Structure Analysis Using Big Data")
# Large Graph Analysis
st.divider()

st.header("🌐 Large Web Graph Analysis")

LARGE_CSV_PATH = OUTPUT_DIR / "large_graph_analysis.csv"

if LARGE_CSV_PATH.exists():

    large_df = pd.read_csv(LARGE_CSV_PATH)

    col1, col2 = st.columns(2)

    col1.metric(
        "Large Graph Websites",
        len(large_df)
    )

    col2.metric(
        "Large Graph Connections",
        int(large_df["In-Degree"].sum())
    )

    st.subheader("🏆 Top 10 Websites by PageRank")

    top10 = large_df.sort_values(
        by="PageRank",
        ascending=False
    ).head(10)

    st.dataframe(
        top10,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("📊 Top 10 PageRank Comparison")

    st.bar_chart(
        top10.set_index("Website")[["PageRank"]]
    )

else:
    st.warning("First run large_graph_analysis.py")
# Large Graph Visualization
st.divider()

st.header("🕸️ Large Web Graph Visualization")

LARGE_GRAPH_IMAGE = OUTPUT_DIR / "large_web_graph.png"

if LARGE_GRAPH_IMAGE.exists():

    st.image(
        str(LARGE_GRAPH_IMAGE),
        caption="Large Web Graph - 300 Website Sample",
        use_container_width=True
    )

else:
    st.warning("Large graph image not found.")