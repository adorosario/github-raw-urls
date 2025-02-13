# github-raw-urls

A lightweight Python tool to list all the raw file URLs in a GitHub repository. Whether you're debugging, automating workflows, or just curious about the structure of a repo, this tool quickly generates direct links to every file hosted on GitHub.

## Features

- **Multiple URL Formats:** Supports HTTPS and SSH GitHub URLs, with or without the `.git` suffix.
- **Recursive File Discovery:** Utilizes the GitHub API to fetch the entire file tree for the default branch (default: `main`).
- **Direct Raw Links:** Constructs and outputs raw URLs that can be used in scripts, automation, or further processing.
- **Dockerized Setup:** Includes Docker and Docker Compose configurations for a seamless containerized experience.

## Installation

### Prerequisites

- Python 3.x
- [Requests](https://pypi.org/project/requests/)

Install the required Python library with:

```bash
pip install requests
```

### Clone the Repository

```bash
git clone https://github.com/adorosario/github-raw-urls.git
cd github-raw-urls
```

## Usage

Run the script by providing a GitHub repository URL as an argument:

```bash
python get_github_raw_urls.py <github_repo_url>
```

### Examples

- **HTTPS URL without `.git`:**

  ```bash
  python get_github_raw_urls.py https://github.com/adorosario/sample-repo
  ```

- **HTTPS URL with `.git`:**

  ```bash
  python get_github_raw_urls.py https://github.com/adorosario/sample-repo.git
  ```

- **SSH URL:**

  ```bash
  python get_github_raw_urls.py git@github.com:adorosario/sample-repo.git
  ```

## How It Works

1. **Extract Repository Details:**  
   The script parses the provided URL to extract the repository owner and name.

2. **Fetch File Tree:**  
   It then calls the GitHub API to retrieve a recursive file tree of the repository's default branch.

3. **Generate Raw URLs:**  
   Finally, the script constructs raw URLs for each file using the base URL format `https://raw.githubusercontent.com/<owner>/<repo>/main/` and prints them out.

## Docker Usage

For those who prefer containerized environments, Docker support is included.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Build the Docker Image

Make sure you are in the project directory and run:

```bash
docker-compose build
```

### Run the Container

Start the container with:

```bash
docker-compose up
```

This will start the service and attach to its logs.

### Access an Interactive Shell

To run the script interactively inside the container:

```bash
docker exec -it github-raw-urls-app-1 /bin/bash
```

Once inside, you can run the script as usual:

```bash
python get_github_raw_urls.py <github_repo_url>
```

### Stopping the Container

Stop the container by pressing `CTRL+C` and then clean up with:

```bash
docker-compose down
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the tool or add new features.

## License

This project is open source. Use, modify, and distribute as needed.
```
