# Experiments

## Overview
Self-contained notebooks for keyword detection experiments on LibriBrain MEG data.

## Prerequisites

### Environment Variables
Set these before running any notebook:
```bash
export NEPTUNE_API_TOKEN="your_token_here"
export NEPTUNE_PROJECT="your_project_here"
```
Obtain credentials from https://neptune.ai/.

### Dependencies
Notebooks use the modified pnpl library from `../modified-pnpl/` (automatically installed).

## Notebooks

| Notebook | Purpose | Results Location |
|----------|---------|------------------|
| `scaling.ipynb` | Train fraction scaling experiments | `runs/` (or `$OUT_DIR`) |
| `sample-length.ipynb` | Buffer length analysis | `playground/buffer/` |
| `keyword-length.ipynb` | Keyword length comparison | `playground/keyword-length/` |
| `different-keywords.ipynb` | Multiple keyword evaluation | `playground/keywords/` |
| `cleanup.ipynb` | Result cleanup utilities | Minimal output |

## Usage
Each notebook installs dependencies and runs independently. Check the specific `playground/` subdirectory for your notebook's results. We recommend using a Python kernel using a virtual environment.
