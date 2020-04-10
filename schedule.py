import os

os.system("python train.py -opt options/train/train_test.yml")

os.system("python test.py -opt options/test/test_test.yml")