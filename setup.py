from setuptools import find_packages, setup

setup(
    name="types-requests-mypy-error",
    version="0.0.1",
    author="Bader AlAttar",
    author_email="baderalattar22@gmail.com",
    description="",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests"
    ],
    extras_require={
        "dev": [
            "mypy",
            "types-requests",
        ],
    },
)
