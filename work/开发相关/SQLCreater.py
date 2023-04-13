import uuid

# 定义常量
COLUMN_NAMES = ['create_date', 'create_time', 'update_date', 'update_time',
                'update_times', 'user_key', 'remaining_count', 'expire_date',
                'use_times', 'valid_status', 'bind_ip', 'bind_phone']
TABLE_NAME = '`db_chat`.`tb_user_key`'
VALUES_TEMPLATE = "(%s, 0, %s, 0, 0, '%s', 100, %s, 0, '1', '0', '0');"

# 生成 SQL 语句
n = 100  # 需要生成的 SQL 语句数量
for i in range(n):
    # 生成 uuid
    user_key = str(uuid.uuid4())

    # 生成插入语句的 values 部分
    create_date = 20230411
    update_date = 20230411
    expire_date = 20230601
    values = VALUES_TEMPLATE % (create_date, update_date, user_key, expire_date)

    # 生成完整的 SQL 语句
    columns = ','.join(['`%s`' % c for c in COLUMN_NAMES])
    sql = 'INSERT INTO %s (%s) VALUES %s' % (TABLE_NAME, columns, values)

    print(sql)

