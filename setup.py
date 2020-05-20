import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="similar-sounding-words",
    version="0.1.1",
    description="A list of similar sounding words to help disambiguate voice coding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dusty-phillips/similar-sounding-words",
    py_modules=["similar_sounding_words"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.8",
)
