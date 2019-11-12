import os
import traceback

import numpy as np
import cv2

if __name__ == "__main__":
    fp = open('number_captcha_match.txt', "r")
    p1 = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        '0': 0
    }
    p2 = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        '0': 0
    }
    p3 = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        '0': 0
    }
    p4 = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        '0': 0
    }

    for line in iter(fp):
        try:
            c = line.split(",")[1].replace("\n", "")
            i = int(c)
            if len(c) == 4:
                # os.rename('classify_src\\' + c + '.png',
                #           'classify_rlt2\\' + c + '.png')
                img = cv2.imread('classify_src\\' + c + '.png', cv2.IMREAD_GRAYSCALE)
                img_p1 = img[:, 31:53]
                img_p2 = img[:, 50:72]
                img_p3 = img[:, 71:93]
                img_p4 = img[:, 90:110]
                cv2.imwrite('classify_rlt\p1\\' + c[0] + "\\" + str(p1[c[0]]) + '.png', img_p1)
                p1[c[0]] = p1[c[0]] + 1
                cv2.imwrite('classify_rlt\p2\\' + c[1] + "\\" + str(p2[c[1]]) + '.png', img_p2)
                p2[c[1]] = p2[c[1]] + 1
                cv2.imwrite('classify_rlt\p3\\' + c[2] + "\\" + str(p3[c[2]]) + '.png', img_p3)
                p3[c[2]] = p3[c[2]] + 1
                cv2.imwrite('classify_rlt\p4\\' + c[3] + "\\" + str(p4[c[3]]) + '.png', img_p4)
                p4[c[3]] = p4[c[3]] + 1
        except Exception as e:
            print(traceback.format_exc())

    fp.close()
