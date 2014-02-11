import logging


class LOG(object):

    def __init__(self, level, only='off'):
        self.only = only
        self.level = level
        self.LOG_FILENAME = 'file.log'

    def message(self, message):
        if self.level == 'debug' and self.only == 'debug':
            logging.basicConfig(filename=self.LOG_FILENAME, level=logging.DEBUG, format='[%(asctime)s] %(levelname)-4s:  %(message)s', datefmt='%a, %d/%b/%Y %I:%M:%S %p')
            logging.debug(message)

        elif self.level == 'info' and self.only == 'info':
            logging.basicConfig(filename=self.LOG_FILENAME, level=logging.INFO, format='[%(asctime)s] %(levelname)-4s:  %(message)s', datefmt='%a, %d/%b/%Y %I:%M:%S %p')
            logging.info(message)
