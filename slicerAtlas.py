# 分割图集

import os
from PIL import Image
import json

# 封装一个TextureUnpacker类
class SlicerAtlas(object):
    @classmethod
    def split_with_json(cls, f_json, save_dir=None):
        f_json = os.path.abspath(f_json)
        if save_dir is None:
            save_dir = f_json + '_split'
        else:
            save_dir = os.path.abspath(save_dir)
        # 读取json配置表
        f = open(f_json, 'r')
        txt = f.read()
        dt = json.loads(txt)
        f.close()
        # 大图集文件名
        big_texture_file_name = dt['file']
        # 小图序列
        frames =  dt['frames']
        # 打开大图
        filepath,tmpfilename = os.path.split(f_json)
        big_path = os.path.join(filepath,big_texture_file_name)
        big_img = Image.open(big_path)
        # 遍历生成小图
        for key,value in frames.items():
            # 解析配置
            #info = cls.parse_as_json(info)
            print(value)
            x = int(value['x'])
            y = int(value['y'])
            width = int(value['w'])
            height = int(value['h'])
            imginfo = {"xy":[x,y],"sz":[width,height],"box":(x,y,x+width,y+height)}
            filename = key.replace("_png", ".png")
            #filename = "%s.png"%(key)
            # 小图的保存路径
            little_image_save_path = os.path.join(save_dir, filename)
            # 生成小图
            cls.generate_little_image(big_img, imginfo, little_image_save_path)

    @classmethod
    def generate_little_image(cls, big_img, info, path):
        # 创建小图
        # little_img = Image.new('RGBA', info['sz'])
        # box –定义左，上，右和下像素坐标的4元组
        # if info['rotated']:
        #     region = region.transpose(Image.ROTATE_90)
        #box –定义左，上，右和下像素坐标的4元组
        # PIL.Image.crop()方法用于裁剪任何图像的矩形部分
        region = big_img.crop(info['box'])
        save_dir = os.path.dirname(path)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        region.save(path)

if __name__ == '__main__':
    atlas = SlicerAtlas()
    atlas.split_with_json('./resources/clo_icon4sheet.json')
    print('done')

