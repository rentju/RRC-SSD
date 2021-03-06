import os.path
import glob
import cv2
import numpy as np

def dark(jpgfile, outdir):
    img = cv2.imread(jpgfile)
    try:
        # print(u'正在处理中')
        w = img.shape[1]
        h = img.shape[0]
        k= 0.1
        # 全部变暗
        for xi in range(0, w):
            for xj in range(0, h):
                # 将像素值整体减少，设为原像素值的20%
                img[xj, xi, 0] = int(img[xj, xi, 0] * k)
                img[xj, xi, 1] = int(img[xj, xi, 1] * k)
                img[xj, xi, 2] = int(img[xj, xi, 2] * k)
            # 显示进度条
        # if xi % 1000 == 0:
        #     print('.')
        cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), img)

    except Exception as e:
            print(e)

for jpgfile in glob.glob(r'D:\kitti\data_object_image_2\training\image_2\*.png'):
    dark(jpgfile, r'D:\kitti\dark5\10')
