import re

def are_texts_not_equal(text1, text2):
    """
    判断两个文本是否一样
    :param text1: 第一个文本
    :param text2: 第二个文本
    :return: 如果文本相同返回 True，否则返回 False
    """
    if text1 != text2:
        return True
    #else:
    return False

# 示例用法
text1 = "Hello, world!"
text2 = "Hello, world!"
text3 = "hello, world!"

print(are_texts_not_equal(text1, text2))  # 输出: True
print(are_texts_not_equal(text1, text3))  # 输出: False


def find_english_words_in_mixed_text(text):
    """
    在中日英文混合文本中查找所有英文单词
    :param text: 输入的混合文本
    :return: 匹配的英文单词列表及其位置
    """
    # 正则表达式匹配英文单词（包括连字符和撇号）
    word_pattern = re.compile(r'\b[A-Za-z\0-9\-\']+\b')
    words = word_pattern.finditer(text)

    matches = []
    for match in words:
        word = match.group()
        #print(type(word))
        matches.append((word, match.start(), match.end()))

    print(matches)
    return matches

# 示例用法
#text = "精品无码 (FC2-PPV-2711719)这可能是近来步兵片最好的金髮萝莉，而她竟然是地下偶像！"
#text = "SONE-607 [中文字幕] スタイルも愛嬌も抜群な美少女のニコニコ笑顔に精液ぶっかける背徳大量顔射オナサポ 乃坂ひより"
#text = "IPZZ-507 [中文字幕] もうセックスなしでは生きていけない… 絶頂イキ 197回 マ×コ痙攣 2255回 鬼ピストン 3686回 快感潮 測定不能 絶頂覚醒 藤咲舞"
#text = "DGCEMD-515 ★配信限定！特典映像付★凄テクで男を飼い慣らす女はこの世に存在する 愛瀬ゆうり"
#text = "[4KUHD] MEYD-927 「やめてっ孕んじゃう…！」夫が海外出張中の20日間、夫の部下に毎日中出しされています。 天海つばさ"
text = "SONE-560 S1 PRECIOUS GIRLS 2024 オールスター24名大集合ハーレムアイランドSpecial"

matches = find_english_words_in_mixed_text(text)

for match in matches:
    if match[2] - match[1] >= 4 and are_texts_not_equal(match[0], '4KUHD'):
        #print("x 大于 5")  # 这行代码会被执行
        print(f"Found '{match[0]}' at position {match[1]} to {match[2]}")