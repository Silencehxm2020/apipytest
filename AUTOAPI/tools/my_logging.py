import logging

from common.project_file_path import log_file_path


class LOG:
    """
    # 新建一个用例收集器
    #定义log级别
    # 定义日志格式
    # 定义一个文件输出渠道
    """

    def my_logging(self, level, msg):
        # 新建一个用例收集器
        project_log = logging.getLogger("xinxiaofu")
        # 设置log级别
        project_log.setLevel("DEBUG")
        # 设置log输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
        # 定义一个文本输出渠道
        log_out = logging.FileHandler(log_file_path, encoding="utf-8")
        # 将格式加载到输出文本中
        log_out.setFormatter(formatter)
        # 设置log输出级别
        log_out.setLevel("DEBUG")
        # 将收集器和输出渠道对接
        project_log.addHandler(log_out)
        # 定义不同级别的日志收集
        if level == "DEBUG":
            project_log.debug(msg)
        elif level == "INFO":
            project_log.info(msg)
        elif level == "ERROR":
            project_log.error(msg)
        elif level == "WARNING":
            project_log.warning(msg)
        elif level == "CRITICAL":
            project_log.critical(msg)
        # 关闭日志收集器
        project_log.removeHandler(log_out)

    @staticmethod
    def debug(msg):
        L = LOG()
        L.my_logging("DEBUG", msg)

    @staticmethod
    def info(msg):
        L = LOG()
        L.my_logging("INFO", msg)

    @staticmethod
    def error(msg):
        L = LOG()
        L.my_logging("ERROR", msg)

    @staticmethod
    def warning(msg):
        L = LOG()
        L.my_logging("WARNING", msg)

    @staticmethod
    def critical(msg):
        L = LOG()
        L.my_logging("CRITICAL", msg)


if __name__ == '__main__':
    LOG.error("去死吧")
