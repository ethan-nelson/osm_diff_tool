from setuptools import setup

setup(
    name='osm_diff_tool',
    version='1.1.0',
    description='Tool for retrieving OpenStreetMap planet diffs' +
                ' and extracting data.',
    url='http://github.com/ethan-nelson/osm_diff_tool',
    author='Ethan Nelson',
    author_email='git@ethan-nelson.com',
    packages=['osmdt'],
    license='MIT',
    install_requires=['requests'],
    zip_safe=False
)
