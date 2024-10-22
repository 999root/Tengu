<div align="center"><img src="https://static.myfigurecollection.net/upload/pictures/2023/09/07/3745732.gif" width='1137'></div>
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

### Using Docker

1. **Clone the repository:**

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

## From Source Code
1. ***Clone the repository:***
   ```bash
   git clone https://github.com/999root/tengu.git
   cd tengu
   ```

2. ***Create a virtual environment (optional but recommended):***
   ```bash
   python3 -m venv venv
   source venv/bin/activate # On Windows use 'venv/Scripts/activate'
   ```

3. ***Install the required packages:***
   ```bash
   pip install -r requirements.txt
   ```

4. ***Run the server:***
   ```bash
   py server.py
   ```

## Usage
Once the server is running, you can access it by navigating to http://localhost:8000 in your web browser. You should see a welcome message indicating that Tengu is running.
