try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'Bond IRC Bot',
    'authors': open('./AUTHORS'),
    'url': 'https://darthlukan@github.com/darthlukan/bond.git',
    'download_url': 'http://github.com/darthlukan/bond.git',
    'author_email': 'darthlukan@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'twisted'],
    'packages': ['bond', 'bin'],
    'scripts': [],
    'name': 'bond'
}

setup(**config)   