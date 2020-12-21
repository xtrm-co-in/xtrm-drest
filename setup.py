import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xtrm-drest", # Replace with your own username
    version="0.0.7",
    author="Extreme Solutions",
    author_email="ketan@extremesolutions.in",
    description="Dynamic REST with DRF Writable Nested package for CRUD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="", # https://github.com/pypa/sampleproject
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)