# -*- coding: utf-8 -*-
# @Time    : 06/08/2023
# @Author  : nzooherd
# @File    : regulate_handler.py 
# @Software: PyCharm
# -*- coding: utf-8 -*-
import os.path

from watchdog.events import FileSystemEventHandler

from config import Config
from crawler.spider import Spider


class RegulateHandler(FileSystemEventHandler):

    """ Regulate Videos Entrance

    Args:
        config (Config):
        spider (Spider):

    """

    def __init__(self, config: Config, spider: Spider):
        self.spider = spider
        pass


    def on_created(self, event):
        """

        """
        pass


    def __process_directory(self, directory: str):
        """
        :param str directory:
        """
        basename = os.path.basename(directory)
        if number := self.spider.match(basename):
            self.spider.scrape(number)
        else:
            for basename in os.listdir(directory):
                path = os.path.join(directory, basename)
                if os.path.isfile(path):
                    self.__process_file(path)
                else:
                    self.__process_directory(directory)

    def __process_file(self, file: str):
        """

        """
        if number := self.spider.match(file):
            self.spider.scrape(number)
