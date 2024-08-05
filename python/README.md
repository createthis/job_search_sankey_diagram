# Getting Started

I'm using python `3.12`.
```bash
brew install python@3.12
```

I'm also using `venv`, but it's not common to put that under version control.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## install dependencies

You can install dependencies like this:

```bash
python3 -m pip install -r requirements.txt
```

## run

```bash
python3 generate_sankey_diagram.py

# on a mac this opens the html in a browser
open job_application_process_sankey_updated.html
```
