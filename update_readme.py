from process_stats import load_stats, generate_graphs, process_stats

def update_readme():
    stats = load_stats()
    stats_content = process_stats(stats)
    generate_graphs(stats)

    # read the current README file
    graph_path = "nyt_stats_graph.png"
    stats_content += f"\n![Solve Times](./{graph_path})\n"

    # update only the stats section
    with open("README.md", "r") as f:
        lines = f.readlines()

    start_marker = "<!-- START NYT-STATS -->"
    end_marker = "<!-- END NYT-STATS -->"

    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_marker in line:
            start_index = i
        elif end_marker in line:
            end_index = i

    if start_index is not None and end_index is not None:
        lines = lines[:start_index + 1] + [stats_content] + lines[end_index:]
    else:
        # if markers not found, add the markers and content to the end of the README
        lines.append(f"\n{start_marker}\n")
        lines.append(stats_content)
        lines.append(f"{end_marker}\n")

    with open("README.md", "w") as f:
        f.writelines(lines)

    print("README.md updated!")

if __name__ == "__main__":
    update_readme()