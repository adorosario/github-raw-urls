import sys
import requests
import re

def extract_repo_details(repo_url):
    # Extract owner and repo name
    base_pattern = r"github\.com[:/]([\w-]+)/([\w.-]+)"
    base_match = re.search(base_pattern, repo_url)
    if not base_match:
        raise ValueError("Invalid GitHub repository URL provided.")
    
    owner, repo = base_match.groups()
    
    # Extract branch if present in URL
    # This pattern allows for complex branch names with slashes
    branch_pattern = r"/tree/([^/]+(?:/[^/]+)*)"
    branch_match = re.search(branch_pattern, repo_url)
    branch = branch_match.group(1) if branch_match else 'main'
    
    return owner, repo, branch

def get_raw_urls(owner, repo, branch='main'):
    # GitHub API URL to fetch repository contents
    api_url = f'https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1'
    response = requests.get(api_url)
    
    if response.status_code != 200:
        raise ValueError(f"Error accessing repository: {response.json().get('message', 'Unknown error')}")
    
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
    try:
        owner, repo, branch = extract_repo_details(repo_url)
        # print(f"Owner: {owner}")
        # print(f"Repo: {repo}")
        # print(f"Branch: {branch}")
        raw_urls = get_raw_urls(owner, repo, branch)
        # print("\nRaw URLs:")
        for url in raw_urls:
            print(url)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)