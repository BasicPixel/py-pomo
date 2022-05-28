from setuptools import setup, find_packages
import pathlib

# Get the project root directory
here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
readme = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="py-pomo",
    version="1.0.1",
    description="A simple CLI pomodoro timer",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/BasicPixel/py-pomo",
    author="Osama AlQudah",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Utilities"
    ],
    keywords="pomodoro, click, cli",
    author_email="osama.mo.qudah@gmail.com",
    py_modules=["pomo"],
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "pomo=pomo:cli"
        ]
    },
)
