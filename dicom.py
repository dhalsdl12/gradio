# DICOM 이미지 디코딩 하기

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_io as tfio

image_bytes = tf.io.read_file('dicom_00000001_000.dcm')
image = tfio.image.decode_dicom_image(image_bytes, dtype=tf.uint16)
skipped = tfio.image.decode_dicom_image(image_bytes, on_error='skip', dtype=tf.uint8)
lossy_image = tfio.image.decode_dicom_image(image_bytes, scale='auto', on_error='lossy', dtype=tf.uint8)

print(image_bytes)

fig, axes = plt.subplots(1,3, figsize=(10,10))
axes[0].imshow(np.squeeze(image.numpy()), cmap='gray')
axes[0].set_title('image')
axes[1].imshow(np.squeeze(skipped.numpy()), cmap='gray')
axes[1].set_title('skipped')
axes[2].imshow(np.squeeze(lossy_image.numpy()), cmap='gray')
axes[2].set_title('lossy image')