class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)


"""
Судя по комментариям - тут что то должно не работать :)

Если делать все пошагово то получается следующая архитектура:

home_dir:

                 -- __init__.py

                 -- conftest.py

                 -- pages:

                                 -- base_page

                                 -- main_page 
"""