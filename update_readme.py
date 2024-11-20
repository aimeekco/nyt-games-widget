from process_stats import load_stats, process_stats

def update_readme():
    stats = load_stats()
    content = process_stats(stats)

    # write to README file
    with open("README.md", "w") as f:
        f.write(content)

    print("README.md updated with the latest stats!")

if __name__ == "__main__":
    update_readme()
