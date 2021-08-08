import os

from unittestreport import TestRunner
import unittest

from common.project_file_path import logging_file_path, report_file_path
from tools.read_config import ReadConfig


class RunTestcase:
    baseurl = ReadConfig.base_url

    @staticmethod
    def run():
        my_suite = unittest.defaultTestLoader.discover(os.path.split(logging_file_path)[0], "test_loging.py")
        runner = TestRunner(my_suite, report_dir=os.path.split(report_file_path)[0], templates=1)
        runner.run()


RunTestcase.run()
