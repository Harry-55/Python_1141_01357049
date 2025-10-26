import csv

# 新增員工資料
new_data = [
    {"職位": "資訊處處長", "年資": 8, "薪水": 70560, "學歷": "博士", "性別": "男", "年齡": 37},
    {"職位": "保全", "年資": 4, "薪水": 34000, "學歷": "碩士", "性別": "男", "年齡": 53},
    {"職位": "工程師", "年資": 13, "薪水": 153000, "學歷": "碩士", "性別": "男", "年齡": 38}
]

old_filename = "company_salaries.csv"
new_filename = "company_salaries_updated.csv"

# 1. 讀取原始 CSV
with open(old_filename, newline='', encoding='utf-8') as f:
    reader = list(csv.DictReader(f))

# 2. 將新資料加入
reader.extend(new_data)

# 3. 寫入新的 CSV
with open(new_filename, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ["職位", "年資", "薪水", "學歷", "性別", "年齡"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(reader)

# 4. 從新 CSV 統計資料
edu_count = {}
gender_count = {}
total = 0
with open(new_filename, newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        total += 1
        edu_count[row['學歷']] = edu_count.get(row['學歷'], 0) + 1
        gender_count[row['性別']] = gender_count.get(row['性別'], 0) + 1

most_edu = max(edu_count, key=edu_count.get)
most_gender = max(gender_count, key=gender_count.get)

# 5. 印出統計結果
print("公司總人數:", total)
print("最多人的學歷:", most_edu)
print("最多人的性別:", most_gender)
