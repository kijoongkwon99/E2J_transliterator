from setuptools import setup, find_packages

setup(
    name="eng2jap",
    version="0.1.0",
    description="English-to-Japanese phonetic transliterator",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="kijoongkwon",
    author_email="kijoongkwon.kaist.ac.kr",
    url="https://github.com/yourname/E2J_transliterator",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "phonemizer>=3.3.0",
        "segments>=2.3.0",
        "regex",
        "joblib",
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
    ],
)
