from setuptools import find_packages, setup

setup(
    name="pnpl",
    version="0.0.5",
    packages=find_packages(),
    install_requires=[
        "mne",
        "mne_bids",
        "numpy",
        "pandas",
        "torch",
        "h5py",
        "huggingface_hub",
        "requests"
    ],
    author="Redacted",
    author_email="Redacted",
    description="Load and process brain datasets for deep learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="Redacted",
    classifiers=[
        "License :: OSI Approved :: BSD-3-Clause License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
