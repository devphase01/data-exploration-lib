from setuptools import setup, find_packages

setup(
    name="dataexplore",
    version="0.1.0",
    packages=find_packages(),
    # package_dir={'': ''},
    description="A library for data exploration",
    author="Ihor Voznyi, *author*, *author*",
    author_email="ihor.voznyi.sa.2021@lpnu.ua, *email*, *email*",
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "scipy"
    ],
)
