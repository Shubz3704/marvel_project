from setuptools import setup, find_packages

setup(
    name="marvelproject",
    version="1.0.0",
    description="A Marvel API client to fetch characters using Streamlit.",
    author="Shubham Mane",
    packages=find_packages(),
    install_requires=[
        "requests",
        "streamlit",
        "python-dotenv",
    ],
)
