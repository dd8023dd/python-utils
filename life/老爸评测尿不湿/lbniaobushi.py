import pandas as pd

# 本项目可以通过权重对尿不湿进行排名，从而选择合适的尿不湿。
# 现在有的指标里面进行筛选，数据源在excel中，可以根据自己想买尿不湿集合对excel内容进行调整
# 本项目仅供娱乐，不做任何推荐使用。
# 权重计算的方式可以运用到很多方面。可以自行研究和修改。


# 读取Excel文件
df = pd.read_excel(r'G:\尿不湿-老爸评测整理1.xlsx', sheet_name=0)

# 计算每个指标的分数
def calculate_score(df, weights):
    # 把每个指标的值转为分数
    df['单片价格'] = (df['单片价格'].max() - df['单片价格']) / (df['单片价格'].max() - df['单片价格'].min()) * weights[0]
    df['吸湿渗透量'] = (df['吸湿渗透量'] - df['吸湿渗透量'].min()) / (df['吸湿渗透量'].max() - df['吸湿渗透量'].min()) * weights[1]
    df['持续加液至底部有滴漏的加入量'] = (df['持续加液至底部有滴漏的加入量'] - df['持续加液至底部有滴漏的加入量'].min()) / (df['持续加液至底部有滴漏的加入量'].max() - df['持续加液至底部有滴漏的加入量'].min()) * weights[2]
    df['透气性'] = (df['透气性'] - df['透气性'].min()) / (df['透气性'].max() - df['透气性'].min()) * weights[3]
    df['丙烯酸残留单体'] = (df['丙烯酸残留单体'].max() - df['丙烯酸残留单体']) / (df['丙烯酸残留单体'].max() - df['丙烯酸残留单体'].min()) * weights[4]
    df['无异味'] = df['无异味'].apply(lambda x: weights[5] if x == 0 else 0)
    # 计算总分
    df['score'] = df['单片价格'] + df['吸湿渗透量'] + df['持续加液至底部有滴漏的加入量'] + df['透气性'] + df['丙烯酸残留单体'] + df['无异味']
    # 按总分倒序排序
    df = df.sort_values(by='score', ascending=False)
    # 输出分数、编号、品牌名称
    result = df[['score', '编号', '品牌名称']]
    return result

# 根据指标权重筛选品牌名称
def filter_brand(df, weights):
    # 把每个指标的值转为分数
    df['单片价格'] = (df['单片价格'].max() - df['单片价格']) / (df['单片价格'].max() - df['单片价格'].min()) * weights[0]
    df['吸湿渗透量'] = (df['吸湿渗透量'] - df['吸湿渗透量'].min()) / (df['吸湿渗透量'].max() - df['吸湿渗透量'].min()) * weights[1]
    df['持续加液至底部有滴漏的加入量'] = (df['持续加液至底部有滴漏的加入量'] - df['持续加液至底部有滴漏的加入量'].min()) / (df['持续加液至底部有滴漏的加入量'].max() - df['持续加液至底部有滴漏的加入量'].min()) * weights[2]
    df['透气性'] = (df['透气性'] - df['透气性'].min()) / (df['透气性'].max() - df['透气性'].min()) * weights[3]
    df['丙烯酸残留单体'] = (df['丙烯酸残留单体'].max() - df['丙烯酸残留单体']) / (df['丙烯酸残留单体'].max() - df['丙烯酸残留单体'].min()) * weights[4]
    df['无异味'] = df['无异味'].apply(lambda x: weights[5] if x == 0 else 0)
    # 计算总分
    df['score'] = df['单片价格'] + df['吸湿渗透量'] + df['持续加液至底部有滴漏的加入量'] + df['透气性'] + df['丙烯酸残留单体'] + df['无异味']
    # 按总分倒序排序
    df = df.sort_values(by='score', ascending=False)
    # 输出品牌名称
    result = df['品牌名称']
    return result

# 测试calculate_score函数
weights = [3, 8, 8, 10, 8, 8]
result = calculate_score(df, weights)
print(result)
# 输出结果到Excel文件
# result.to_excel(r'G:\结果2.xlsx', index=False)

# # 测试filter_brand函数
# weights = [10, 8, 6, 4, 2, 1]
# result = filter_brand(df, weights)
# print(result)