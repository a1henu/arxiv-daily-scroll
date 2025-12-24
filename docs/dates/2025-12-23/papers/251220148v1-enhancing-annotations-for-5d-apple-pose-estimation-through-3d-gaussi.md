---
layout: default
title: Enhancing annotations for 5D apple pose estimation through 3D Gaussian Splatting (3DGS)
---

# Enhancing annotations for 5D apple pose estimation through 3D Gaussian Splatting (3DGS)
**arXiv**：[2512.20148v1](https://arxiv.org/abs/2512.20148) · [PDF](https://arxiv.org/pdf/2512.20148.pdf)  
**作者**：Robert van de Ven, Trim Bresilla, Bram Nelissen, Ard Nieuwenhuizen, Eldert J. van Henten, Gert Kootstra  

**一句话要点**：提出基于3D高斯泼溅的苹果姿态估计标注增强流程，以解决果园环境中遮挡导致的标注困难问题。

**关键词**：苹果姿态估计, 3D高斯泼溅, 标注增强, 果园自动化, 遮挡处理, 3D重建

## 3 点简述
- 核心问题：果园自动化任务中苹果姿态估计因环境变化和遮挡导致关键点标注耗时且不一致。
- 方法要点：利用3D高斯泼溅重建场景，简化标注并自动投影至图像，大幅减少手动标注需求。
- 实验或效果：实验显示，使用≤95%遮挡的标签训练效果最佳，F1分数达0.927，但姿态估计方法未能正确学习苹果方向。

## 摘要（原文）

> Automating tasks in orchards is challenging because of the large amount of variation in the environment and occlusions. One of the challenges is apple pose estimation, where key points, such as the calyx, are often occluded. Recently developed pose estimation methods no longer rely on these key points, but still require them for annotations, making annotating challenging and time-consuming. Due to the abovementioned occlusions, there can be conflicting and missing annotations of the same fruit between different images. Novel 3D reconstruction methods can be used to simplify annotating and enlarge datasets. We propose a novel pipeline consisting of 3D Gaussian Splatting to reconstruct an orchard scene, simplified annotations, automated projection of the annotations to images, and the training and evaluation of a pose estimation method. Using our pipeline, 105 manual annotations were required to obtain 28,191 training labels, a reduction of 99.6%. Experimental results indicated that training with labels of fruits that are $\leq95\%$ occluded resulted in the best performance, with a neutral F1 score of 0.927 on the original images and 0.970 on the rendered images. Adjusting the size of the training dataset had small effects on the model performance in terms of F1 score and pose estimation accuracy. It was found that the least occluded fruits had the best position estimation, which worsened as the fruits became more occluded. It was also found that the tested pose estimation method was unable to correctly learn the orientation estimation of apples.

