import setuptools

with open("Readme.md","r",encoding="UTF-8") as f:
    long_description=f.read()

__version__="0.0.0"
REPO_NAME="End-to-End-Cancer-Cllassification-using-MLflow-and-DVC"
AUTHOR_USER_NAME="SUDIPTA252002"
SRC_REPO="cnnClassifier"
AUTHOR_EMAIL="sudipmaha123@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small pyhton package for CNN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={
        "Bug-Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue",
    },
    package_dir={"":"src"},
    pakckages=setuptools.find_packages(where="src")

)