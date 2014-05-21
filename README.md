polished
========

<p align="center">
    <a href="http://www.youtube.com/watch?v=Yi5fHkGqe38">
        <img src="http://img.youtube.com/vi/Yi5fHkGqe38/0.jpg" alt="Polished Example Video">
    </a>
</p>

The goal of polished is to show the awesome progression and amount of tweaks that go into any website. My <a href="http://www.ericcarmichael.com/pages/resume.html">resume</a>
is a good example, dozens of hours of work and tweaking to come up with this pretty basic final product. Showing that
blood, sweat and hilarious tears in between should be pretty entertaining. Watch pages undulate, stretch, break,
grow, and shrink into place.

More explanation available [on my blog](http://www.ericcarmichael.com/polished.html).

### Table of Contents

1. [How does it work?](#how-does-polished-work?)
2. [Installing](#installing)
3. [Usage](#usage)
4. [Configuring](#configuring-behavior)
5. [Backends](#backends)
6. [Example Custom Backend](#custom-backend)
7. [Polishing ugly screenshots](#polishing-certain-commits)
8. [Known Issues](#known-issues)
9. [Acknowledgements](#acknowledgements)


-----------------------------


### How does polished work?

1. Fires up selected backend *(for example, PelicanBackend if you use the [Pelican](https://github.com/getpelican/pelican) blog site generator)*
2. Gets the git revision history
3. Iterates through that history, prepares the page, screen caps it
4. Converts images to video
5. OPTIONALLY: If after reviewing the images/video you find bugs, inherit a backend and `@polish` out the kinks so it's a nice smooth video


### Installing

**Requirements**

1. Mac/Linux
1. NodeJS
2. PhantomJS
3. ffmpeg

Then

```
> pip install polished
```




### Usage

For a static website with no .html generation needed and `index.html` is in the same dir:

```
> polished
```

For a static website with `index.html` in another location

```
> polished "some/path/to/index.html"
```

For a pelican blog:

```
> polished "output/index.html" --backend polished.backends.pelican.PelicanBackend
```




### Configuring behavior

The default backend is `SimpleBackend` which (with no path specified) looks for "index.html" in current directory and
expects static html without any steps needed to generate the page. This default setup probably doesn't work for most
projects.

To expand the behavior, call `polished my/output/index.html --backend my.backend.Backend`





### Backends

**SimpleBackend**

The most basic backend, assumes no steps are needed to generate HTML.

```python
polished.backends.simple.SimpleBackend
```


**PelicanBackend**

For the Pelican blogging system, calls `make html` between screenshots.

```python
polished.backends.pelican.PelicanBackend
```


**DjangoBackend**

For the Django framework, calls `python manage.py syncdb --migrate`

```python
polished.backends.django.DjangoBackend
```





## Custom backend

Generally, on a simple website these backends will care of you, however you may have to
inherit them and add custom behavior

```python
from polished.backends import PelicanBackend

class SomeWeirdBehaviorRequired(PelicanBackend):
    def prepare(self):
        '''
        Prepare your general stuff here! Generate HTML, setup static files, etc.
        '''
        pass

    def cleanup(self):
        '''
        Clean up after yourself, delete static files if you need to
        '''
        pass
```




## Polishing certain commits

Use the `@polish` decorator:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from polished.backends import PelicanBackend
from polished.decorators import polish

class SomeWeirdBehaviorRequired(PelicanBackend):
    def _patch_image_srcs(self):
        wait = WebDriverWait(self.DRIVER, 10)
        element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'img')))

        self.DRIVER.execute_script("""
            var img_array = document.getElementsByTagName('img');

            for(var i=0; i<img_array.length; i++) {
                var href_replaced = img_array[i].getAttribute('src').replace(
                    /^\/images/,
                    "../images"
                );
                img_array[i].setAttribute("src", href_replaced);
            }
        """)

    @polish(urls=["output/pages/about.html"], commit_indexes=range(112, 135))
    def fix_about_me_broken_images(self):
        self._patch_image_srcs()

    @polish(urls=["output/pages/resume.html"], commit_indexes=range(68,134))
    def fix_resume_page_broken_images(self):
        self._patch_image_srcs()
```

### @polish range of commit indexes

```python
@polish(commit_indexes=range(20,30))
def some_func():
    # Polish commits 20 through 30
```



### @polish certain pages

```python
@polish(urls=["index.html", "about.html"])
def some_func():
    # Fix up something with "index.html" and "about.html"
```



### @polish certain pages of certain commits

```python
@polish(urls=["index.html", "about.html"], commit_indexes=range(20,30))
def some_func():
    # Fix up something with "index.html" and "about.html", but only in commits 20 through 30
```



Known issues
============

* It leaves a ton of processes still running for some reason
* Web fonts don't work right with PhantomJS








Acknowledgements
================
Couldn't have done it without this [screenshot script](http://stackoverflow.com/a/18068097) by Aamir Adnan

Thanks [Levi Thomason](https://github.com/levithomason) for always listening to me, encouraging me to improve,
and helping me out in all aspects of life
