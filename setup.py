from setuptools import setup
import pathlib

# Get the project root directory
here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="py-pomo",
    version="1.0",
    description="A simple CLI pomodoro timer",
    long_description=long_description,
    url="https://github.com/BasicPixel/py-pomo",
    author="Osama AlQudah",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Utilities"
    ],
    keywords="pomodoro, click, cli",
    author_email="osama.mo.qudah@gmail.com",
    py_modules=["pomo"],
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        pomo=pomo:cli
    """,
)
