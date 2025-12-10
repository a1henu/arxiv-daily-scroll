---
layout: default
title: An Iteration-Free Fixed-Point Estimator for Diffusion Inversion
---

# An Iteration-Free Fixed-Point Estimator for Diffusion Inversion
**arXiv**：[2512.08547v1](https://arxiv.org/abs/2512.08547) · [PDF](https://arxiv.org/pdf/2512.08547.pdf)  
**作者**：Yifei Chen, Kaiyu Song, Yan Pan, Jianxing Yu, Jian Yin, Hanjiang Lai  

**一句话要点**：提出迭代无关的定点估计器以解决扩散反演中的计算成本高和超参数选择复杂问题。

**关键词**：扩散反演, 定点估计, 误差近似, 图像重建, 计算效率, 无偏估计

## 3 点简述
- 扩散反演旨在通过最小化每一步误差来恢复初始噪声，但现有定点迭代方法计算成本高且超参数选择复杂。
- 方法推导理想反演步的定点显式表达式，并引入误差近似来估计未知误差，形成低方差无偏估计器。
- 在NOCAPS和MS-COCO数据集上评估，相比DDIM反演和其他定点迭代方法，重建性能一致更优，无需额外迭代或训练。

## 摘要（原文）

> Diffusion inversion aims to recover the initial noise corresponding to a given image such that this noise can reconstruct the original image through the denoising diffusion process. The key component of diffusion inversion is to minimize errors at each inversion step, thereby mitigating cumulative inaccuracies. Recently, fixed-point iteration has emerged as a widely adopted approach to minimize reconstruction errors at each inversion step. However, it suffers from high computational costs due to its iterative nature and the complexity of hyperparameter selection. To address these issues, we propose an iteration-free fixed-point estimator for diffusion inversion. First, we derive an explicit expression of the fixed point from an ideal inversion step. Unfortunately, it inherently contains an unknown data prediction error. Building upon this, we introduce the error approximation, which uses the calculable error from the previous inversion step to approximate the unknown error at the current inversion step. This yields a calculable, approximate expression for the fixed point, which is an unbiased estimator characterized by low variance, as shown by our theoretical analysis. We evaluate reconstruction performance on two text-image datasets, NOCAPS and MS-COCO. Compared to DDIM inversion and other inversion methods based on the fixed-point iteration, our method achieves consistent and superior performance in reconstruction tasks without additional iterations or training.

