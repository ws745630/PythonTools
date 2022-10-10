#!/usr/bin/python
print("注：请将txt和jpeg文件重命名成书名+后缀\n并将其放入脚本所在文件夹\n请查看txt的编码\n\n请务必确保文件夹内有txt和jpeg后缀的同名文件\n\n")
import os
import re
import glob
import chardet
import time

 
print('正在录入书籍数据')
path = glob.glob('*.txt')
filename = str(path)[2:-6]
title_string = "大学刑法课" #re.search(r'(?<=《)[^》]+',filename)
author_string = "无" #re.search(r'(?<=作者：).*',filename)[0]
bookname = title_string
txtname = bookname + ".txt"
jpgname = bookname + ".jpeg"
epubname = bookname + ".epub"
kepubname = bookname + ".kepub.epub"
title_string = bookname

print('书名: '+bookname+'\n'+'作者: '+author_string)

os.system('mv *.txt "%s"' % (txtname))

start = time.perf_counter()

# 开始图片处理
Your_Dir='./'
Files=os.listdir(Your_Dir)
for k in range(len(Files)):
    # 提取文件夹内所有文件的后缀
    Files[k] = os.path.splitext(Files[k])[1]

# 你想要找的文件的后缀
Str='.jpg'
if Str in Files:
    os.system("rename .jpg .jpeg *.jpg")
    print('图片转换已完成')
else:
    print('图片转换已完成') 

os.system("find ./ -name '*.jpeg' -exec convert -resize 600x800 {} {} \;")
os.system('mv *.jpeg "%s"' % (jpgname))
#图片转换结束

print("开始文件转码.......")

def detectCode(path):
    with open(path, 'rb') as file:
        data = file.read(20000)
        dicts = chardet.detect(data)
    return dicts["encoding"]

ecode = detectCode(path[0])
print('文件编码：' + ecode)
if ecode != 'utf-8' and ecode != 'UTF-8-SIG':
        f = open(txtname, 'r', encoding = "gb18030")
        content = f.read()
        f.close()
        f = open(txtname, 'w', encoding="utf-8")
        f.write(content)
        f.close()
else:
        print('文件转码完成')
 
if __name__ == '__main__':
    
    print('开始分章以及处理多余内容')
    f = open(path[0],'r', encoding="utf-8")
    content = f.read()
    f.close

    lines = content.rsplit("\n") 
    new_content = []
    new_content.append("% "+ title_string)
    new_content.append("% "+ author_string)

    for line in lines:
        
        if line == "更多精校小说尽在知轩藏书下载：http://www.zxcs.me/" or line == "==========================================================" or line == title_string or line == title_string + " 作者：" + author_string or line == "作者：" + author_string or line == "作者: " + author_string:
            continue
        if line == "简介:" or line == "内容简介：" or line == "内容简介":
                new_content.append("### " + line + "\n")
                continue
        if re.match(r'^\s*(楔子|序章|序言|序|引子).*',line):
                new_content.append("## " + line + "\n")
                continue
        if re.match(r'^\s*[第][0123456789ⅠI一二三四五六七八九十零序〇百千两]*[卷].*',line):
            new_content.append("# " + line + "\n")
            continue

        if re.match(r'^\s*[第][0123456789ⅠI一二三四五六七八九十零序〇百千两]*[章].*',line):
                new_content.append("## " + line + "\n")
                continue

        new_content.append(line + "\n")
    new_content = "\n".join(new_content)

    f = open(txtname,'w',encoding="utf=8")
    f.write(new_content)
    f.close


    print("开始转换EPUB文件........")
    #os.system('pandoc "%s" -o "%s" -t epub3 --css=epub.css --epub-chapter-level=2 --epub-cover-image="%s"' % (txtname, epubname, jpgname))
    os.system('pandoc "%s" -o "%s" -t epub3 --css=epub.css --epub-chapter-level=2' % (txtname, epubname))
    end = time.perf_counter()
    print('Running time: %s Seconds' % (end - start))
    start_1 = time.perf_counter()
    #os.system('kindlegen -c1 -dont_append_source "%s" > a' % (epubname))
    os.system('kepubify "%s"' % (epubname))
    end_1 = time.perf_counter()
    print('Running time: %s Seconds' % (end_1 - start_1))
    print("删除残留文件......")
    os.system('rm "%s"' % (txtname))
    os.system('rm "%s"' % (jpgname))
    os.system('rm a')
    os.system('mv *.kepub.epub "%s"' % (kepubname))
    os.system('mv "%s" ~/Desktop' % (epubname))
    os.system('mv "%s" ~/Desktop' % (kepubname))
    print("完成，收工，撒花！！🎉🎉")
