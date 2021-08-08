import os


class GetFilePath:
    @staticmethod
    def file_path(tir_name, file_name):
        now_path = os.path.realpath(__file__)
        tir_path = os.path.split(now_path)[0]
        project_path = os.path.split(tir_path)[0]
        find_file_path = os.path.join(project_path, tir_name, file_name)
        return find_file_path



