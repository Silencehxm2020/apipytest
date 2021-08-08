from tools.do_exl import DOEXL
from tools.get_filepath import GetFilePath


class Beforedata:
    # filepath = GetFilePath.file_path('test_data', 'test_da.xlsx')
    # data = DOEXL(filepath, 'login').get_sheet_data()
    # # print(data[0]["请求方式"])
    # baseurl = ReadConfig.base_url
    @staticmethod
    def do_test_data(dir_a, filename, sheetname):
        filepath = GetFilePath.file_path(dir_a, filename)
        data = DOEXL(filepath, sheetname).get_sheet_data()
        return data
