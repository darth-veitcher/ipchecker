from setuptools import setup
import os
import pypandoc

import ipchecker


current_dir = os.path.abspath(os.path.dirname(__file__))


try:
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r", "")  # YOU  NEED THIS LINE
except OSError:
    print("Pandoc not found. Long_description conversion failure.")
    import io
    # pandoc is not installed, fallback to using raw contents
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()


setup(
    name='ipchecker',
    version=ipchecker.__version__,
    url='',  # TODO: add github link
    license='MIT',
    author='James Veitch',
    author_email='james@jamesveitch.com',
    description='Check IP addresses against configurable white/blacklists.',
    long_description=long_description if long_description else None,
    packages=['ipchecker'],
    zip_safe=False,
    install_requires=open('requirements.txt', 'r').readlines(),
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='ip whitelist blacklist tor',
    python_requires='>=2.7',
)
