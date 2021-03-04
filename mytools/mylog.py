import logging


class Mylog:
    def __init__(self):
        # logging.basicConfig函数对日志的输出格式及方式做相关配置
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    def info(self, thstr):
        # 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
        logging.info(thstr)

    def warning(self, thstr):
        logging.warning(thstr)

    def error(self, thstr):
        logging.error(thstr)
