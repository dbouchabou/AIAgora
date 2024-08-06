from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="AIAgora",
    version="0.1.0",
    author="Damien Bouchabou",
    author_email="@example.com",
    description="A communication bus for AI agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbouchabou/AIAgora",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pydantic>=1.10.7,<2.0.0",
    ],
)
