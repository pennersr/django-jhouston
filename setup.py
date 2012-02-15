#!/usr/bin/env python
from setuptools import setup,find_packages

METADATA = dict(
    name='django-jhouston',
    version='0.1.0',
    author='Raymond Penners',
    author_email='raymond.penners@intenct.nl',
    description='jhouston catches Javascript errors occuring in the browser and automatically posts them to the server.',
    long_description=open('README.rst').read(),
    url='http://github.com/pennersr/django-jhouston',
    keywords='django javascript error',
    install_requires=['django'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    packages=find_packages(),
    package_data={'jhouston': ['static/jhouston/js/*.js' ] }
)

if __name__ == '__main__':
    setup(**METADATA)
    
