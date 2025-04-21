# ds5111lab04

# Chrome Headless Browser and Python Environment Setup

This repository sets up a Python environment with Google Chrome in headless mode, useful for web scraping and automation. Designed for reproducibility on a fresh VM (e.g., AWS EC2).

## Purpose

Automate setup for a headless browser data collection project. Output is a CSV file (`ygainers.csv`) scraped from the web.

## Requirements

- Ubuntu 20.04+ (tested on AWS EC2)
- Python 3.12
- Git with SSH access
- Internet access

## What’s Included

- `init.sh`: Installs base tools (`make`, `python3.12-venv`, `tree`)
- `install_chrome.sh`: Installs Google Chrome in headless mode
- `Makefile`: Automates environment setup and test runs
- `requirements.txt`: Python dependencies (`pandas`, `lxml`)
- `scrape_gainers.py`: Sample script using headless Chrome
- `ygainers.csv`: Sample output

## 1. VM Setup

### 1.1 Update and Install Base Packages

Manually run:

```bash
sudo apt update
```

Then run:

```bash
./init.sh
```

This installs:

- `make`
- `python3.12-venv`
- `tree`

### 1.2 Git + SSH Setup

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
```

Add the key to your GitHub SSH settings.

Clone the repo:

```bash
git clone git@github.com:your-username/your-repo.git
cd your-repo
```

## 2. Project Setup

### 2.1 Install Chrome

```bash
./scripts/install_chrome.sh
```

Test:

```bash
google-chrome --headless --disable-gpu --dump-dom https://example.com
```

### 2.2 Set Up Python Environment

```bash
make update
```

Installs dependencies into `env/`.

### 2.3 Run a Sample Job

```bash
make ygainers.csv
```

Creates `sample_data/ygainers.csv`.

## Example Structure

```bash
.
├── init.sh
├── Makefile
├── README.md
├── requirements.txt
├── sample_data/
│   └── ygainers.csv
└── scripts/
    ├── install_chrome.sh
    ├── scrape_gainers.py
    └── setup_git.sh
```

## Notes

- `env/` is ignored from version control
- All scripts should be executable (`chmod +x filename`)
- Output is saved to `sample_data/`

## Troubleshooting

- **Chrome not found:** Re-run `install_chrome.sh`
- **Python venv error:** Confirm Python 3.12 is installed
- **Git SSH error:** Check if your key is added to GitHub
