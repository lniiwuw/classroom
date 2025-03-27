from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # 生产依赖
    extras_require={
        "test": ["pytest", "pytest-cov"]
    }
)