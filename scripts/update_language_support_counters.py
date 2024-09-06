import json

# List of languages and files
languages = {
    "🇺🇦": "ukrainian.json",
    "🇵🇱": "polish.json",
    "🇺🇸": "english.json"
}

def count_entries(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return len(data)

def update_readme(counts):
    readme = []

    with open('README.md', 'r', encoding='utf-8') as file:
        readme = file.readlines()
    
    # Find the line where the counters are displayed and update
    for i, line in enumerate(readme):
        if line.startswith("# language support"):
            readme[i + 1] = f"🇺🇦: {counts['🇺🇦']}, 🇵🇱: {counts['🇵🇱']}, 🇺🇸: {counts['🇺🇸']}\n"
            break
    
    # Write the updated README back
    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(readme)

    return readme

if __name__ == "__main__":
    print("starting to count language support")
    counts = {flag: count_entries(file) for flag, file in languages.items()}
    print(f"counts = {counts}")
    readme = update_readme(counts)
    print(f"updated readme: {readme}")
