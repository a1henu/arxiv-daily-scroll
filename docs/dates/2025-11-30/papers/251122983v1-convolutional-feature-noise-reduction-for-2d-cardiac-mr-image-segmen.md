---
layout: default
title: Convolutional Feature Noise Reduction for 2D Cardiac MR Image Segmentation
---

# Convolutional Feature Noise Reduction for 2D Cardiac MR Image Segmentation
**arXiv**：[2511.22983v1](https://arxiv.org/abs/2511.22983) · [PDF](https://arxiv.org/pdf/2511.22983.pdf)  
**作者**：Hong Zheng, Nan Mu, Han Su, Lin Feng, Xiaoning Li  

**一句话要点**：提出卷积特征滤波器以降低2D心脏MR图像分割中的特征噪声

**关键词**：卷积特征滤波, 噪声抑制, 心脏MR图像分割, 特征信号处理, 信息熵分析

## 3 点简述
- 核心问题：分割网络中卷积特征噪声常被忽视，可能影响整体特征系统性能。
- 方法要点：设计低幅度通滤波器，将卷积特征视为高斯分布信号矩阵进行噪声抑制。
- 实验或效果：在两种分割网络和两个公开心脏MR数据集上验证，特征信号矩阵噪声减少，并开发二值化方程计算信息熵以量化分析。

## 摘要（原文）

> Noise reduction constitutes a crucial operation within Digital Signal Processing. Regrettably, it frequently remains neglected when dealing with the processing of convolutional features in segmentation networks. This oversight could trigger the butterfly effect, impairing the subsequent outcomes within the entire feature system. To complete this void, we consider convolutional features following Gaussian distributions as feature signal matrices and then present a simple and effective feature filter in this study. The proposed filter is fundamentally a low-amplitude pass filter primarily aimed at minimizing noise in feature signal inputs and is named Convolutional Feature Filter (CFF). We conducted experiments on two established 2D segmentation networks and two public cardiac MR image datasets to validate the effectiveness of the CFF, and the experimental findings demonstrated a decrease in noise within the feature signal matrices. To enable a numerical observation and analysis of this reduction, we developed a binarization equation to calculate the information entropy of feature signals.

