import os
import shutil

# 文件夹整理工具，根据规则将文件夹整理到一起。
# 本例子使用了后缀名整理，也可以写其他规则。

if __name__ == '__main__':

    # 指定目录
    path = "E:\\文档"

    # 获取指定目录下的所有文件
    files = os.listdir(path)

    # 创建文件夹列表
    dirs = set()

    # 遍历所有文件
    for file in files:
        # 排除文件夹，只处理文件
        if os.path.isfile(os.path.join(path, file)):
            # 获取文件后缀名
            ext = os.path.splitext(file)[1]
            # 排除没有后缀名的文件
            if ext:
                # 创建对应后缀名的文件夹
                dir_name = ext[1:].lower()
                if dir_name not in dirs:
                    os.mkdir(os.path.join(path, dir_name))
                    dirs.add(dir_name)
                # 移动文件到对应文件夹中
                shutil.move(os.path.join(path, file), os.path.join(path, dir_name, file))