import configparser

data = configparser.RawConfigParser()

data.read("C:\\Users\\Tejas\\Class Project\\Configuration\\Config.ini")


class Read_Config:

    @staticmethod
    def getURL():
        UL = data.get("login data", "URL")
        return UL

    @staticmethod
    def getname():
        name = data.get("login data", "username")
        return name

    @staticmethod
    def getpass():
        password = data.get("login data", "password")
        return password

