def update_readme():
    stats = load_stats()
    content = process_stats(stats)

    # read current README
    with open("README.md", "r") as f:
        readme = f.read()

    # replace placeholder <!-- NYT-STATS --> with the new content
    updated_readme = readme.replace(
        "<!-- NYT-STATS -->",
        content
    )

    # write updated content back to the README file
    with open("README.md", "w") as f:
        f.write(updated_readme)

    print("README.md updated with the latest stats!")

if __name__ == "__main__":
    update_readme()