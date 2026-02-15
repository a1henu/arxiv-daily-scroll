---
layout: default
title: U-DAVI: Uncertainty-Aware Diffusion-Prior-Based Amortized Variational Inference for Image Reconstruction
---

# U-DAVI: Uncertainty-Aware Diffusion-Prior-Based Amortized Variational Inference for Image Reconstruction
**arXiv**：[2602.11704v1](https://arxiv.org/abs/2602.11704) · [PDF](https://arxiv.org/pdf/2602.11704.pdf)  
**作者**：Ayush Varshney, Katherine L. Bouman, Berthy T. Feng  

**一句话要点**：提出不确定性感知扩散先验的摊销变分推断方法，用于图像重建以提升细节和效率。

**关键词**：图像重建, 扩散先验, 摊销变分推断, 不确定性估计, 逆问题

## 3 点简述
- 核心问题：图像逆问题中，现有摊销变分推断方法难以重建精细细节和复杂纹理。
- 方法要点：在训练中基于不确定性估计注入空间自适应扰动，强调最不确定区域的学习。
- 实验或效果：在去模糊和超分辨率任务中，性能优于或媲美先前扩散方法，无需迭代优化。

## 摘要（原文）

> Ill-posed imaging inverse problems remain challenging due to the ambiguity in mapping degraded observations to clean images. Diffusion-based generative priors have recently shown promise, but typically rely on computationally intensive iterative sampling or per-instance optimization. Amortized variational inference frameworks address this inefficiency by learning a direct mapping from measurements to posteriors, enabling fast posterior sampling without requiring the optimization of a new posterior for every new set of measurements. However, they still struggle to reconstruct fine details and complex textures. To address this, we extend the amortized framework by injecting spatially adaptive perturbations to measurements during training, guided by uncertainty estimates, to emphasize learning in the most uncertain regions. Experiments on deblurring and super-resolution demonstrate that our method achieves superior or competitive performance to previous diffusion-based approaches, delivering more realistic reconstructions without the computational cost of iterative refinement.

