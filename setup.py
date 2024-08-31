import setuptools

def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

setuptools.setup(
    name="imag",
    version="0.0.1",
    author="darrenwang",
    author_email="wangyang9113@gmail.com",
    description="Image Auto Generator",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/boundles/mvsegmentation3d",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6"
)
