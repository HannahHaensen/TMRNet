import os
import numpy as np
import pickle

root_dir2 = '../data/heichole_test/'
img_dir2 = os.path.join(root_dir2, 'cutMargin')
phase_dir2 = os.path.join(root_dir2, 'phase_annotations')
# tool_dir2 = os.path.join(root_dir2, 'tool_annotations')

# train_video_num = 8
# val_video_num = 4
# test_video_num = 2

print(root_dir2)
print(img_dir2)
print(phase_dir2)


# cholec80==================
def get_dirs2(root_dir):
    file_paths = []
    file_names = []
    for lists in os.listdir(root_dir):
        path = os.path.join(root_dir, lists)
        if os.path.isdir(path):
            file_paths.append(path)
            file_names.append(os.path.basename(path))
    file_names.sort(key=lambda x: int(x))
    file_paths.sort(key=lambda x: int(os.path.basename(x)))
    return file_names, file_paths


def get_files2(root_dir):
    file_paths = []
    file_names = []
    for lists in os.listdir(root_dir):
        path = os.path.join(root_dir, lists)
        if not os.path.isdir(path):
            file_paths.append(path)
            file_names.append(os.path.basename(path))
    file_names.sort()
    file_paths.sort()
    return file_names, file_paths


# heichole==================

img_dir_names2, img_dir_paths2 = get_dirs2(img_dir2)
# tool_file_names2, tool_file_paths2 = get_files2(tool_dir2)
phase_file_names2, phase_file_paths2 = get_files2(phase_dir2)

phase_dict = {}
phase_dict_key = ['Preparation', 'CalotTriangleDissection', 'ClippingCutting', 'GallbladderDissection',
                  'GallbladderPackaging', 'CleaningCoagulation', 'GallbladderRetraction']
for i in range(len(phase_dict_key)):
    phase_dict[phase_dict_key[i]] = i
print(phase_dict)

all_info_all2 = []

for j in range(len(phase_file_names2)):
    downsample_rate = {
        1: 25,
        2: 25,
        3: 25,
        4: 25,
        5: 25,
        6: 25,
        7: 25,
        8: 25,
        9: 25,
        10: 25,
        11: 25,
        12: 25,
        13: 25,
        14: 25,
        15: 25,
        16: 50,
        17: 50,
        18: 50,
        19: 50,
        20: 50,
        21: 25,
        22: 25,
        23: 50,
        24: 50
    }
    # video 16 = 50 fps
    # video 17
    # video 18
    # video 19
    # video 20
    # video 21 = 25 fps
    # video 22 = 25 fps
    # video 23 = 50 fps
    # video 24 = 50 fps
    phase_file = open(phase_file_paths2[j])

    video_num_file = int(os.path.splitext(os.path.basename(phase_file_paths2[j]))[0][9:11])
    video_num_dir = int(os.path.basename(img_dir_paths2[j]))

    print("video_num_file:", video_num_file, "video_num_dir:", video_num_dir, "rate:", downsample_rate[video_num_dir])

    info_all = []
    first_line = True
    index = 1
    for phase_line in phase_file:
        phase_split = phase_line.split()
        if first_line:
            first_line = False
            continue
        if int(phase_split[0]) % downsample_rate[video_num_dir] == 0:
            info_each = []
            img_file_each_path = os.path.join(img_dir_paths2[j], str(index) + '.jpg')
            info_each.append(img_file_each_path)
            info_each.append(phase_dict[phase_split[1]])
            info_all.append(info_each)
            index += 1

            # print(len(info_all))
    all_info_all2.append(info_all)

with open('./heichole2.pkl', 'wb') as f:
    pickle.dump(all_info_all2, f)

with open('./heichole2.pkl', 'rb') as f:
    all_info_heiChole = pickle.load(f)

# heiChole==================
test_file_paths_heichole = []
test_labels_heichole = []

test_num_each_heiChole = []

for i in range(0, len(all_info_heiChole)):
    test_num_each_heiChole.append(len(all_info_heiChole[i]))
    for j in range(len(all_info_heiChole[i])):
        test_file_paths_heichole.append(all_info_heiChole[i][j][0])
        test_labels_heichole.append(all_info_heiChole[i][j][1:])

print(len(test_file_paths_heichole))
print(len(test_labels_heichole))

# cholec80==================


train_val_test_paths_labels = []
train_val_test_paths_labels.append(test_file_paths_heichole)

train_val_test_paths_labels.append(test_labels_heichole)

train_val_test_paths_labels.append(test_num_each_heiChole)

with open('test_paths_labels_heichole2.pkl', 'wb') as f:
    pickle.dump(train_val_test_paths_labels, f)

print('Done')
print()
