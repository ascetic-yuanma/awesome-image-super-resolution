# awesome-image-super-resolution
Paper list and implementation  (training and testing codes & results) of CNN-based single image super-resolution algorithms, inspired by [Single-Image-Super-Resolution](https://github.com/YapengTian/Single-Image-Super-Resolution).

All the implementation results are compared with reported results in their papers. For fast training, it's only trained at scaling ratio 4.

Everyone is free to use the results for qualitative comparisons in your own work, I hope this repository can help you a lot!

If you have any suggestions, please kindly send an e-mail to yuan.ma@whut.edu.cn.
## Requirements
Python = 3.6  
PyTorch = 1.1
## Survey paper
[1] Anwar S, Khan S, Barnes N. A deep journey into super-resolution: A survey[J]. arXiv preprint arXiv:1904.07523, 2019. [[paper]](https://arxiv.org/pdf/1904.07523.pdf)
## Paper list and implementation of CNN-based algorithms
[1] Dong C, Loy C C, He K, et al. Image super-resolution using deep convolutional networks[J]. IEEE transactions on pattern analysis and machine intelligence, 2015, 38(2): 295-307. [[paper]](http://mmlab.ie.cuhk.edu.hk/projects/SRCNN.html)[[official project]](http://mmlab.ie.cuhk.edu.hk/projects/SRCNN.html)

For training:	`python main.py -opt options\\train\\train_SRCNN.yml`  
For testing:	`python main.py -opt options\\test\\train_SRCNN.yml`  

|    algorithms    | Set5  | Set14 | B100  | Urban100 | Manga109 |
| :--------------: | :---: | :---: | :---: | :------: | :------: |
| reported results | 0.001 | 0.001 | 0.001 |  0.001   |  0.001   |
|  implementation  | 0.001 | 0.001 | 0.001 |  0.001   |  0.001   |

