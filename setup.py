from setuptools import setup, find_packages

setup(
    name="DataExplorer",
    version="0.1",
    packages=find_packages(),
    description="A library for data exploration",
    author="Ihor Voznyi, *author*, *author*",
    author_email="ihor.voznyi.sa.2021@lpnu.ua, *email*, *email*",
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
    ],
)
