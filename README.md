polish
======

Only tested on Mac Mavericks




`git rev-list master`


for me i might have to PELICAN_SITE_URL?


how do I get the URLs to traverse? manual input?
file://localhost/Users/eric/src/ericcarmichael/output/index.html


call(['webkit2png', '/Users/eric/src/ericcarmichael/output/index.html'])


Getting started
===============

THIS ONLY WORKS ON MAC!

### Install webkit2png

```
brew install webkit2png
```

### Install polished

```
pip install polished
```

### Select a backend

- Create a polished.py in your root package directory
- Default backend is "simple" and expects static html without any steps needed to generate the page
- Available backends:

```
'polished.backends.simple'
'polished.backends.pelican'
'polished.backends.django'
```

Generally, these backends will not be enough to generate the page you want


Settings
========

- Set settings file if not polished.py
-
