---
layout: default
title: InSPECT: Invariant Spectral Features Preservation of Diffusion Models
---

# InSPECT: Invariant Spectral Features Preservation of Diffusion Models
**arXiv**：[2512.17873v1](https://arxiv.org/abs/2512.17873) · [PDF](https://arxiv.org/pdf/2512.17873.pdf)  
**作者**：Baohua Yan, Qingyuan Liu, Jennifer Kava, Xuan Di  

**一句话要点**：提出InSPECT扩散模型，通过保持不变谱特征以提升生成质量与效率。

**关键词**：扩散模型, 谱特征保持, 图像生成, 计算效率, 不变特征

## 3 点简述
- 核心问题：传统扩散模型将数据扩散至白噪声导致预测任务困难且计算量大。
- 方法要点：在前后向过程中保持不变谱特征，傅里叶系数平滑收敛至指定噪声。
- 实验或效果：在CIFAR-10等数据集上，FID降低39.23%，IS提升45.80%，收敛更快。

## 摘要（原文）

> Modern diffusion models (DMs) have achieved state-of-the-art image generation. However, the fundamental design choice of diffusing data all the way to white noise and then reconstructing it leads to an extremely difficult and computationally intractable prediction task. To overcome this limitation, we propose InSPECT (Invariant Spectral Feature-Preserving Diffusion Model), a novel diffusion model that keeps invariant spectral features during both the forward and backward processes. At the end of the forward process, the Fourier coefficients smoothly converge to a specified random noise, enabling features preservation while maintaining diversity and randomness. By preserving invariant features, InSPECT demonstrates enhanced visual diversity, faster convergence rate, and a smoother diffusion process. Experiments on CIFAR-10, Celeb-A, and LSUN demonstrate that InSPECT achieves on average a 39.23% reduction in FID and 45.80% improvement in IS against DDPM for 10K iterations under specified parameter settings, which demonstrates the significant advantages of preserving invariant features: achieving superior generation quality and diversity, while enhancing computational efficiency and enabling faster convergence rate. To the best of our knowledge, this is the first attempt to analyze and preserve invariant spectral features in diffusion models.

