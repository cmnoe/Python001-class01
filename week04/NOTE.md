# 学习笔记

## 数据清洗与预处理

### panda

#### 基本数据类型

- Series

- DataFrame

#### 数据导入

- 从excel导入：pd.read_excel()

- 从csv导入：pd.read_csv()

- 从txt导入：pd.read_table()

- 从mysql导入：pd.read_sql()

#### 数据调整

- 数据中的缺失值

    - df.hasnans 检查是否有缺失值

    - df.fillna() 填充缺失值

    - df.ffill(axis= 0 | 1) 用上一行或列填充

    - df.dropna() 删除缺失值 

- 选择列：df['column_name']

    - 使用列表选择多列 df[ ['A', 'C'] ] 

    - 使用iloc根据索引选择行列 df.iloc[:, [0, 2]] // 所有行， 1，3列

    - 行选择 df.loc[ [0, 2] ] // 1, 3行   df.loc[0:2] // 1到3行

    - 使用条件运算符比较 df[ ( df['A']<5 ) & ( df['C']<4 ) ] // A列小于5，C列小于4的行

- 替换 df.replace()

    - 多对一  df.replace([4,5,8], 1000)

    - 多对多  df.replace({4:400,5:500,8:800})

- 排序 df.sort_values() // by指定列，ascending（bool）指定升降序

- 删除 df.drop() axis = 0 // 删除行  axis = 1 // 删除列

- 索引重塑 df.stack().reset_index()

#### 基本操作

- 算数运算  df['A'] + df['C']

- 常数加减  df['A'] + / - 5

- 比较运算  df['A'] > df['C']

- 非空值计算  df.count()

- 非空值求和  df.sum()    df['A'].sum() // 列求和

- 更多  mean求均值 max求最大值 min求最小值 median求中位数 mode求众数 var求方差 std求标准差

#### 分组聚合

- df.groupby()  把数据分解为多组子数据

- df.aggregate()  重新聚合数据

- pd.pivot_table()  数据透视表

#### 多表拼接
```
group = ['x','y','z']
data1 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10)
    })

data2 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    })

data3 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10),
    "salary":np.random.randint(5,50,10),
    })
```
- pd.merge()

    - 一对一  pd.merge(data1, data2)

    - 多对一  pd.merge(data3, data2, on='group')

    - 多对多  pd.merge(data3, data2)

    - 连接键（没有公共列）  pd.merge(data3, data2, left_on= 'age', right_on='salary')

    - 连接方式

        - 内连接（默认）  how='inner'

        - 外连接         how='outer'

        - 左连接         how='left'

        - 右连接         how='right'

        - 纵向连接  pd.concat([data1, data2])

#### 输出和绘图

- 输出

    - df.to_excel()  // 导出为excel

    - df.to_csv()  // 导出为csv

    - df.to_pickle() //  导出为数据流，性能好

- 绘图

    - matplotlib.pyplot

#### 数据分析

- jieba   抽取关键词

- SnowNLP  情感倾向分析
