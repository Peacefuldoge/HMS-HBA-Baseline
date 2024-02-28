import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_1 = pd.read_csv('HMS-HBA-Baseline/data/submission_35.csv') #0.35
data_2 = pd.read_csv('HMS-HBA-Baseline/data/submission_40.csv')

row_data_1 = data_1.loc[0]
row_data_2 = data_2.loc[0]

data_dict_1 = row_data_1.to_dict()
data_dict_2 = row_data_2.to_dict()

excluded_label = 'eeg_id'

labels = [label for label in data_dict_1.keys() if label != excluded_label]

values_1 = [value for label, value in data_dict_1.items() if label != excluded_label]

print(values_1)

values_2 = [value for label, value in data_dict_2.items() if label != excluded_label]

print(values_2)

# 设置每个柱形的宽度
bar_width = 0.35

# 创建 x 轴位置
x = np.arange(len(labels))

# 绘制直方图
plt.bar(x - bar_width/2, values_1, width=bar_width, color='blue', label='0.35')
plt.bar(x + bar_width/2, values_2, width=bar_width, color='red', label='0.4')

# 设置 x 轴标签和标题
plt.xlabel('Label')
plt.ylabel('Value')
plt.title('Histogram by Label')
plt.xticks(x + bar_width / 2, labels)
plt.legend()

plt.show()