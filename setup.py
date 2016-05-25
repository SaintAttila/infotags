try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# This will always succeed because infotags has no external dependencies. That means you can include
# it in your distribution next to your setup.py script and just assume it will work like I do here.
import infotags

PACKAGE_NAME = 'infotags'

info = infotags.get_info(PACKAGE_NAME)

setup(
    name=PACKAGE_NAME,
    version=info['version'],
    py_modules=['infotags'],
    url=info['url'],
    license=info['license'],
    author=info['author'],
    author_email=info['author_email'],
    description=info['description'],
)
