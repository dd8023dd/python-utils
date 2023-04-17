import os
import openpyxl

# 定义输入文件夹路径和输出文件路径
input_folder = 'C:\\Users\\LD-WX02\\Desktop\\yihu\\'
output_file = 'C:\\Users\\LD-WX02\\Desktop\\yihu\\ot.sql'

# 遍历文件夹下所有的Excel文件
for file_name in os.listdir(input_folder):
    if file_name.endswith('.xlsx'):
        print(f'Reading {file_name}...')
        file_path = os.path.join(input_folder, file_name)
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        # 读取列名并过滤空格或空值
        columns = []
        for cell in sheet[1]:
            if cell.value is None or cell.value.strip() == '':
                # 如果列名为空则使用缺省列名
                columns.append(f'column_{cell.column}')
            else:
                columns.append(cell.value)

        # 按照列名和值构造INSERT语句
        # 按照列名和值构造INSERT语句
        for row in sheet.iter_rows(min_row=2):
            values = []
            for cell in row:
                if cell.value is None:
                    # 如果值为空则使用缺省值
                    values.append('NULL')
                elif isinstance(cell.value, str):
                    values.append(f"'{cell.value}'")
                else:
                    values.append(str(cell.value))
            insert_statement = f"INSERT INTO my_table ({', '.join(columns)}) VALUES ({', '.join(values)});"
            # 将结果写入输出文件
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(insert_statement + '\n')

print('Done.')
