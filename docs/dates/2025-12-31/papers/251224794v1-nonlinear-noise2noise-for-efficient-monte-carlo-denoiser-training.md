---
layout: default
title: Nonlinear Noise2Noise for Efficient Monte Carlo Denoiser Training
---

# Nonlinear Noise2Noise for Efficient Monte Carlo Denoiser Training
**arXiv**：[2512.24794v1](https://arxiv.org/abs/2512.24794) · [PDF](https://arxiv.org/pdf/2512.24794.pdf)  
**作者**：Andrew Tinits, Stephen Mann  

**一句话要点**：提出非线性Noise2Noise方法以高效训练蒙特卡罗去噪器

**关键词**：蒙特卡罗去噪, Noise2Noise训练, 非线性函数分析, 高动态范围图像, 机器学习去噪

## 3 点简述
- 核心问题：Noise2Noise训练中非线性函数导致目标图像期望值偏差，限制预处理应用。
- 方法要点：理论分析非线性函数影响，识别偏差最小的一类非线性函数，结合损失函数与色调映射减少异常值影响。
- 实验或效果：应用于HDR图像去噪，仅用噪声训练数据接近原高样本参考图像训练效果。

## 摘要（原文）

> The Noise2Noise method allows for training machine learning-based denoisers with pairs of input and target images where both the input and target can be noisy. This removes the need for training with clean target images, which can be difficult to obtain. However, Noise2Noise training has a major limitation: nonlinear functions applied to the noisy targets will skew the results. This bias occurs because the nonlinearity makes the expected value of the noisy targets different from the clean target image. Since nonlinear functions are common in image processing, avoiding them limits the types of preprocessing that can be performed on the noisy targets. Our main insight is that certain nonlinear functions can be applied to the noisy targets without adding significant bias to the results. We develop a theoretical framework for analyzing the effects of these nonlinearities, and describe a class of nonlinear functions with minimal bias.
>   We demonstrate our method on the denoising of high dynamic range (HDR) images produced by Monte Carlo rendering. Noise2Noise training can have trouble with HDR images, where the training process is overwhelmed by outliers and performs poorly. We consider a commonly used method of addressing these training issues: applying a nonlinear tone mapping function to the model output and target images to reduce their dynamic range. This method was previously thought to be incompatible with Noise2Noise training because of the nonlinearities involved. We show that certain combinations of loss functions and tone mapping functions can reduce the effect of outliers while introducing minimal bias. We apply our method to an existing machine learning-based Monte Carlo denoiser, where the original implementation was trained with high-sample count reference images. Our results approach those of the original implementation, but are produced using only noisy training data.

