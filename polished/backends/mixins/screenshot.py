import os
import subprocess

from selenium import webdriver



class ScreenshotMixin(object):

    SCREENSHOT_DEFAULTS = {
        "path": "polished/",
        "width": 1280,
        "height": 960,
    }
    SCREENSHOT_COUNT = 0

    def screenshot(self, url):
        print "Capturing screen.."

        filename = "%05d.polished.png" % self.SCREENSHOT_COUNT
        screenshot_path = os.path.abspath(os.path.join(self.SCREENSHOT_DEFAULTS["path"], filename))

        self._do_screenshot(
            url,
            screenshot_path,
            self.SCREENSHOT_DEFAULTS["width"],
            self.SCREENSHOT_DEFAULTS["height"],
        )

        self.SCREENSHOT_COUNT = self.SCREENSHOT_COUNT + 1

    def _do_screenshot(self, url, screen_path, width, height):
        driver = webdriver.PhantomJS(service_log_path="/dev/null")
        #driver = webdriver.Chrome()
        driver.set_script_timeout(30)
        if width and height:
            driver.set_window_size(width, height)
        driver.get(url)
        driver.save_screenshot(screen_path)
        driver.quit()

        # verify screenshot has data, if not just delete it
        if os.stat(screen_path).st_size == 0:
            os.remove(screen_path)
