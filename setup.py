from setuptools import setup

setup(name='OpenStreetMap Diff Tool',
      version='1.0.0',
      description='Tool for use with OpenStreetMap planet diffs.',
      url='http://github.com/ethan-nelson/osm_diff_tool',
      author='Ethan Nelson',
      author_email='ethan-nelson@users.noreply.github.com',
      packages=['osmdt'],
      install_requires = ['requests'],
      zip_safe=False)
      
