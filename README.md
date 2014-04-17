polish
======

Only tested on Mac Mavericks


Uses [screenshot script](http://stackoverflow.com/a/18068097) by Aamir Adnan


Getting started
===============

THIS ONLY WORKS ON MAC!

### Install

Install PhantomJS
```
npm install -g phantomjs
```

Install imageMagick

```
pip install polished
```

### Select a backend

- Default backend is "simple" and expects static html without any steps needed to generate the page
- Available backends:

```
'polished.backends.simple'
'polished.backends.pelican'
'polished.backends.django'
```

Generally, on a simple website these backends will probably take care of you, however you may have to
inherit them and add custom behavior

```python
import polished

class SomeWeirdBehaviorRequired(polished.backends.pelican):
    def prepare(self):
        '''
        Prepare your stuff here! Generate HTML, make small changes based on a specific problem, skip
        '''
        pass

    def cleanup(self):
        '''
        Clean up after yourself
        '''
        pass
```


Settings
========

- Set settings file if not polished.py
-
