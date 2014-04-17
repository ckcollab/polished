polished
========

[![Polished example video](http://img.youtube.com/vi/yBTDiGhJjlo/0.jpg)](http://www.youtube.com/watch?v=yBTDiGhJjlo)

The goal of polished is to show the awesome progression and amount of tweaks that go into any website. My resume
is a good example, dozens of hours of work and tweaking to come up with this pretty basic final product. Showing that
blood, sweat and hilarious tears in between should be pretty entertaining. Watch pages undulate, stretch, break,
grow, and shrink into place.


Getting started
===============

THIS ONLY WORKS ON MAC!

### Requirements

1. NodeJS
2. PhantomJS
3. ImageMagick
4. ffmpeg

### Install

```
pip install polished
```

### Configuring behavior

The default backend is `SimpleBackend` which looks for "index.html" in current directory and expects static html
without any steps needed to generate the page. This default setup probably doesn't work for most setups.

To expand the behavior, call `polished --backend my.backend.Backend`


### Basic available backends

`polished.backends.simple.SimpleBackend()`

The most basic backend, assumes no steps are needed to generate HTML.

`polished.backends.pelican.PelicanBackend()`

For the Pelican blogging system, calls `make html` between builds.

`polished.backends.django.DjangoBackend()`

For the Django framework, calls "syncdb --migrate"


Generally, on a simple website these backends will care of you, however you may have to
inherit them and add custom behavior

```python
import polished
import subprocess

class SomeWeirdBehaviorRequired(polished.backends.pelican):
    def prepare(self):
        '''
        Prepare your general stuff here! Generate HTML, setup static files, etc.
        '''


    def cleanup(self):
        '''
        Clean up after yourself, delete static files if you need to
        '''
        pass

    @polish(image=15, html="output/pages/about.html")
    def fix_broken_import(self):
        '''
        So you committed some broken img reference that is breaking image #15 (generally polished/00015.polished.png)
        '''
        all_a_tags = html.cssselect('a')
        for a in all_a_tags:
            a.attrib["href"] = "some_other_url/%s" % a.attrib["href"]
```

@polish(between_shas=("sha1", "sha2"))

@polish(between_images=(1, 3))

@polish(image=1)

@polish(sha="sha")


@skip(between_shas=("sha1", "sha2"))

@skip(between_images=(1, 3))

@skip(image=1)

@skip(sha="sha")





Acknowledgements
================
Couldn't have done it without this [screenshot script](http://stackoverflow.com/a/18068097) by Aamir Adnan
