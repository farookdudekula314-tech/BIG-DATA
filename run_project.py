
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def run_project():

    print("\n================================")
    print(" WEB GRAPH ANALYSIS PROJECT")
    print("================================")

    # Step 1: Small graph analysis
    print("\n1. Running Small Graph Analysis...")
    subprocess.run(
        [sys.executable, "main.py"],
        cwd=BASE_DIR,
        check=True
    )

    # Step 2: Generate large graph if not available
    large_csv = BASE_DIR / "output" / "large_web_graph.csv"

    if not large_csv.exists():
        print("\n2. Generating Large Graph...")
        subprocess.run(
            [sys.executable, "src/large_graph_generator.py"],
            cwd=BASE_DIR,
            check=True
        )

    # Step 3: Large graph analysis
    print("\n3. Running Large Graph Analysis...")
    subprocess.run(
        [sys.executable, "src/large_graph_analysis.py"],
        cwd=BASE_DIR,
        check=True
    )

    # Step 4: Large graph visualization
    print("\n4. Creating Large Graph Visualization...")
    subprocess.run(
        [sys.executable, "src/large_graph_visualization.py"],
        cwd=BASE_DIR,
        check=True
    )

    # Step 5: Launch dashboard
    print("\n5. Starting Streamlit Dashboard...")
    print("Project is ready!")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            "dashboard/app.py"
        ],
        cwd=BASE_DIR,
        check=True
    )


if __name__ == "__main__":
    run_project()
