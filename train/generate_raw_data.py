import os

import numpy as np
import cv2

data_path = "../classify_rlt/p4/"


def get_img_list(n):
    path = data_path + str(n) + "/"
    name_list = os.listdir(path)
    l = []
    for img_name in name_list:
        if ".png" in img_name:
            l.append(cv2.imread(path + img_name, cv2.IMREAD_GRAYSCALE))
    print("Load " + str(n) + " finish.")
    return l


def log(s):
    print(s)
    with open("log.txt", "a") as f:
        f.write(s + "\n")


if __name__ == "__main__":
    number_data = [get_img_list(0),
                   get_img_list(1),
                   get_img_list(2),
                   get_img_list(3),
                   get_img_list(4),
                   get_img_list(5),
                   get_img_list(6),
                   get_img_list(7),
                   get_img_list(8),
                   get_img_list(9)]

    raw_list = None
    ground_truth_list = []
    count = 0
    number = 0
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

        np.savetxt(data_path + str(number) + "/raw_" + str(number) + ".txt", number_raw_list)
        ground_truth_list = ground_truth_list + [number] * number_raw_list.shape[0]
        log("Number " + str(number) + " end : " + str(count - 1))
        log("Number " + str(number) + " len : " + str(len(img_list)))
        log("----------------------------------------------------")
        number = number + 1
    np.savetxt(data_path + "p4_raw_data.txt", raw_list)
    np.savetxt(data_path + "p4_ground_truth.txt", np.array(ground_truth_list))
