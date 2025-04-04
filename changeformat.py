import csv
import json

def convert_csv_to_json(csv_path, json_path):
    # 创建结果列表
    result = []
    
    # 读取CSV文件
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        # 跳过标题行
        next(csvfile)
        reader = csv.reader(csvfile)
        
        # 处理每一行数据
        for row in reader:
            # CSV中每行有两列：text和summary
            if len(row) == 2:
                entry = {
                    "input": row[0].strip('"'),  # 移除可能存在的引号
                    "refs": row[1].strip('"')    # 移除可能存在的引号
                }
                result.append(entry)
    
    # 写入JSON文件
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(result, jsonfile, indent=4, ensure_ascii=False)

# 使用示例
csv_path = '/home/yshi0940/SC/seq2seq-sc/data/allnli/processed/allnli_train_full.csv'
json_path = '/home/yshi0940/SC/seq2seq-sc/data/allnli/allnli_train_full.json'
convert_csv_to_json(csv_path, json_path)