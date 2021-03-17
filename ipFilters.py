import cv2
import numpy as np

def resize(img, output_size):
    return cv2.resize(img, output_size)

def clip(img, maxI, minI=0):
    img[np.where(img < minI)] = minI
    img[np.where(img > maxI)] = maxI
    return img

def flip(img, horizontal=True, vertical=False):
    if horizontal:
        img = np.flip(img, 1)
    if vertical:
        img = np.flip(img, 0)
    return img

def crop(img, r1, c1, h, w):
    return img[r1:r1 + h, c1:c1 + w]

def sharpen(img, factor=4):
    sharp = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    kernel = sharp * np.random.random() * factor / 4
    kernel[1, 1] += 1
    return cv2.filter2D(img, -1, kernel)

def blur(img, level):
    level = int(level / 2) * 2 + 1
    img = cv2.GaussianBlur(img, (level, level), 0)
    return img

def translate(img, r1, c1):
    height, width = img.shape[:2]
    T = np.float32([[1, 0, r1], [0, 1, c1]])
    return cv2.warpAffine(img, T, (width, height))

def padding(img, padX=10, padY=10, color=(0, 0, 0)):
    height, width, c = img.shape
    heightNew = height + 2 * padX
    widthNew = width + 2 * padY
    result = np.full((heightNew, widthNew, c), color, dtype=np.uint8)
    result[padX:height + padX, padY:width + padY] = img
    return result

def rotate(img, angle=0):
    imgCenter = tuple(np.array(img.shape[1::-1]) / 2)
    rotMat = cv2.getRotationMatrix2D(imgCenter, angle, 1.0)
    result = cv2.warpAffine(img, rotMat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

def shear(img, shearLevelX, shearLevelY):
    # shearLevel should be between 0 and 1, float value
    height, width = img.shape[:2]
    matrix = np.eye(3)
    if shearLevelX:
        matrix = matrix @ np.float32([[1, 0.5 * shearLevelX, 0], [0, 1, 0], [0, 0, 1]])
    if shearLevelY:
        matrix = matrix @ np.float32([[1, 0, 0], [0.5 * shearLevelY, 1, 0], [0, 0, 1]])
    return cv2.warpPerspective(img, matrix, (int(width * 1.5), int(height * 1.5)))

def brightness(img, alpha, beta):
    alpha = np.array([alpha])
    beta = np.array([beta])
    cv2.multiply(img, alpha, img)
    cv2.add(img, beta, img)

    return img

def gamma(img, gamma):
    Lab = cv2.split(cv2.cvtColor(img.astype('uint8'), cv2.COLOR_BGR2LAB))
    Lab[0] = (((Lab[0] / 255.0)**gamma) * 255.0).astype('uint8')
    return cv2.cvtColor(cv2.merge(Lab), cv2.COLOR_LAB2BGR)

def noise(img, level):
    noise = np.random.normal(0, level, img.shape)
    return np.clip(img + noise, 0, 255).astype("uint8")

def histEqual(img):
    Lab = cv2.split(cv2.cvtColor(img.astype('uint8'), cv2.COLOR_BGR2LAB))
    Lab[0] = cv2.equalizeHist(Lab[0])
    return cv2.cvtColor(cv2.merge(Lab), cv2.COLOR_LAB2BGR)

def Clahe(img, clip=2.0, size=8):
    Clahe = cv2.createCLAHE(clipLimit=float(clip), tileGridSize=(int(size), int(size)))
    Lab = cv2.split(cv2.cvtColor(img.astype('uint8'), cv2.COLOR_BGR2LAB))
    Lab[0] = Clahe.apply(Lab[0])
    return cv2.cvtColor(cv2.merge(Lab), cv2.COLOR_LAB2BGR)

class Vignetting(object):
    def __init__(self,
                 ratio_min_dist=0.2,
                 range_vignette=(0.2, 0.8),
                 vignette=0.3,
                 random_sign=False):
        self.ratio_min_dist = ratio_min_dist
        self.range_vignette = np.array(range_vignette)
        self.random_sign = random_sign
        self.vignette = vignette

    def __call__(self, img):
        h, w = img.shape[:2]
        min_dist = np.array([h, w]) / 2 * np.random.random() * self.ratio_min_dist

        # create matrix of distance from the center on the two axis
        x, y = np.meshgrid(np.linspace(-w / 2, w / 2, w), np.linspace(-h / 2, h / 2, h))
        x, y = np.abs(x), np.abs(y)

        # create the vignette mask on the two axis
        x = (x - min_dist[0]) / (np.max(x) - min_dist[0])
        x = np.clip(x, 0, 1)
        y = (y - min_dist[1]) / (np.max(y) - min_dist[1])
        y = np.clip(y, 0, 1)

        # then get a random intensity of the vignette
        vignette = (x + y) / 2 * self.vignette
        vignette = np.tile(vignette[..., None], [1, 1, 3])

        sign = 2 * (self.random_sign) - 1
        img = np.round(img * (1 + sign * vignette) / 20)

        return img

class LensDistortion(object):
    def __init__(self, d_coef=(0.15, 0.15, 0.1, 0.1, 0.05), amount=1):
        self.d_coef = np.array(d_coef)
        self.amount = amount

    def __call__(self, img):

        # get the height and the width of the image
        h, w = img.shape[:2]

        # compute its diagonal
        f = (h ** 2 + w ** 2) ** 0.5

        # set the image projective to carrtesian dimension
        K = np.array([[f, 0, w / 2],
                      [0, f, h / 2],
                      [0, 0, 1]])

        d_coef = self.d_coef * self.amount  # value
        d_coef = d_coef * (2 * (np.random.random(5) < 0.5) - 1)  # sign
        # Generate new camera matrix from parameters
        M, _ = cv2.getOptimalNewCameraMatrix(K, d_coef, (w, h), 0)

        # Generate look-up tables for remapping the camera image
        remap = cv2.initUndistortRectifyMap(K, d_coef, None, M, (w, h), 5)

        # Remap the original image to a new image
        img = cv2.remap(img, *remap, cv2.INTER_LINEAR)
        return img

def LinearContrastStretching(img):
    '''
    Performs contrast stretching on the input image according to a piecewise linear mapping
    args --
        img - the input image passed as a numpy array
    '''
    L = 255
    minI, maxI = np.ndarray.min(img), np.ndarray.max(img)
    img = (img * 255 / (maxI - minI))
    img = np.multiply(img / 2, img < L / 8) + np.multiply(-L / 4 + 3 * img / 2, np.multiply(img >= L / 8, img <= 7 * L / 8)) + np.multiply(3 * L / 4 + img / 2, img > 7 * L / 8)
    minI, maxI = np.ndarray.min(img), np.ndarray.max(img)
    img = (img * 255 / (maxI - minI))
    return np.clip(img, 0, 255).astype("uint8")
