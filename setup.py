from setuptools import setup, find_packages

setup(
    name="ds-video",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "playwright",
        "pytest",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "ds-video=ds_video.cli:main",
        ],
    },
    author="",
    author_email="",
    description="A Python library to convert markdown to video using ds-markdown and ffmpeg",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)