from setuptools import setup


try:
    with open('README.md') as readme:
        long_description = readme.read()
except IOError, ImportError:
    long_description = ''

setup(
    name="polish",
    py_modules=["polish"],
    version="0.0.1",
    author="Eric Carmichael",
    author_email="eric@ckcollab.com",
    description="Generates screenshots of a website based on git history",
    long_description=long_description,
    license="MIT",
    keywords="link checker",
    url="https://github.com/ckcollab/polish",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
