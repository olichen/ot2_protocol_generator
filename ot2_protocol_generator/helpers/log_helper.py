import logging

class LogHandler(logging.Handler):
    def __init__(self, text):
        logging.Handler.__init__(self)

        # Reference to the text that the handler will edit
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        self.text[0] += msg
        self.text[0] += '\n'
