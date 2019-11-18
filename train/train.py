import os
import time

import cv2
import numpy as np
import tensorflow as tf
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'


num_epochs = ㄓㄢ
batch_size = 50
learning_rate = 0.001

path = "../classify_rlt/p2/"
name_p = "p2"

class DATALoader():
    def __init__(self):
        self.train_data = self.get_data_list()
        self.train_label = self.get_ground_truth_list()

        self.train_data = self.train_data.astype(np.float32) / 255.0      # [60000, 28, 28, 1]
        self.train_label = self.train_label.astype(np.int32)    # [60000]
        self.num_train_data = self.train_data.shape[0]

    def get_batch(self, batch_size):
        # 从数据集中随机取出batch_size个元素并返回
        index = np.random.randint(0, np.shape(self.train_data)[0], batch_size)
        return self.train_data[index, :], self.train_label[index]

    def get_ground_truth_list(self):
        return np.loadtxt(path + name_p + "_ground_truth.txt")

    def get_data_list(self):
        return np.loadtxt(path + name_p + "_raw_data.txt")


class MLP(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.dense1 = tf.keras.layers.Dense(units=100, activation=tf.nn.relu)
        self.dense2 = tf.keras.layers.Dense(units=10)

    @tf.function
    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        output = tf.nn.softmax(x)
        return output


if __name__ == "__main__":
    data_loader = DATALoader()
    print("Start")
    n = 0
    for i in data_loader.train_data:
        print(data_loader.train_label[n])
        cv2.imshow("asd", i.reshape(45, 22))
        n = n + 1




    input("PAUSE")
    t_start = time.time()

    model = MLP()
    data_loader = DATALoader()
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    num_batches = int(data_loader.num_train_data // batch_size * num_epochs)
    for batch_index in range(num_batches):
        X, y = data_loader.get_batch(batch_size)
        with tf.GradientTape() as tape:
            y_pred = model(X)
            loss = tf.keras.losses.sparse_categorical_crossentropy(y_true=y, y_pred=y_pred)
            loss = tf.reduce_mean(loss)
            print("batch %d: loss %f" % (batch_index, loss.numpy()))
        grads = tape.gradient(loss, model.variables)
        optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))

    print("End")
    print(time.time() - t_start)
    tf.saved_model.save(model, path + "model/")

