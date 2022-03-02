# blenderproc run examples/basics/physics_positioning/main.py examples/basics/physics_positioning/output

import subprocess
import sys

cmd = [#("resnest", 'python eval/python/test_singlenet_phase_non-local_pretrained_2fc_copy_mutiConv6_resnest.py -n "./Training TMRNet/best_model/non-local/pretrained_lr5e-7_L30_2fc_copy_mutiConv6_resnest_bs40/lstm_epoch_4_length_10_opt_0_mulopt_1_flip_1_crop_1_batch_50_train_9859_val_9126.pth" --lfb "False" --test_path_labels eval/python/test_paths_labels_heichole.pkl'),
       #("resnest", 'python eval/python/test_singlenet_phase_non-local_pretrained_2fc_copy_mutiConv6_resnest.py -n "./Training TMRNet/best_model/non-local/pretrained_lr5e-7_L30_2fc_copy_mutiConv6_resnest_bs50_run2/lstm_epoch_2_length_10_opt_0_mulopt_1_flip_1_crop_1_batch_50_train_9811_val_9035.pth" --lfb "True" --test_path_labels eval/python/test_paths_labels_heichole.pkl'),
       #("resnest", 'python eval/python/test_singlenet_phase_non-local_pretrained_2fc_copy_mutiConv6_resnest.py -n "./Training TMRNet/best_model/non-local/pretrained_lr5e-7_L30_2fc_copy_mutiConv6_resnest_bs50_run3/lstm_epoch_3_length_10_opt_0_mulopt_1_flip_1_crop_1_batch_50_train_9841_val_9064.pth" --lfb "True" --test_path_labels eval/python/test_paths_labels_heichole.pkl'),
       #("resnest", 'python eval/python/test_singlenet_phase_non-local_pretrained_2fc_copy_mutiConv6_resnest.py -n "./Training TMRNet/best_model/non-local/pretrained_lr5e-7_L30_2fc_copy_mutiConv6_resnest_bs50_run4/lstm_epoch_4_length_10_opt_0_mulopt_1_flip_1_crop_1_batch_50_train_9867_val_9095.pth" --lfb "True" --test_path_labels eval/python/test_paths_labels_heichole.pkl'),
       #("resnest", 'python eval/python/test_singlenet_phase_non-local_pretrained_2fc_copy_mutiConv6_resnest.py -n "./Training TMRNet/best_model/non-local/pretrained_lr5e-7_L30_2fc_copy_mutiConv6_resnest_bs50_run5/lstm_epoch_4_length_10_opt_0_mulopt_1_flip_1_crop_1_batch_50_train_9860_val_9050.pth" --lfb "True" --test_path_labels eval/python/test_paths_labels_heichole.pkl'),
       ("multiConv", 'python eval/python/test_singlenet_phase_non-local_pretrained_2fc_copy_mutiConv6_3.py -n "./Training TMRNet/best_model/non-local/pretrained_lr5e-7_L30_2fc_copy_mutiConv6_3/lstm_epoch_5_length_10_opt_0_mulopt_1_flip_1_crop_1_batch_50_train_9912_val_8927.pth" --lfb "True" --test_path_labels eval/python/test_paths_labels_heichole.pkl'),
       ("multiConv", 'python eval/python/test_singlenet_phase_non-local_pretrained_2fc_copy_mutiConv6_3.py -n "./Training TMRNet/best_model/non-local/pretrained_lr5e-7_L30_2fc_copy_mutiConv6_3_run2/lstm_epoch_9_length_10_opt_0_mulopt_1_flip_1_crop_1_batch_50_train_9935_val_8885.pth" --lfb "True" --test_path_labels eval/python/test_paths_labels_heichole.pkl'),
       ("multiConv", 'python eval/python/test_singlenet_phase_non-local_pretrained_2fc_copy_mutiConv6_3.py -n "./Training TMRNet/best_model/non-local/pretrained_lr5e-7_L30_2fc_copy_mutiConv6_3_run3/lstm_epoch_18_length_10_opt_0_mulopt_1_flip_1_crop_1_batch_50_train_9953_val_8904.pth" --lfb "True" --test_path_labels eval/python/test_paths_labels_heichole.pkl'),
       ("multiConv", 'python eval/python/test_singlenet_phase_non-local_pretrained_2fc_copy_mutiConv6_3.py -n "./Training TMRNet/best_model/non-local/pretrained_lr5e-7_L30_2fc_copy_mutiConv6_3_run4/lstm_epoch_0_length_10_opt_0_mulopt_1_flip_1_crop_1_batch_50_train_9180_val_8833.pth" --lfb "True" --test_path_labels eval/python/test_paths_labels_heichole.pkl'),
       ("multiConv", 'python eval/python/test_singlenet_phase_non-local_pretrained_2fc_copy_mutiConv6_3.py -n "./Training TMRNet/best_model/non-local/pretrained_lr5e-7_L30_2fc_copy_mutiConv6_3_run5/lstm_epoch_9_length_10_opt_0_mulopt_1_flip_1_crop_1_batch_50_train_9932_val_8885.pth" --lfb "True" --test_path_labels eval/python/test_paths_labels_heichole.pkl')]

for i in range(len(cmd)):
    output_file = cmd[i][0] + '_' + str(i) + '.txt'
    sys.stdout = open(output_file, 'w+')
    subprocess.call(cmd[i][1], stdout=sys.stdout, stderr=subprocess.STDOUT)
    print("done " + str(i))

