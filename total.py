import os
import pandas as pd

def count_anomalies_in_raw_csv(folder_path):
    results = []

    for file in os.listdir(folder_path):
        if file.endswith('.csv') and file.startswith('tube'):
            file_path = os.path.join(folder_path, file)
            try:
                df = pd.read_csv(file_path)

                # 按第17列和第18列是否非零标记异常（Python从0开始计数）
                anomaly_mask = (df.iloc[:, 16] != 0) | (df.iloc[:, 17] != 0)
                anomaly_count = anomaly_mask.sum()
                total = len(df)

                results.append({
                    'File': file,
                    '#Anomalies': int(anomaly_count),
                    'Total': total,
                    'Anomaly Ratio (%)': round(100 * anomaly_count / total, 4)
                })

            except Exception as e:
                print(f"❌ Error reading {file_path}: {e}")

    # 输出结果表格
    result_df = pd.DataFrame(results)
    print("\n📊 Raw Anomaly Stats Based on f17 or f18 != 0:\n")
    print(result_df)

    # 可选：保存统计结果
    save_path = os.path.join(folder_path, 'raw_anomaly_summary.csv')
    result_df.to_csv(save_path, index=False)
    print(f"\n✅ 统计结果已保存至：{save_path}")

# ✅ 运行
if __name__ == '__main__':
    count_anomalies_in_raw_csv(r"D:\个人文件\SCUPI\数据挖掘\HW2\Data")
