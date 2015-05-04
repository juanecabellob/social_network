import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
      name='django-todo',
      version='1.0',
      packages=['ToDo'],
      include_package_data=True,
      license='License',  # example license
      description='A simple Django app to conduct a ToDo Tracker.',
      long_description=README,
      url='http://www.juancabello.com/',
      author='Juan Cabello',
      author_email='juanecabellob@example.com',
      classifiers=[
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License', # example license
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   # Replace these appropriately if you are stuck on Python 2.
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   ],
      )