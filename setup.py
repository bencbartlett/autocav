import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autocav",
    version="0.0.0",
    author="Ben Bartlett",
    author_email="benbartlett@stanford.edu",
    description="Photonic cavity simulations",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bencbartlett/autocav",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        "numpy",
        "scipy",
        "tqdm"
    ],
)
