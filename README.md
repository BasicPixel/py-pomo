# py-pomo

A simple CLI [pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) timer with many options, made with Python w/ [Click](https://click.palletsprojects.com/) library.

```shell
pip install py-pomo
```

All contibutions are welcome.

---

- [py-pomo](#py-pomo)
- [Usage](#usage)
  - [Installation](#installation)
  - [Local Installation](#local-installation)
  - [Examples](#examples)
  - [Todo](#todo)

# Usage

To use this program, you can either:

1. Download and run the executable file found in the releases page (\*unix only)
2. Install the script as a python module using pip
3. Clone the repo, install and run locally

## Installation

Install by running:

```
pip install py-pomo
```

Then use by running:

```shell
python -m pomo [--OPTIONS]
```

## Local Installation

```shell
git clone https://github.com/BasicPixel/py-pomo.git # Clone this repo
cd py-pomo

virtualenv venv # Start a virtualenv (on unix systems, requires virtualenv package)
. venv/bin/activate

pip install --editable . # Install the package

pomo --help # Run the script
```

## Examples

Start a 25-minute pomo timer:

```shell
pomo
```

Start a timer for 30 seconds:

```shell
pomo -s -d 30

# Or
pomo --in-seconds --duration 30
```

Start a 10-minute timer, with minimal output (MM:SS):

```shell
pomo -m -d 10

# Or
pomo --minimal --duration 10
```

---

Learn more about the available options by running:

```shell
pomo --help
```

## Todo

- [ ] Save configuration to a file
- [x] Publish to PyPI
- [ ] Test on different environments
