import inspect
import logging


class LogGenerator:

    @staticmethod
    def getLog(Name="All_logs"):
        loggerName = inspect.stack()[1][3]
        # The "inspect.stack()[1][3]" will copy the class Name in Details From Test File
        logger = logging.getLogger(loggerName)
        # getLogger() method takes the Tests Case Name as input
        File = logging.FileHandler(f"C:\\Users\\Tejas\\Class Project\\Logs\\{Name}.log")
        # fileHandler() method takes location or path of log file.
        Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        # formatter() method takes care of the file log file formatting.
        File.setFormatter(Formatter)
        # setFormatter() method update All format in every fraction of time in to the file.
        logger.addHandler(File)
        # addHandler() method takes fileHandler object as parameter
        logger.setLevel(logging.INFO)
        # setting the logger level.
        return logger