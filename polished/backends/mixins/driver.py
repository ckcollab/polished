import os

from selenium import webdriver

from base import Base



class DriverMixin(Base):

    SCREENSHOT_DEFAULTS = {
        "path": "polished_output/",
        "width": 1280,
        "height": 960,
    }
    DRIVER = None
    PAGE_SOURCE = None
    OLD_SCREENSHOT_PAGE_SOURCE = None

    def __init__(self, *args, **kwargs):
        self.DRIVER = webdriver.PhantomJS(service_log_path="/dev/null")
        self.DRIVER.set_script_timeout(30)
        self.DRIVER.set_window_size(self.SCREENSHOT_DEFAULTS["width"], self.SCREENSHOT_DEFAULTS["height"])
        super(DriverMixin, self).__init__(*args, **kwargs)

    def screenshot(self, only_new_pages=False):
        if only_new_pages:
            if self.OLD_SCREENSHOT_PAGE_SOURCE == self.PAGE_SOURCE:
                return

        print "Capturing screen.."

        filename = "%05d.%s.polished.png" % (self.CURRENT_COMMIT_INDEX, self.CURRENT_SHA)
        screenshot_path = os.path.abspath(os.path.join(self.SCREENSHOT_DEFAULTS["path"], filename))

        self.DRIVER.save_screenshot(screenshot_path)

        self.OLD_SCREENSHOT_PAGE_SOURCE = self.PAGE_SOURCE

        # verify screenshot has data, if not delete it
        if os.stat(screenshot_path).st_size == 0:
            os.remove(screenshot_path)

    def go_to_url(self, url):
        self.DRIVER.get(url)
        self.PAGE_SOURCE = self.DRIVER.page_source

    def dispose(self, *args, **kwargs):
        self.DRIVER.quit()
        super(DriverMixin, self).dispose(*args, **kwargs)
