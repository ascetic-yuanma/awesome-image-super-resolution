# awesome-image-super-resolution
Paper list and implementation  (training and testing codes & results) in an unified project of CNN-based single image super-resolution algorithms, inspired by [Single-Image-Super-Resolution](https://github.com/YapengTian/Single-Image-Super-Resolution).

All the implementation results are compared with reported results in their papers. For fast training, it's only trained at scaling ratio 4.

Everyone is free to use the results for qualitative comparisons in your own work, I hope this repository can help you a lot!

If you have any suggestions, please kindly send an e-mail to yuan.ma@whut.edu.cn.

## Survey paper
[1] Anwar S, Khan S, Barnes N. A deep journey into super-resolution: A survey[J]. arXiv preprint arXiv:1904.07523, 2019. [[paper]](https://arxiv.org/pdf/1904.07523.pdf)

## Paper list and implementation results of PSNR-maximization algorithms
[1] Dong C, Loy C C, He K, et al. Image super-resolution using deep convolutional networks[J]. TPAMI, 2015, 38(2): 295-307. [[paper]](http://mmlab.ie.cuhk.edu.hk/projects/SRCNN.html)[[official project]](http://mmlab.ie.cuhk.edu.hk/projects/SRCNN.html)[[implementation results]](to be filled)

| algorithms & PSNR/SSIM |     Set5     |    Set14     |     B100     |   Urban100   |   Manga109   |
| :--------------------: | :----------: | :----------: | :----------: | :----------: | :----------: |
|         SRCNN          | 30.48/0.8628 | 27.50/0.7513 | 26.90/0.7103 | 24.52/0.7226 | 27.66/0.8580 |
|     implementation     | to be filled | to be filled | to be filled | to be filled | to be filled |

## Paper list and implementation results of PI-minimization algorithms
[1] Ledig C, Theis L, Huszár F, et al. Photo-realistic single image super-resolution using a generative adversarial network[C]//CVPR. 2017: 4681-4690.[[paper]](https://arxiv.org/pdf/1609.04802.pdf)[[implementation results]](to be filled)

| algorithms & PI/RMSE |     Set5     |    Set14     |     B100     |   Urban100   |   Manga109   |   PIRM-SR    |
| :------------------: | :----------: | :----------: | :----------: | :----------: | :----------: | :----------: |
|        SRGAN         | to be filled | to be filled | to be filled | to be filled | to be filled | to be filled |
|    implementation    | to be filled | to be filled | to be filled | to be filled | to be filled | to be filled |

