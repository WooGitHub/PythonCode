# 导入库
import os
import time

# 指定读取的路径
base_dir = './'

# 文件列表
file_lists = []

# 指定想要统计的文件类型
file_type = ['java','py','php','html','js','go','c','cpp','css','vue']

f = open('totalcount.txt', 'a', encoding='utf-8')

# 遍历文件, 递归遍历文件夹中的所有
def getDir_or_File(base_dir):
    # 定义一个全局变量
    global file_lists
    # 定义文件数
    total_files = 0
    # 遍历当前目录下所有的目录名
    for parent, dirnames, filenames in os.walk(base_dir):
        for filename in filenames:
            file = filename.split('.')[-1]
            if file in file_type:
                total_files += 1
                file_lists.append(os.path.join(parent, filename))
    return total_files

# 统计一个文件的行数
def countLines(file_name):
    count = 0
    for file_line in open(file_name, 'r', encoding='utf-8').readlines():
        if file_line != '' and file_line != '\n':  # 过滤掉空行
            count += 1
    f.write(file_name + ' ---- ' + str(count) + '\n')
    return count

if __name__ == '__main__' :
    startTime = time.perf_counter()
    getDir_or_File(base_dir)
    totallines = 0
    for filelist in file_lists:
    	# 计算总代码行数
        totallines = totallines + countLines(filelist)
    f.write('--------------------------------------------\n')
    demo = getDir_or_File(base_dir)
    f.write('total_files : ' + str(getDir_or_File(base_dir)) + '\n')
    # 打印代码行数
    f.write('total lines : ' + str(totallines) + '\n')
    # 打印程序执行时间
    f.write('Success! Cost Time: %0.2f seconds' % (time.perf_counter() - startTime))


