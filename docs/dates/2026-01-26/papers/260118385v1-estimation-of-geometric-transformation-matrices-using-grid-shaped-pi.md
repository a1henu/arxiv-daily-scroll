---
layout: default
title: Estimation of geometric transformation matrices using grid-shaped pilot signals
---

# Estimation of geometric transformation matrices using grid-shaped pilot signals
**arXiv**：[2601.18385v1](https://arxiv.org/abs/2601.18385) · [PDF](https://arxiv.org/pdf/2601.18385.pdf)  
**作者**：Rinka Kawano, Masaki Kawamura  

**一句话要点**：提出基于网格形导频信号估计几何变换矩阵的数字水印方法，以解决裁剪攻击下的同步问题。

**关键词**：数字水印, 几何变换估计, 裁剪鲁棒性, 网格形导频信号, Radon变换, 图像同步

## 3 点简述
- 核心问题：数字水印在图像裁剪等几何失真攻击下同步困难，现有方法对裁剪鲁棒性不足。
- 方法要点：嵌入网格形导频信号，通过Radon变换分析失真网格的角度和间隔，估计变换矩阵并确定方向。
- 实验或效果：模拟各向异性缩放、旋转、剪切和裁剪攻击，结果显示方法能准确估计变换矩阵，误差较低。

## 摘要（原文）

> Digital watermarking techniques are essential to prevent unauthorized use of images. Since pirated images are often geometrically distorted by operations such as scaling and cropping, accurate synchronization - detecting the embedding position of the watermark - is critical for proper extraction. In particular, cropping changes the origin of the image, making synchronization difficult. However, few existing methods are robust against cropping. To address this issue, we propose a watermarking method that estimates geometric transformations applied to a stego image using a pilot signal, allowing synchronization even after cropping. A grid-shaped pilot signal with distinct horizontal and vertical values is embedded in the image. When the image is transformed, the grid is also distorted. By analyzing this distortion, the transformation matrix can be estimated. Applying the Radon transform to the distorted image allows estimation of the grid angles and intervals. In addition, since the horizontal and vertical grid lines are encoded differently, the grid orientation can be determined, which reduces ambiguity. To validate our method, we performed simulations with anisotropic scaling, rotation, shearing, and cropping. The results show that the proposed method accurately estimates transformation matrices with low error under both single and composite attacks.

