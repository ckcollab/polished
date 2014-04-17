'''
I snagged this from http://stackoverflow.com/a/18068097 written by Aamir Adnan

Usage examples

    screen_path, crop_path, thumbnail_path = get_screen_shot(
        url=url, filename='sof.png',
        crop=True, crop_replace=False,
        thumbnail=True, thumbnail_replace=False,
        thumbnail_width=200, thumbnail_height=150,
    )

    get_screen_shot(
        url="http://google.com",
        path="polished/"
    )
'''

import os
from subprocess import Popen, PIPE
from selenium import webdriver

abspath = lambda *p: os.path.abspath(os.path.join(*p))
#ROOT = abspath(os.path.dirname(__file__))

DEFAULTS = {
    "path": "polished/",
    "width": 1386,
    "height": 1024,
}


def execute_command(command):
    #result = Popen(command, shell=True, stdout=PIPE).stdout.read()
    result = Popen(command, stdout=PIPE).stdout.read()
    if len(result) > 0 and not result.isspace():
        raise Exception(result)


def do_screen_capturing(url, screen_path, width, height):
    print "Capturing screen.."
    driver = webdriver.PhantomJS(service_log_path="/dev/null")
    # it save service log file in same directory
    # if you want to have log file stored else where
    # initialize the webdriver.PhantomJS() as
    # driver = webdriver.PhantomJS(service_log_path='/var/log/phantomjs/ghostdriver.log')
    driver.set_script_timeout(30)
    if width and height:
        driver.set_window_size(width, height)
    driver.get(url)
    driver.save_screenshot(screen_path)


def do_crop(params):
    print "Croping captured image.."
    command = [
        'convert',
        params['screen_path'],
        '-crop', '%sx%s+0+0' % (params['width'], params['height']),
        params['crop_path']
    ]
    execute_command(' '.join(command))


def do_thumbnail(params):
    print "Generating thumbnail from croped captured image.."
    command = [
        'convert',
        params['crop_path'],
        '-filter', 'Lanczos',
        '-thumbnail', '%sx%s' % (params['width'], params['height']),
        params['thumbnail_path']
    ]
    execute_command(' '.join(command))


def get_screen_shot(**kwargs):
    url = kwargs['url']
    width = int(kwargs.get('width', DEFAULTS["width"])) # screen width to capture
    height = int(kwargs.get('height', DEFAULTS["height"])) # screen height to capture
    filename = kwargs.get('filename', 'screen.png') # file name e.g. screen.png
    path = kwargs.get('path', DEFAULTS["path"]) # directory path to store screen

    crop = kwargs.get('crop', False) # crop the captured screen
    crop_width = int(kwargs.get('crop_width', width)) # the width of crop screen
    crop_height = int(kwargs.get('crop_height', height)) # the height of crop screen
    crop_replace = kwargs.get('crop_replace', False) # does crop image replace original screen capture?

    thumbnail = kwargs.get('thumbnail', False) # generate thumbnail from screen, requires crop=True
    thumbnail_width = int(kwargs.get('thumbnail_width', width)) # the width of thumbnail
    thumbnail_height = int(kwargs.get('thumbnail_height', height)) # the height of thumbnail
    thumbnail_replace = kwargs.get('thumbnail_replace', False) # does thumbnail image replace crop image?

    if not os.path.isdir(path) and not os.path.exists(path):
        os.makedirs(path)

    screen_path = abspath(path, filename)
    #crop_path = thumbnail_path = screen_path

    if thumbnail and not crop:
        raise Exception, 'Thumnail generation requires crop image, set crop=True'

    do_screen_capturing(url, screen_path, width, height)

    if crop:
        if not crop_replace:
            crop_path = abspath(path, 'crop_'+filename)
        params = {
            'width': crop_width, 'height': crop_height,
            'crop_path': crop_path, 'screen_path': screen_path}
        do_crop(params)

        if thumbnail:
            if not thumbnail_replace:
                thumbnail_path = abspath(path, 'thumbnail_'+filename)
            params = {
                'width': thumbnail_width, 'height': thumbnail_height,
                'thumbnail_path': thumbnail_path, 'crop_path': crop_path}
            do_thumbnail(params)

    return screen_path#, crop_path, thumbnail_path
