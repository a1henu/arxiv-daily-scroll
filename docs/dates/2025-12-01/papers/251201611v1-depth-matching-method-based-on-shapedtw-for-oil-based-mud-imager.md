---
layout: default
title: Depth Matching Method Based on ShapeDTW for Oil-Based Mud Imager
---

# Depth Matching Method Based on ShapeDTW for Oil-Based Mud Imager
**arXiv**：[2512.01611v1](https://arxiv.org/abs/2512.01611) · [PDF](https://arxiv.org/pdf/2512.01611.pdf)  
**作者**：Fengfeng Li, Zhou Feng, Hongliang Wu, Hao Zhang, Han Tian, Peng Liu, Lixin Yuan  

**一句话要点**：提出基于ShapeDTW的深度匹配方法以解决油基泥浆成像仪图像深度错位问题

**关键词**：深度匹配, ShapeDTW算法, 油基泥浆成像仪, HOG1D特征, 井眼图像处理

## 3 点简述
- 油基泥浆成像仪上下垫片图像在速度校正后仍存在深度错位问题
- 方法使用HOG1D和原始信号组合特征提取局部形状特征，构建形态敏感距离矩阵
- 现场测试显示方法能精确对齐复杂纹理、深度偏移或局部缩放图像

## 摘要（原文）

> In well logging operations using the oil-based mud (OBM) microresistivity imager, which employs an interleaved design with upper and lower pad sets, depth misalignment issues persist between the pad images even after velocity correction. This paper presents a depth matching method for borehole images based on the Shape Dynamic Time Warping (ShapeDTW) algorithm. The method extracts local shape features to construct a morphologically sensitive distance matrix, better preserving structural similarity between sequences during alignment. We implement this by employing a combined feature set of the one-dimensional Histogram of Oriented Gradients (HOG1D) and the original signal as the shape descriptor. Field test examples demonstrate that our method achieves precise alignment for images with complex textures, depth shifts, or local scaling. Furthermore, it provides a flexible framework for feature extension, allowing the integration of other descriptors tailored to specific geological features.

