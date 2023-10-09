import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_erosion, binary_dilation, binary_opening
from skimage.measure import label


def invoice(image):
    image = label(image)
    len = 0
    for y in range(image.shape[0]):
        if np.max(image[y]) > len:
            len = np.max(image[y])
    return len


def erosion_by_mask(image, mask):
    image = binary_erosion(image, structure=mask)
    return invoice(image)


image = np.load(f"stars.npy")
imageLab = image

totalAccount = invoice(image)

plusAccount = erosion_by_mask(imageLab, np.array([[1., 0, 1.], [0, 1., 0], [1., 0, 1.]]))
crossesAccount = erosion_by_mask(imageLab, np.array([[0, 1., 0], [1., 1., 1.], [0, 1., 0]]))

print(f"На картинке: {totalAccount - plusAccount} звезд плюсиков")
print(f"На картинке: {totalAccount - crossesAccount} звезд крестиков")
