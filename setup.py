from setuptools import setup, find_packages

setup(
    name="ml_project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires=[
        "numpy>=1.19.5",
        "pandas>=1.3.0",
        "matplotlib>=3.4.2",
        "seaborn>=0.11.1",
        "scikit-learn>=0.24.2",
        "jupyter>=1.0.0",
    ],
    author="Author",
    author_email="author@example.com",
    description="Machine Learning Project analyzing infrared thermography temperature data",
    keywords="machine-learning, data-analysis, thermography",
    python_requires=">=3.6",
)
