# pyScarper

A simple HTML web scraper made in Python that I built for learning purposes.

# Contributing

If anyone wants to take this further, bug reports, feature requests and PRs are welcome.

# System Dependencies

1. `python-tkinter`

> [!WARNING]
> TK must be installed through a sepparate package manager (apt, pacman, dnf, etc.) if it didn't come with your python installation.

# How to run it?

### Pull down the code

```bash
git clone https://github.com/PolyCatDev/pyScarper && \
cd pyScarper
```

### Create a Python virtual enviroment and enter it

```bash
python3 -m venv .venv && \
source .venv/bin/activate
```

### Install the dependencies

```bash
pip3 install poetry && poetry install
```

### Run the main.py file

```bash
python3 main.py
```

# How to use it?

1. Paste your link in the text box.
2. Press the download button.
3. A file called `website.html` will appear in the project folder.

# What websites can I scrape?

Any one really, but here is an example: https://quotes.toscrape.com/
