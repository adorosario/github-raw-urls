import sys
import requests
import re

def extract_repo_details(repo_url):
    # Regular expression to extract details from various GitHub URL formats
    match = re.search(r"github\.com[:/](\w+)/(.*?)(\.git|$)", repo_url)
    if not match:
        raise ValueError("Invalid GitHub repository URL provided.")
    owner, repo = match.groups()[:2]
    return owner, repo

def get_raw_urls(owner, repo, branch='main'):
    # GitHub API URL to fetch repository contents
    api_url = f'https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1'
    response = requests.get(api_url)
    data = response.json()
    urls = []

    # Base URL for raw content
    base_raw_url = f'https://raw.githubusercontent.com/{owner}/{repo}/{branch}/'

    # Loop through the contents of the repository
    for file in data.get('tree', []):
        if file['type'] == 'blob':
            raw_url = base_raw_url + file['path']
            urls.append(raw_url)

    return urls

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <github_repo_url>")
        sys.exit(1)

    repo_url = sys.argv[1]
    owner, repo = extract_repo_details(repo_url)
    raw_urls = get_raw_urls(owner, repo)
    for url in raw_urls:
        print(url)

