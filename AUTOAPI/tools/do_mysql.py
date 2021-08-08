import pymysql

from tools.my_logging import LOG


class DoMysql:
    def do_mysql(self, sql_info, query, state="all"):
        """"
        进行数据库连接，并执行SQL语句
        """
        try:
            LOG.info("正在连接数据库")
            connect = pymysql.connect(**sql_info)
            cusor = connect.cursor()
            LOG.info("连接数据库成功")
            cusor.execute(query)
            if state == "all":
                res = cusor.fetchall()
            elif state == 1:
                res = cusor.fetchone()
            cusor.close()
            connect.close()
            return res
        except Exception as e:
            LOG.error("数据库连接失败或SQL语句执行错误{}".format(e))
