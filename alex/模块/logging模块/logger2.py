import  logging


def logmod(ex):
    #step1
    # 定义logger日志对象，通常是模块名字;
    # 定义全局日志等级
    logger = logging.getLogger("testst")
    logger.setLevel(logging.DEBUG)

    #step 2
    #定义日志输出到什么地方
    # 屏幕
    # 文件
    #到屏幕
    input_mirror = logging.StreamHandler() # 日志打印到屏幕
    input_mirror.setLevel(logging.DEBUG) #只想在屏幕上打印出debug日志

    #到文件
    input_file = logging.FileHandler("access-loggger")
    input_file.setLevel(logging.DEBUG)


    #step3
    #formatter设置输出格式
    # 3.1 定义文件的输出格式
    # 3.2 定义屏幕的输出格式
    formatter_type = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    input_mirror.setFormatter(formatter_type)
    input_file.setFormatter(formatter_type)

    #step 4  日志打印到指定的Handler里面


    logger.addHandler(input_mirror)
    logger.addHandler(input_file)



    logger.debug(ex)



