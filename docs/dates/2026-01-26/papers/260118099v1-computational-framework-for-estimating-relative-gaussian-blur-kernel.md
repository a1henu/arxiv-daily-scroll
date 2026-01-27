---
layout: default
title: Computational Framework for Estimating Relative Gaussian Blur Kernels between Image Pairs
---

# Computational Framework for Estimating Relative Gaussian Blur Kernels between Image Pairs
**arXiv**：[2601.18099v1](https://arxiv.org/abs/2601.18099) · [PDF](https://arxiv.org/pdf/2601.18099.pdf)  
**作者**：Akbar Saadat  

**一句话要点**：提出零训练前向计算框架，用于实时估计图像对间相对高斯模糊核

**关键词**：高斯模糊估计, 零训练框架, 实时图像处理, 部分模糊图像, 解析表达式计算, 相似度筛选

## 3 点简述
- 核心问题：估计图像对间相对高斯模糊核，适用于部分模糊场景，无需训练数据。
- 方法要点：基于离散计算解析表达式，通过相似度筛选多解，实现实时处理。
- 实验效果：在真实图像上，估计合成模糊值的平均绝对误差低于1.7%，强度差异小于2%。

## 摘要（原文）

> Following the earlier verification for Gaussian model in \cite{ASaa2026}, this paper introduces a zero training forward computational framework for the model to realize it in real time applications. The framework is based on discrete calculation of the analytic expression of the defocused image from the sharper one for the application range of the standard deviation of the Gaussian kernels and selecting the best matches. The analytic expression yields multiple solutions at certain image points, but is filtered down to a single solution using similarity measures over neighboring points.The framework is structured to handle cases where two given images are partial blurred versions of each other. Experimental evaluations on real images demonstrate that the proposed framework achieves a mean absolute error (MAE) below $1.7\%$ in estimating synthetic blur values. Furthermore, the discrepancy between actual blurred image intensities and their corresponding estimates remains under $2\%$, obtained by applying the extracted defocus filters to less blurred images.

