import os

# 接口统计工具，可以统计接口或者其他的内容

def scan_files(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            # 判断那些是接口类
            if filename.startswith('I') and filename.endswith('Service.java'):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r', encoding='UTF-8') as f:
                    for line in f.readlines():
                        # 接口特征
                        if 'xxxx' in line:
                            method_index = line.find('inter = ') + len('inter = ')
                            methods = line[method_index:]
                            method = methods[: methods.find(',')]
                            print(method.strip('"'))

if __name__ == '__main__':
    path = "需要扫描的文件路径"
    scan_files(path)







