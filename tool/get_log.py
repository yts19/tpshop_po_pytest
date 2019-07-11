import logging.handlers
class GetLog():
    # 单例思想
    logger=None
    @classmethod
    def get_loggin(cls):
        if cls.logger is None:

        # 获取日志器入口
            cls.logger=logging.getLogger()
        # 设置级别
            cls.logger.setLevel(logging.INFO)
        # 获取处理器
            hd=logging.handlers.TimedRotatingFileHandler(filename="./log/tp_log.log",
                                                         when='h',
                                                         interval=1,
                                                         backupCount=2,
                                                         encoding="utf-8")
            hd.setLevel(logging.INFO)

        # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
        # 将格式器添加到处理器
            hd.setFormatter(fm)
        # 将处理器添加给日志器
            cls.logger.addHandler(hd)
        return cls.logger
