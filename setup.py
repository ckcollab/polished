from setuptools import setup


try:
    with open('README.md') as readme:
        long_description = readme.read()
except (IOError, ImportError):
    long_description = ''


# Depends on
# pip install git+https://github.com/adamn/python-webkit2png.git@6488a1fbd06d5479f8592af47acc73834647e837

setup(
    # requires selenium
    name="polished",
    py_modules=["polished"],
    version="0.0.1",
    author="Eric Carmichael",
    author_email="eric@ckcollab.com",
    description="Generates screenshots of a website based on git history",
    long_description=long_description,
    license="MIT",
    keywords="link checker",
    url="https://github.com/ckcollab/polished",
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