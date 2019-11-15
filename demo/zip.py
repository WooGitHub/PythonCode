from tkinter import *                        # 导入tkinter的所有组件
from tkinter.filedialog import askdirectory  # 导入目录操作库
import tkinter.messagebox      # 弹出消息框
import zipfile                 # 解压缩核心库
import os                      # os操作库
import tkinter.filedialog      # 导入操作文件的库

def selectPath():
    path_ = askdirectory()
    path.set(path_)

def selectFile():
    file_path = tkinter.filedialog.askopenfilename()
    file_path.replace("/","\\\\")
    filename.set(file_path)

def outputFlie():
    output_flie = askdirectory()
    outputfile.set(output_flie)

#压缩文件
# path：要压缩的文件的路径
def zip_file():
    zip_name = path.get() +'.zip'         # 获取绝对路径然后给压缩文件加上.zip结尾      
    z = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)  # 写入.zip
    for dirpath, dirnames, filenames in os.walk(path.get()):# 使用os遍历目录路径，目录名，文件名
        fpath = dirpath.replace(path.get(),'')              # 获取目录路径
        fpath = fpath and fpath + os.sep or ''              
        for filename in filenames:                          # 迭代文件名
            z.write(os.path.join(dirpath, filename),fpath+filename)  # 写入
    z.close()                                               # 关闭资源，以免占用内存
    zip_file_message()                                      # 调用zip_file_message弹出信息框

# filename:是zip文件的全路径
# outputfile：是要解压到的目的文件夹
def unzip_file():
    r = zipfile.is_zipfile(filename.get())          # 判断是否为压缩文件以.zip为判断依据
    if r:                                           # 如果是则执行if里面的语句，如果不是执行else里面的语句
        fz = zipfile.ZipFile(filename.get(), 'r')   # 读取压缩文件
        for file in fz.namelist():                  # 遍历文件
            fz.extract(file, outputfile.get())      # 输出文件
        unzip_file_message()                        # 调用unzip_file_message弹出信息框
    else:
        failed()                                    # 调用failed弹出信息框

# 弹出信息框
def zip_file_message():
    result = tkinter.messagebox.askokcancel(title='success',message="压缩成功")

# 弹出信息框
def unzip_file_message():
    result = tkinter.messagebox.askokcancel(title='success',message="解压成功")

# 弹出信息框
def failed():
    result = tkinter.messagebox.askokcancel(title='success',message="这不是一个压缩文件")

# 界面代码实现
def main():
    # label标签 grid括号中的row代表你的label是放在第几行，column是放在第几列
    Label(root,text = "压缩目录路径:").grid(row = 0, column = 0)

    # Entry是获取输入
    Entry(root, textvariable = path).grid(row = 0, column = 1)

    # 操作按钮
    Button(root, text = "目录选择", command = selectPath).grid(row = 0, column = 2)

    # Label标签
    Label(root,text = "解压目录路径:").grid(row = 1, column = 0)
   
    # Entry是获取输入
    Entry(root, textvariable = filename).grid(row = 1, column = 1)
    
    # 操作按钮
    Button(root, text = "文件选择", command = selectFile).grid(row = 1, column = 2)

    # Label标签
    Label(root,text = "解压到:").grid(row = 2, column = 0)
    
    # Entry是获取输入
    Entry(root, textvariable = outputfile).grid(row = 2, column = 1)
    
    # 操作按钮
    Button(root, text = "解压路径选择", command = outputFlie).grid(row = 2, column = 2)

    # 操作按钮
    Button(root,text="压缩文件",command=zip_file).grid(row=3,column=0)
    
    # 操作按钮
    Button(root,text="解压文件",command=unzip_file).grid(row=3,column=2)

    # 操作按钮
    Button(root,text="退出程序",command=root.quit).grid(row=4,column=1)

    #显示操作界面
    root.mainloop()

if __name__ == '__main__':
    root = Tk()              # 初始化
    path = StringVar()       # 显示路径名
    filename = StringVar()   # 显示文件路径名
    outputfile = StringVar() # 显示解压后的文件路径名
    main()                   # 调用main函数



