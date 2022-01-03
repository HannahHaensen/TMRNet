import shutil
import glob
import os


# paths
source_path = '../data/cholec80_original/'
video_path = os.path.join(source_path, 'videos')
phase_path = os.path.join(source_path, 'phase_annotations')
tool_path = os.path.join(source_path, 'tool_annotations')


# create target folder tree
target_path = '../data/cholec80_test/'
target_video_path = os.path.join(target_path, 'videos')

if not os.path.exists(target_path):
    os.mkdir(target_path)

if not os.path.exists(target_video_path):
    os.mkdir(target_video_path)

# get list of videos
videos = [v for v in os.listdir(video_path) if v.endswith('.mp4')]

# create a target video folder and convert to frames
for v in videos:
    #  target video name
    video_name = str(int(v.split('.')[0][-2] + v.split('.')[0][-1]))
    # video_name = v.split('.')[0]
    target_frame_path = os.path.join(target_video_path, video_name)
    
    # create target folder
    if not os.path.exists(target_frame_path):
        os.mkdir(target_frame_path)

    print('processing... ', os.path.join(video_path, v), 
        os.path.join(target_frame_path, video_name))
    
    # convert video into frames
    os.system('ffmpeg -i {} -r 1 -filter:v fps=fps=1 {}/%d.jpg'.format(
        os.path.join(video_path, v), target_frame_path))
    break

# TODO
# Copy phase and tool annotations
