from setuptools import setup, find_packages

version = '0.0.2'

setup(
    name = 'svnchecker',
    version = version,
    description = "Quick wrapper around svn to run a command before commit",
    long_description = open('README.rst').read(),
    author = "Tom Wardill",
    author_email = "tom.wardill@isotoma.com",
    url = "https://github.com/tomwardill/svnchecker",
    license = "MIT",
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
    ],
    entry_points = {
        'console_scripts': ['svn = svnchecker:main'],
    }
)
