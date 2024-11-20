import json

def load_stats():
    with open("nyt_stats.json", "r") as f:
        return json.load(f)

def process_stats(stats):
    results = stats["results"]
    stats_data = results["stats"]
    streaks_data = results["streaks"]

    puzzles_solved = stats_data["puzzles_solved"]
    solve_rate = stats_data["solve_rate"] * 100
    current_streak = streaks_data["current_streak"]
    longest_streak = streaks_data["longest_streak"]

    readme_content = f"# NYT Games Stats\n\n"
    readme_content += f"- **Puzzles Solved:** {puzzles_solved}\n"
    readme_content += f"- **Solve Rate:** {solve_rate:.1f}%\n"
    readme_content += f"- **Current Streak:** {current_streak}\n"
    readme_content += f"- **Longest Streak:** {longest_streak}\n\n"
    readme_content += "## Daily Solve Times\n"
    for day in stats_data["stats_by_day"]:
        readme_content += f"- **{day['label']}:** Best: {day['best_time']}s, Avg: {day['avg_time']}s, Latest: {day['latest_time']}s\n"

    return readme_content

if __name__ == "__main__":
    stats = load_stats()
    content = process_stats(stats)
    print(content)
