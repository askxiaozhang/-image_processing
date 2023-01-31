#智慧交通所用到的工具类
import cv2
import os
import cv2 as cv
import numpy as np

class ITS_tools(object):
     #视频转图片的方法
    @staticmethod #封装为静态方法
    def vedio_toimg(vedioPath,imgPath,save_format = '.jpg',imgNumber = 0,nameLength = 4):
        '''
        params:
            vedioPath : 视频路径 例如  u'E:\Test/123.mp4'
            imgPath : 图片路径 例如 r'F:\Test/tu/'      #保存图片路径,路径最后加/斜杠
            save_format : 保存的图片格式，默认为jpg可以改为'.png'
            imgNumber : 图片保存的名字数量默认为0开始
        '''
        print("视频转图片的方法")
        capture = cv2.VideoCapture(vedioPath)
        frame_num = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        suc = capture.isOpened() #是否成功打开
        frame_count = imgNumber #图片张数从多少开始
        while suc:
            frame_count += 1
            suc,frame = capture.read()
            cv2.imwrite(imgPath + str(frame_count).zfill(4)+save_format,frame)
            #zfill() 方法返回指定长度的字符串,原字符串右对齐,前面填充0
            #:str.zfill(width) 参数width
            if frame_num == frame_count:
                suc = False
        capture.release()
        print("视频转图片结束! ")  
    
    @staticmethod #封装为静态方法
    def img_tovedio(vedioPath,imgPath,vedio_fps = 30,isColor = 1):  #图片转为视频的方法
        '''
        parmas:
            isColor : 是否为灰度图片，灰度图为0；彩色图为1
            vedioPath : 保存的视频路径 如u'E:\Test/123.mp4'
            imgPath : 图片文件夹路径 如r'F:\Test/tu/''#设置图片文件夹的路径，末尾加/
            vedio_fps : 保存的视频帧数 默认为30
        '''
        print("正在进行图片转化为视频中……")
        fourcc = cv2.VideoWriter_fourcc( 'm', 'p', '4 ', 'v')#设置输出视频为mp4格式# cap_fps是帧率,根据自己需求设置帧率
        cap_fps = vedio_fps
        file_lst = os.listdir(imgPath)
        img = cv2.imread(imgPath + file_lst[0]) #取第一张图片的大小
        size = (img.shape[1],img.shape[0])
        video = cv2.VideoWriter(vedioPath,fourcc,vedio_fps,size,isColor)
        for filename in file_lst:
            img = cv2.imread(imgPath + filename)
            video.write(img)
        video.release()
        print("转化完毕")
        
if __name__ == "__main__": 
    vedioPath = u'E:\Test/123.mp4'
    imgPath = r'F:\Test/tu/'
    # ITS_tools.vedio_toimg(vedioPath,imgPath,imgNumber = 1)
    ITS_tools.img_tovedio(vedioPath, imgPath)
