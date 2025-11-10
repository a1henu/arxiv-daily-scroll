---
layout: default
title: GroupKAN: Rethinking Nonlinearity with Grouped Spline-based KAN Modeling for Efficient Medical Image Segmentation
---

# GroupKAN: Rethinking Nonlinearity with Grouped Spline-based KAN Modeling for Efficient Medical Image Segmentation
**arXiv**：[2511.05477v1](https://arxiv.org/abs/2511.05477) · [PDF](https://arxiv.org/pdf/2511.05477.pdf)  
**作者**：Guojie Li, Anwar P. P. Abdul Majeed, Muhammad Ateeq, Anh Nguyen, Fan Zhang  

**一句话要点**：提出GroupKAN以高效解决医学图像分割中的非线性建模问题

**关键词**：医学图像分割, Kolmogorov-Arnold网络, 分组非线性建模, 轻量网络, 可解释性

## 3 点简述
- 医学图像分割需轻量、准确、可解释模型，现有方法存在复杂度高或非线性不足问题
- 引入分组KAN变换与激活，通过通道分组降低复杂度至O(C²/G)，提升效率
- 在三个医学基准测试中，平均IoU达79.80%，参数减少至47.6%，优于U-KAN

## 摘要（原文）

> Medical image segmentation requires models that are accurate, lightweight,
> and interpretable. Convolutional architectures lack adaptive nonlinearity and
> transparent decision-making, whereas Transformer architectures are hindered by
> quadratic complexity and opaque attention mechanisms. U-KAN addresses these
> challenges using Kolmogorov-Arnold Networks, achieving higher accuracy than
> both convolutional and attention-based methods, fewer parameters than
> Transformer variants, and improved interpretability compared to conventional
> approaches. However, its O(C^2) complexity due to full-channel transformations
> limits its scalability as the number of channels increases. To overcome this,
> we introduce GroupKAN, a lightweight segmentation network that incorporates two
> novel, structured functional modules: (1) Grouped KAN Transform, which
> partitions channels into G groups for multivariate spline mappings, reducing
> complexity to O(C^2/G), and (2) Grouped KAN Activation, which applies shared
> spline-based mappings within each channel group for efficient, token-wise
> nonlinearity. Evaluated on three medical benchmarks (BUSI, GlaS, and CVC),
> GroupKAN achieves an average IoU of 79.80 percent, surpassing U-KAN by +1.11
> percent while requiring only 47.6 percent of the parameters (3.02M vs 6.35M),
> and shows improved interpretability.

