---
layout: default
title: Defocus Aberration Theory Confirms Gaussian Model in Most Imaging Devices
---

# Defocus Aberration Theory Confirms Gaussian Model in Most Imaging Devices
**arXiv**：[2601.04779v1](https://arxiv.org/abs/2601.04779) · [PDF](https://arxiv.org/pdf/2601.04779.pdf)  
**作者**：Akbar Saadat  

**一句话要点**：基于离焦像差理论验证高斯模型在多数成像设备中的适用性

**关键词**：离焦深度估计, 高斯模型, 像差理论, 3D恢复, 成像设备

## 3 点简述
- 核心问题：从2D图像准确估计深度是3D恢复中的基本挑战，涉及空间变化离焦模糊的估计。
- 方法要点：利用离焦像差理论分析几何光学和衍射极限光学，验证高斯模型对离焦算子的拟合精度。
- 实验或效果：在典型聚焦深度1-100米范围内，最大平均绝对误差小于1%，确认模型准确可靠。

## 摘要（原文）

> Over the past three decades, defocus has consistently provided groundbreaking depth information in scene images. However, accurately estimating depth from 2D images continues to be a persistent and fundamental challenge in the field of 3D recovery. Heuristic approaches involve with the ill-posed problem for inferring the spatial variant defocusing blur, as the desired blur cannot be distinguished from the inherent blur. Given a prior knowledge of the defocus model, the problem become well-posed with an analytic solution for the relative blur between two images, taken at the same viewpoint with different camera settings for the focus. The Gaussian model stands out as an optimal choice for real-time applications, due to its mathematical simplicity and computational efficiency. And theoretically, it is the only model can be applied at the same time to both the absolute blur caused by depth in a single image and the relative blur resulting from depth differences between two images. This paper introduces the settings, for conventional imaging devices, to ensure that the defocusing operator adheres to the Gaussian model. Defocus analysis begins within the framework of geometric optics and is conducted by defocus aberration theory in diffraction-limited optics to obtain the accuracy of fitting the actual model to its Gaussian approximation. The results for a typical set of focused depths between $1$ and $100$ meters, with a maximum depth variation of $10\%$ at the focused depth, confirm the Gaussian model's applicability for defocus operators in most imaging devices. The findings demonstrate a maximum Mean Absolute Error $(\!M\!A\!E)$ of less than $1\%$, underscoring the model's accuracy and reliability.

