import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "text-summerizer"
AUTHOR_USER_NAME = "neh-0505"
SRC_REPO = "text-summerizer"
AUTHOR_EMAIL = "nehamohan61772@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    verison=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A samll python package for NLP app",
    long_description=long_description,
    long_decsription_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    pacakges=setuptools.find_packages(where="src")
)