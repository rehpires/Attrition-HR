import setuptools
from pathlib import Path

# Read requirements from requirements.txt
requirements_file = Path(__file__).parent / "requirements.txt"
with requirements_file.open() as f:
    required_packages = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setuptools.setup(
    name="Machine-Learning",
    version="0.0.1",
    author="Renato Pires",
    author_email="econrenatopires@gmail.com",
    description="machine learning study and projects",
    long_description="A machine learning study and projects by Renato Pires",
    long_description_content_type="text/markdown",
    url="https://github.com/rehpires/Machine-Learning",
    packages=setuptools.find_packages(),
    install_requires=required_packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)