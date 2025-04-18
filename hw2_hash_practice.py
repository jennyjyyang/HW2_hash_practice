# -*- coding: utf-8 -*-
"""HW2_hash_practice

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10IGxd-OmW_FoCKwwIqjXATbJX7KBkqEW
"""

#匯入畫圖需要的套件
import matplotlib.pyplot as plt

#建立字典
word_count={}

#讀取檔案
file_path="hw2_data.txt"
with open(file_path,"r") as file:
  for line in file:
    word=line.strip()
    if word in word_count:
      word_count[word]+=1
    else:
      word_count[word]=1

#統計不重複的英文字總數
unique_words=len(word_count)
print(f"1.總共有 {unique_words} 個不重複的英文字。\n")

#每個英文字出現的次數
print("2.每一個英文字出現次數如下：")
for word,count in sorted(word_count.items(),key=lambda x:x[1],reverse=True):
  print(f"{word}:{count}")

#畫出直方圖（由多到少）
print("\n3.英文字出現次數直方圖如下:")
sorted_words = sorted(word_count.items(),key=lambda x:x[1],reverse=True)
words = [item[0] for item in sorted_words]
counts = [item[1] for item in sorted_words]

plt.figure(figsize=(12,6))
plt.bar(words,counts)
plt.xticks(rotation=90)
plt.xlabel("Words")
plt.ylabel("Counts")
plt.tight_layout()
plt.show()