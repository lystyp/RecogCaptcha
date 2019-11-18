import os

import cv2
import tensorflow as tf
from theano.gradient import np

path = "../classify_rlt/"
model_p1 = tf.saved_model.load(path + "p1/model")
model_p2 = tf.saved_model.load(path + "p2/model")
model_p3 = tf.saved_model.load(path + "p3/model")
model_p4 = tf.saved_model.load(path + "p4/model")


def recog_single_number(raw_data, model, ex=None):
    new = np.array([raw_data] * 50).reshape(50, raw_data.shape[0] * raw_data.shape[1])
    result_list = model.call(new)
    if ex is None:
        return str(np.argmax(result_list[0]))
    else:
        return str(np.argmax(result_list[0]) + 1)


def recognize_image(img):
    result = ""
    img_p1 = img[:, 31:53]
    img_p2 = img[:, 50:72]
    img_p3 = img[:, 71:93]
    img_p4 = img[:, 90:110]
    print(img_p1.shape)
    raw_data_p1 = np.expand_dims(img_p1.astype(np.float32) / 255.0, axis=-1)
    raw_data_p2 = np.expand_dims(img_p2.astype(np.float32) / 255.0, axis=-1)
    raw_data_p3 = np.expand_dims(img_p3.astype(np.float32) / 255.0, axis=-1)
    raw_data_p4 = np.expand_dims(img_p4.astype(np.float32) / 255.0, axis=-1)
    result = result + recog_single_number(raw_data_p1, model_p1, ex=1)
    result = result + recog_single_number(raw_data_p2, model_p2)
    result = result + recog_single_number(raw_data_p3, model_p3)
    result = result + recog_single_number(raw_data_p4, model_p4)

    return result


def get_img_list():
    data_path = "../test_data/image/"
    name_list = os.listdir(data_path)
    l = []
    for img_name in name_list:
        if ".png" in img_name:
            l.append(cv2.imread(data_path + img_name, cv2.IMREAD_GRAYSCALE))
    return l


if __name__ == "__main__":
    img_list = get_img_list()
    for img in img_list:
        print(recognize_image(img))
        cv2.imshow("asd", img)
        cv2.waitKey(0)

