import logging, sys


class Log_Util:
    logger = None

    @staticmethod
    def create_logger():
        # create logger
        logger = logging.getLogger()

        # create handler
        logHandler = logging.StreamHandler(sys.stdout)
        logger.addHandler(logHandler)

        # set logger level
        logger.setLevel(logging.DEBUG)

        return logger
    
    @staticmethod
    def get_logger():
        if not Log_Util.logger:
            Log_Util.logger = Log_Util.create_logger()
        return Log_Util.logger