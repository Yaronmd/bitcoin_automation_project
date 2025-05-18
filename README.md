# Project Overview

This project designed to fetch bitcoin data from api, process, analyze, and visualize data, sends results via email. It includes testing, Dockerization, and structured configuration management.

## 📁 Project Structure

```
├── api
│   ├── __init__.py
│   ├── api_client.py          # Handles API requests
│   └── api_config.json        # API configuration file
├── config                     # Configuration files directory
├── docker-compose.yml         # Docker Compose setup for multi-container environments
├── Dockerfile.app             # Dockerfile for main application
├── Dockerfile.test            # Dockerfile for testing environment
├── helper
│   ├── __init__.py
│   ├── analytics.py           # Data analysis tools
│   ├── config_loader.py       # Load configurations
│   ├── data_fetcher.py        # Fetch and preprocess data
│   ├── email_sender.py        # Email sending logic
│   ├── email_utils.py         # Email utility functions
│   ├── file_utils.py          # File read/write utilities
│   ├── logger_helper.py       # Logging setup
│   └── plot_geneartor.py      # Data visualization
├── main.py                    # run the application
├── poetry.lock                # Poetry lock file for dependency management
├── pyproject.toml             # Project dependencies and configuration
├── README.md                  # Project documentation
├── result
│   ├── btc_price_plot.png     # Output image plot
│   └── data.json              # Raw or processed data output
└── tests                      # test for all components 
    ├── __init__.py
    ├── test_analytics.py
    ├── test_api.py
    ├── test_email.py
    ├── test_file.py
    └── test_plot.py          
```

### Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/)
- Docker & Docker Compose

### Installation

```bash
git clone "https://github.com/Yaronmd/bitcoin_automation_project.git"
cd <project-folder>
poetry install
```

### Running the App

```bash
poetry run python main.py
```

### Using Docker

To build and run the application:

```bash
docker build -f Dockerfile.app -t my-app .
docker run my-app
```

Or use Docker Compose:

```bash
docker-compose up --build
```

Additional Docker Compose commands:

```bash
docker-compose build
docker-compose run app
docker-compose run test
```

## Running Tests

```bash
poetry run pytest
```

Or with Docker:

```bash
docker build -f Dockerfile.test -t my-app-test .
docker run my-app-test
```


## Data Output

Generated graphs and data will be saved to the `result/` folder.

## Configuration

Edit or extend config files in the `config/` or `api/api_config.json`.

Environment variables such as email credentials should be set in `config/.env`

