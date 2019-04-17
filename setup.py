

from setuptools import setup
from yats import __author__, __version__

setup(
  name='uagent',
  version=__version__,
  description='latest user-agent',
  # author=__author__,
  packages=['uagent'],
  install_requires=["requests"],
)

