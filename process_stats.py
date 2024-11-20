import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def load_stats():
    with open("nyt_stats.json", "r") as f:
        return json.load(f)
    
def process_stats(stats):
    results = stats["results"]["stats"]
    stats_by_day = results["stats_by_day"]
    
    today_date = datetime.now().strftime("%Y-%m-%d")
    today_stats = next((day for day in stats_by_day if day["latest_date"] == today_date), None)

    content = "## "
    content += f"NYT Crossword Stats\n"
    content += f"**Puzzles solved:** {results['puzzles_solved']}\n\n"
    if today_stats:
        today_label = today_stats["label"]
        today_time = today_stats["latest_time"] / 60
        content += f"Today's ({today_label}, {today_date}) Time: {today_time:.1f} minutes\n\n"
    else:
        content += "Haven't done the crossword today yet!\n\n"

    return content

def generate_graphs(stats):
    stats_by_day = stats["results"]["stats"]["stats_by_day"]
    
    days = [day["label"] for day in stats_by_day]
    best_times = [day["best_time"] / 60 for day in stats_by_day]
    avg_times = [day["avg_time"] / 60 for day in stats_by_day]
    latest_times = [day["latest_time"] / 60 for day in stats_by_day]

    bar_width = 0.3
    x = np.arange(len(days))

    plt.figure(figsize=(8, 5), facecolor="#0d1116")

    bars1 = plt.bar(x - bar_width, best_times, width=bar_width, color="#4CAF50", alpha=0.8, label="best")
    bars2 = plt.bar(x, latest_times, width=bar_width, color="#2196F3", alpha=0.8, label="today")
    
    today_index = days.index("Today") if "Today" in days else -1
    if today_index != -1:
        bars2[today_index].set_color("#FF5722")

    for bar, time in zip(bars1, best_times):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f"{time:.1f} min",
                 ha='center', va='center', fontsize=10, color="white", rotation=90)
        
    for bar, time in zip(bars2, latest_times):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f"{time:.1f} min",
                 ha='center', va='center', fontsize=10, color="white", rotation=90)

    plt.xticks(x, days, fontsize=12, fontweight='bold', color="white")
    plt.yticks(fontsize=10)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().yaxis.set_visible(False)
    plt.gca().tick_params(axis='y', which='both', left=False)
    plt.gca().set_facecolor("#0d1116")

    plt.tight_layout()

    # Save the graph
    plt.savefig("nyt_stats_graph.png", dpi=300, bbox_inches='tight', facecolor="#0d1116")
    print("Graph saved as nyt_stats_graph.png")

if __name__ == "__main__":
    stats = load_stats()
    generate_graphs(stats)

