from setuptools import setup

setup(
    name = 'osm_diff_tool',
    version = '1.0.1',
    description = 'Tool for use with OpenStreetMap planet diffs.',
    url = 'http://github.com/ethan-nelson/osm_diff_tool',
    author = 'Ethan Nelson',
    author_email = 'ethan-nelson@users.noreply.github.com',
    packages = ['osmdt'],
    license = 'MIT',
    install_requires = ['requests'],
    zip_safe=False
    )
      
