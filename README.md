<!--<div align="center"><img src="https://mir-s3-cdn-cf.behance.net/project_modules/hd/06a22446366801.5851795421436.gif" width="897"></div>-->
<div align="center"><img src="_assets/logo.jpg"></div>
<h1 align="center">Tengu (天狗)</h1>
An easily deployable WSGI Python Webserver designed with enhanced security in mind.

## Features

- Lightweight and efficient
- WSGI-compliant, making it compatible with various web frameworks
- Easily deployable via Docker
- Simple to run from source code
- Enhanced security measures

## Table of Contents

- [Installation](#installation)
  - [Using Docker](#using-docker)
  - [From Source Code](#from-source-code)
- [Usage](#usage)

## Installation

### Using Docker Build

1. ***Clone the repository:***

   ```bash
   git clone https://github.com/yourusername/tengu.git
   cd tengu
   ```

2. ***Build the Docker Image:***
  ```bash
  docker build -t tengu .
  ```

3. ***Run the Docker Container:***
   ```bash
   docker run -d -p 5000:5000 tengu
   ```

### Docker Compose

***Run Docker Compose***
```bash
docker compose up --build -d
```

## Usage
Once the server is running, you can access it by navigating to http://localhost:5000 in your web browser. You should see a welcome message indicating that Tengu is running.
