#将进度保持到 progerss.tmp
progerss_file = 'progerss.tmp'
def save_progress(progerss):
    fo = open(progerss_file, "w")
    fo.write(str(progerss))
    fo.close()

def get_progress():
    # 打开一个文件
    try:
        fo = open(progerss_file, "r+")
        str = fo.read()
        # 关闭打开的文件
        fo.close()
        return int(str)
    except BaseException as e:
        return 0