from setuptools import setup

setup(
    name="wrike",
    version="0.1.0",
    description="A Python JSON REST API wrapper for the Wrike API",
    url="https://github.com/zackpelster-q/wrike",
    author="Zack Pelster",
    author_email="zack.pelster@qorvo.com",
    license="BSD 2-clause",
    packages=["wrike"],
    install_requires=[
        "certifi==2024.8.30",
        "charset-normalizer==3.3.2",
        "idna==3.10",
        "python-dotenv==1.0.1",
        "requests==2.32.3",
        "urllib3==2.2.3",
    ],
)
