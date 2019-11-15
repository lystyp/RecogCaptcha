import os

import numpy as np
import cv2


def get_img_list(n):
    path = "./classify_rlt/p1/" + str(n) + "/"
    name_list = os.listdir(path)
    l = []
    for img_name in name_list:
        l.append(cv2.imread(path + img_name, cv2.IMREAD_GRAYSCALE))
    print("Load " + str(n) + " finish.")
    return l


def log(s):
    print(s)
    with open("log.txt", "a") as f:
        f.write(s + "\n")


def generate_ground_truth_list():
    count = 0
    ground_truth_list = []
    for i in range(1, 10):
        print(i)
        f = open("./p1/raw_" + str(i) + ".txt", 'r').readlines()
        c = len(f)
        l = [i] * (c - count)
        print(len(l))
        ground_truth_list += l
        count = c
    arr = np.array([ground_truth_list])
    print(arr.shape)
    np.savetxt("./p1/p1_ground_truth.txt", arr)


if __name__ == "__main__":
    number_data = [get_img_list(1),
                   get_img_list(2),
                   get_img_list(3),
                   get_img_list(4),
                   get_img_list(5),
                   get_img_list(6),
                   get_img_list(7),
                   get_img_list(8),
                   get_img_list(9)]

    raw_list = None
    count = 0
    number = 1
    for img_list in number_data:
        number_raw_list = None
        log("Number " + str(number) + " start : " + str(count))
        for img in img_list:
            raw = img.reshape((1, img.shape[0] * img.shape[1]))
            if raw_list is None:
                raw_list = raw
            else:
                raw_list = np.vstack((raw_list, raw))

            if number_raw_list is None:
                number_raw_list = raw
            else:
                number_raw_list = np.vstack((number_raw_list, raw))
            count = count + 1

        np.savetxt("./classify_rlt/p1/" + str(number) + "/raw_" + str(number) + ".txt", number_raw_list)
        log("Number " + str(number) + " end : " + str(count - 1))
        log("Number " + str(number) + " len : " + str(len(img_list)))
        log("----------------------------------------------------")
        number = number + 1
    np.savetxt("./classify_rlt/p1/p1_raw_data.txt", raw_list)
