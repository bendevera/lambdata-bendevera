from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-bendevera",
    version="1.0",
    author="Ben de Vera",
    author_email="ben10devera@gmail.com",
    description="Gameplay logic for Rock-Paper-Scissors",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/s2t2/game-utils-py",
    keywords="rock paper scissors game",
    packages=find_packages() # ["game_utils"]
)