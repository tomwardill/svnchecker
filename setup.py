from setuptools import setup, find_packages

version = '0.0.2'

setup(
    name = 'svnchecker',
    version = version,
    description = "",
    long_description = "",
    author = "",
    author_email = "",
    url = "",
    license = "",
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
    ],
    entry_points = {
        'console_scripts': ['svn = svnchecker:main'],
    }
)
