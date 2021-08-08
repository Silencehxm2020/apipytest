import os

from tools.get_filepath import GetFilePath

log_file_path = GetFilePath.file_path("log", "log.text")
logging_file_path = GetFilePath.file_path("test_case", "test_loging.py")
report_file_path=GetFilePath.file_path("html_report", "report.html")
print (os.path.split(report_file_path)[0])