from setuptools import setup, find_packages

setup(
    name="captain_kube",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "kubernetes",
        "click",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "captain-kube=captain_kube:cli",
        ],
    },
    include_package_data=True,
)