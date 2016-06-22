
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='dnsprop',
      version='0.1',
      description='DNS prop',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='dns propogation',
      url='https://github.com/aRKosis/dnsprop',
      author='',
      author_email='',
      license='MIT',
      packages=['requests'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['dnsprop=dnsprop.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
