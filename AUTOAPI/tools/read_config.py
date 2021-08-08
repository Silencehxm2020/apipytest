import configparser

from tools.get_filepath import GetFilePath


class ReadConfig:
    cf = configparser.ConfigParser()
    cf.read(GetFilePath.file_path("common", "base.config"), encoding="utf-8")
    base_url = cf.get("BASEURL", "base_url")
