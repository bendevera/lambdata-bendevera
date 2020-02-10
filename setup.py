from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_bendevera",
    version="0.2",
    author="Ben de Vera",
    author_email="ben10devera@gmail.com",
    description="Data helper functions package.",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/bendevera/lambdata-bendevera",
    keywords="data tools pandas",
    packages=find_packages() # ["game_utils"]
)