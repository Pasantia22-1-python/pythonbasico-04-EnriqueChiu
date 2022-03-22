from importlib.metadata import entry_points
from setuptools import setup


setup(
    name='pv',
    veriosn='0.1',
    install_requires = [
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)