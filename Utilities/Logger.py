import inspect
import logging


class LogGenerator:

    @staticmethod
    def getLog():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        File = logging.FileHandler("C:\\Users\\Tejas\\Class Project\\Logs\\All_logs.log")
        Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        File.setFormatter(Formatter)
        logger.addHandler(File)
        logger.setLevel(logging.INFO)
        return logger

