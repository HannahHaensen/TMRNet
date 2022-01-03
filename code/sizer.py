import os
import glob
import cv2

source_path = '../data/cholec80/cutMargin/'
videos = os.listdir(source_path)

def change_size(image):
    binary_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image2 = cv2.threshold(binary_image, 15, 255, cv2.THRESH_BINARY)
    binary_image2 = cv2.medianBlur(binary_image2,
                                   19)  # filter the noise, need to adjust the parameter based on the dataset
    x = binary_image2.shape[0]
    y = binary_image2.shape[1]

    edges_x = []
    edges_y = []
    for i in range(x):
        for j in range(10, y - 10):
            if binary_image2.item(i, j) != 0:
                edges_x.append(i)
                edges_y.append(j)

    if not edges_x:
        return image

    left = min(edges_x)  # left border
    right = max(edges_x)  # right
    width = right - left
    bottom = min(edges_y)  # bottom
    top = max(edges_y)  # top
    height = top - bottom

    pre1_picture = image[left:left + width, bottom:bottom + height]

    # print(pre1_picture.shape)

    return pre1_picture


for v in videos:
    print(v)
    frames = glob.iglob(os.path.join(source_path, v, '*.jpg'))

    for f in frames:
        frame = cv2.imread(f)
        if frame.shape[0] != 250:
            frame = change_size(frame)
            res = cv2.resize(frame, dsize=(250, 250), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(f, res)
    print("frames done")

cv2.destroyAllWindows()
print("Cut Done")