---
layout: default
title: A low-complexity method for efficient depth-guided image deblurring
---

# A low-complexity method for efficient depth-guided image deblurring
**arXiv**：[2601.03924v1](https://arxiv.org/abs/2601.03924) · [PDF](https://arxiv.org/pdf/2601.03924.pdf)  
**作者**：Ziyao Yi, Diego Valsesia, Tiziano Bianchi, Enrico Magli  

**一句话要点**：提出低复杂度深度引导图像去模糊方法，利用小波变换和深度信息提升效率

**关键词**：图像去模糊, 深度引导, 低复杂度神经网络, 小波变换, 移动Lidar

## 3 点简述
- 图像去模糊是高度不适定问题，深度学习模型复杂度高，难以在移动设备部署
- 采用小波变换分离结构细节并减少空间冗余，结合深度信息进行高效特征条件化
- 实验显示在保持竞争性图像质量的同时，复杂度降低达两个数量级

## 摘要（原文）

> Image deblurring is a challenging problem in imaging due to its highly ill-posed nature. Deep learning models have shown great success in tackling this problem but the quest for the best image quality has brought their computational complexity up, making them impractical on anything but powerful servers. Meanwhile, recent works have shown that mobile Lidars can provide complementary information in the form of depth maps that enhance deblurring quality. In this paper, we introduce a novel low-complexity neural network for depth-guided image deblurring. We show that the use of the wavelet transform to separate structural details and reduce spatial redundancy as well as efficient feature conditioning on the depth information are essential ingredients in developing a low-complexity model. Experimental results show competitive image quality against recent state-of-the-art models while reducing complexity by up to two orders of magnitude.

