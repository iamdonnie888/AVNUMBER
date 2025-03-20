
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            positions.append(i)

    return positions

# 示例
text = "AV制作アシスタントに密着 パワハラ上司やセクハラ男優の無茶振りにも健気に働く女性AD 吉高寧々"
pattern = "吉高寧々"

print(naive_search(text, pattern))  # 输出: [10]

#text = "Hello, world! This is a test."
target = "吉高寧々"
if target in text:
    print(f"'{target}' 存在于文本中")
else:
    print(f"'{target}' 不存在于文本中")

#text = "Hello, world! This is a test."
#target = "world"
index = text.find(target)
if index != -1:
    print(f"'{target}' 首次出现在索引 {index} 处")
else:
    print(f"'{target}' 不存在于文本中")

import re

#text = "Hello, world! This is a test."
#target = "world"
match = re.search(target, text)
if match:
    print(f"'{target}' 存在于文本中，首次出现在索引 {match.start()} 处")
else:
    print(f"'{target}' 不存在于文本中")
