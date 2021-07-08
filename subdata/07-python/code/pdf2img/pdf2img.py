#!/usr/bin/python3
#********************************************
# PDF 转图片,将要转换的 pdf 文件放在 pdf 目录
#********************************************
# 需要安装 pdf2image
# pip install pdf2image
#********************************************
#********************************************
# 有的 pdf 拆分后乱码,可以先用电脑把 pdf 打印成 pdf
# 这样新的 pdf 其实就是一张图片
#********************************************
#[pdf2image](https://pypi.org/project/pdf2image/)
#[poppler-windows](http://blog.alivate.com.au/poppler-windows/)
#********************************************

poppler_path = r"poppler-0.68.0\bin"
print(poppler_path)

from pdf2image import convert_from_path, convert_from_bytes

# 定义拆分方法，将pdf文件拆分到对应文件名的目录,图片名按索引
def splitPdf(file,outdir):
    print('正在拆分',file)
    images = convert_from_path(file,poppler_path=poppler_path)
    print('{0} 拆分完成，共{1}张'.format(file,len(images)))
    #如果输出目录不存在则创建
    if not os.path.exists(outdir):
        #print('dir not exists')
        os.makedirs(outdir)
    for im in images:
        #w, h = im.size
        #print('Original image size: %sx%s' % (w, h))
        index=images.index(im)
        print('正在保存第{0}张'.format(index+1))
        im.save('{0}\{1}.jpg'.format(outdir,index),'JPEG')
    
# 统一放到 pdf 目录，输出到 pdf\out
import os
path=r"pdf"
#获取 pdf 目录下的所有 pdf 列表
files= os.listdir(path)
for file in files:
    #拆分文件名和后缀名
    filename,type=os.path.splitext(file)
    #只处理PDF文件
    if type.lower()=='.pdf':
        splitPdf('{0}\{1}'.format(path,file),'{0}\{1}\{2}'.format(path,'out',filename))
print('PDF 处理完毕')
