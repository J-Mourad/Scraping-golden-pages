from setuptools import setup, find_packages

setup(
        name='Scraping golden pages',
        version='0.0.1',
        url='https://github.com/J-Mourad/Scraping-golden-pages',
        license='BSD',
        author='J-Mourad',
        packages=find_packages(),
        install_requires=['numpy', 'pandas', 'numpy', 'jupyter', 'matplotlib', 'scipy'],
        entry_points={},
        extras_require={'dev': ['flake8',]},
        )
