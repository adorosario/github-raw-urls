# Docker Quickstart

This document explains how to build and run the Python program using Docker, and shows examples of different GitHub URL formats accepted by the script.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) must be installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) is required.

## Building the Docker Image

Make sure you are in the project directory (where the Dockerfile and docker-compose.yml are located) and run:

```bash
docker-compose build
```

This command builds the Docker image as defined in your Dockerfile citeturn0file0.

## Running the Container

Start the container with:

```bash
docker-compose up
```

This command starts the container defined as the `app` service (see docker-compose.yml citeturn0file0). By default, docker-compose attaches to the container's logs.

## Getting an Interactive Shell

If you need to access an interactive bash shell inside the running container, execute:

```bash
docker exec -it github-raw-urls-app-1 /bin/bash
```

This command attaches you to the running container so you can run commands interactively.

## Running the Python Program

Once you have access to the shell, you can run your Python script manually. The script `get_github_raw_urls.py` accepts GitHub repository URLs in several formats. Here are some examples:

### Example 1: Using SSH URL Format

```bash
python get_github_raw_urls.py git@github.com:adorosario/wordpress-to-customgpt.git
```

*Explanation:*  
This format is the SSH version of the GitHub URL. It is useful when you have SSH keys set up for authentication. The URL includes the username (`git@github.com`) and the repository path (`adorosario/wordpress-to-customgpt.git`).

### Example 2: Using HTTPS URL without .git Suffix

```bash
python get_github_raw_urls.py https://github.com/adorosario/apify-customgpt
```

*Explanation:*  
This HTTPS format does not include the `.git` suffix. The script is designed to handle this format by extracting the repository owner and name correctly.

### Example 3: Using HTTPS URL with .git Suffix

```bash
python get_github_raw_urls.py https://github.com/adorosario/apify-customgpt.git
```

*Explanation:*  
This is the HTTPS format with the `.git` suffix. It functions similarly to the previous example, and the script can extract the necessary details to build the raw URLs for the repository files.

## Stopping the Container

If you started the container with `docker-compose up`, you can stop it by pressing `CTRL+C`. Then, clean up the container and network by running:

```bash
docker-compose down
```

## Summary

- **Build the image:** `docker-compose build`
- **Run the container:** `docker-compose up`
- **Get an interactive shell:** `docker exec -it github-raw-urls-app-1 /bin/bash`
- **Run the Python program:**  
  Use one of the following examples:
  - SSH URL:  
    `python get_github_raw_urls.py git@github.com:adorosario/wordpress-to-customgpt.git`
  - HTTPS URL without .git:  
    `python get_github_raw_urls.py https://github.com/adorosario/apify-customgpt`
  - HTTPS URL with .git:  
    `python get_github_raw_urls.py https://github.com/adorosario/apify-customgpt.git`
- **Stop the container:** `docker-compose down`

For more detailed information, please refer to the [Docker documentation](https://docs.docker.com/).

---