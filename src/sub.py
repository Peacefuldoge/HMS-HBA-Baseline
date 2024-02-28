import pandas as pd
import matplotlib.pyplot as plt

data_1 = pd.read_csv('HMS-HBA-Baseline/data/submission_35.csv') #0.35
data_2 = pd.read_csv('HMS-HBA-Baseline/data/submission_40.csv')

row_data_1 = data_1.loc[0]
row_data_2 = data_2.loc[0]

data_dict_1 = row_data_1.to_dict()
data_dict_2 = row_data_2.to_dict()

excluded_label = 'eeg_id'

values_1 = [value for label, value in data_dict_1.items() if label != excluded_label]

print(values_1)

values_2 = [value for label, value in data_dict_2.items() if label != excluded_label]

print(values_2)

plt.hist(values_1, bins=10, edgecolor='black', color='blue', alpha=0.5, label='Data 1')  # alpha 参数设置透明度
plt.hist(values_2, bins=10, edgecolor='black', color='red', alpha=0.5, label='Data 2')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.legend()  # 显示图例
plt.grid(True)  # 添加网格线
plt.show()