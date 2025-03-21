
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            positions.append(i)

    return positions

# 示例
#text = "AV制作アシスタントに密着 パワハラ上司やセクハラ男優の無茶振りにも健気に働く女性AD 吉高寧々"
text = "SONE-541 夢乃真实药物服药 870 天后身体变得非常敏感，性欲增强，她弓起后背狂喜不已尽情享受sex 夢乃あいか"

#pattern = "吉高寧々"
pattern = "夢乃あいか"

print(naive_search(text, pattern))  # 输出: [10]

#text = "Hello, world! This is a test."
#target = "吉高寧々"
target = "夢乃あいか"

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

def contains_char(text, char):
    return char in text

# 示例
text = "hello world"
char = "o"
print(contains_char(text, char))  # 输出: True
