import os
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with open(file_path, encoding="utf-8") as file:
        content = file.read()
    return content if content else 'no content read'


setup(
    name='mkdocs-random_walk-plugin',
    version='0.1.1',
    author='NoughtQ',
    author_email='noughtq666@gmail.com',
    description='A MkDocs plugin that generates a random link of pages',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown notes random random_walk',
    url='https://github.com/NoughtQ/mkdocs-random_walk-plugin',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10', 
        'Programming Language :: Python :: 3.11', 
        'Programming Language :: Python :: 3.12', 
        'Programming Language :: Python :: 3.13', 
    ],
    entry_points={
        'mkdocs.plugins': [
            'random_walk = mkdocs_random_walk_plugin.plugin:RandomWalkPlugin'
        ]
    },
    include_package_data=True,
    package_data={
        'mkdocs_random_walk_plugin': [
            'random_walk.js'
        ]
    }
)
