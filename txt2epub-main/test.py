#!/usr/bin/python3
import regex as re
import re

content = "目录/wangcl"
xlsPath = r'C:\Users\Administrator'


#去除特殊符号
def remove_special_characters(text):
    tokens = tokenize_text(text) #tokens为分词后的文本
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation))) #正则匹配特殊符号
    print(pattern)
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

content = remove_special_characters(content)


