from setuptools import setup

setup(
    name="pomo",
    version="1.0",
    py_modules=["pomo"],
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        pomo=pomo:cli
    """,
)
