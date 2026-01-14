---
layout: default
title: Second-order Gaussian directional derivative representations for image high-resolution corner detection
---

# Second-order Gaussian directional derivative representations for image high-resolution corner detection
**arXiv**：[2601.08182v1](https://arxiv.org/abs/2601.08182) · [PDF](https://arxiv.org/pdf/2601.08182.pdf)  
**作者**：Dongbo Xie, Junjie Qiu, Changming Sun, Weichuan Zhang  

**一句话要点**：提出基于二阶高斯方向导数的图像高分辨率角点检测方法，以解决相邻角点灰度相互影响的问题。

**关键词**：角点检测, 二阶高斯方向导数, 高分辨率图像, 图像匹配, 3D重建

## 3 点简述
- 核心问题：现有角点检测方法中，简单角点模型存在理论缺陷，相邻角点灰度信息会相互干扰。
- 方法要点：使用二阶高斯方向导数滤波器平滑高分辨率角点模型，推导其表示并发现新特征，指导高斯尺度选择以准确描绘相邻角点。
- 实验或效果：新方法在定位误差、图像模糊鲁棒性、图像匹配和3D重建方面优于现有先进方法。

## 摘要（原文）

> Corner detection is widely used in various computer vision tasks, such as image matching and 3D reconstruction. Our research indicates that there are theoretical flaws in Zhang et al.'s use of a simple corner model to obtain a series of corner characteristics, as the grayscale information of two adjacent corners can affect each other. In order to address the above issues, a second-order Gaussian directional derivative (SOGDD) filter is used in this work to smooth two typical high-resolution angle models (i.e. END-type and L-type models). Then, the SOGDD representations of these two corner models were derived separately, and many characteristics of high-resolution corners were discovered, which enabled us to demonstrate how to select Gaussian filtering scales to obtain intensity variation information from images, accurately depicting adjacent corners. In addition, a new high-resolution corner detection method for images has been proposed for the first time, which can accurately detect adjacent corner points. The experimental results have verified that the proposed method outperforms state-of-the-art methods in terms of localization error, robustness to image blur transformation, image matching, and 3D reconstruction.

