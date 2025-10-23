from setuptools import setup, find_packages
from pathlib import Path

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8") if (HERE / "README.md").exists() else ""

setup(
    name="head_cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "asttokens==3.0.0",
        "click==8.3.0",
        "colorama==0.4.6",
        "executing==2.2.1",
        "i==2.1.0",
        "Pygments==2.19.2",
        "setuptools==80.9.0",
    ],
    entry_points={
        "console_scripts": [
            "head_cli=head_cli.__main__:main",
        ],
    },
    long_description=README,
    long_description_content_type="text/markdown",
)
