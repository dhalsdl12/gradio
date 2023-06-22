import matplotlib.pyplot as plt
import numpy as np
import pydicom


def dcm(input_file):
    # DICOM 이미지 파일 읽기
    dcm = pydicom.dcmread(input_file)
    image = dcm.pixel_array

    # 이미지 출력
    '''
    plt.imshow(image, cmap='gray')
    plt.title('image')
    plt.show()
    '''

    return image