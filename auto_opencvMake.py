import os
import numpy as np
import cv2

save_point = []
location = []

def search(dirname):
    global save_point, location

    focusimages = []

    for path, direct, files in os.walk(dirname):

        if path.split('\\')[0] == 'resize':
            first_path = path.replace("\\",'/')
            save_point.append(first_path.split('/')[-1])
            location.append(first_path)
        else:
            pass
    del location[0]
    del save_point[0]
    make_folder(save_point)
    image_opencv(location)

    # print(location)
    # print(save_point)


def make_folder(save_point):
        os.makedirs('new', exist_ok = True)

        for i in save_point:
            # print(i)
            os.makedirs('new/'+i, exist_ok = True)


###############################################################
# 여기에 이미지 처리를 위한 opencv의 다양한 함수 사용
# 마지막 변수명만 dst로 작성

def make_image_opencv(original):
    sharpening_2 = np.array([[-1, -1, -1, -1, -1],
                [-1, 2, 2, 2, -1],
                [-1, 2, 9, 2, -1],
                [-1, 2, 2, 2, -1],
                [-1, -1, -1, -1, -1]]) / 9.0

    dst = cv2.filter2D(original, -1, sharpening_2)
    
    return dst
###############################################################


def image_opencv(locatrion):

    for se_path in location:
        print(se_path)
        image_files = sorted(os.listdir(se_path))
    # print(len(image_files))

        for img in image_files:
            if img.split(".")[-1].lower() not in ["jpg", "jpeg", "png", "bmp"]:
                image_files.remove(img)
        
        for start in image_files:
            original = cv2.imdecode(np.fromfile(se_path+"/{}".format(start), np.uint8), cv2.IMREAD_COLOR)
            # cv2.imshow('original',original)
            # cv2.waitKey(0)

            dst = make_image_opencv(original)

            save_path = 'new/'+se_path.split('/')[-1]
            print(save_path+'/'+start)
            cv2.imwrite(save_path+'/'+start, dst)

###############################################################
# 폴더 위치를 작성해주세요 ex) resize 있는 곳

start_folder = 'resize' 
search(start_folder)
