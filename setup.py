from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Darshan Patel",
    author_email="dypatel2004@gmail.com",
    install_requires=["openai","langchain","pandas","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)