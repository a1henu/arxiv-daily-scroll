---
layout: default
title: Laplacian Multi-scale Flow Matching for Generative Modeling
---

# Laplacian Multi-scale Flow Matching for Generative Modeling
**arXiv**：[2602.19461v1](https://arxiv.org/abs/2602.19461) · [PDF](https://arxiv.org/pdf/2602.19461.pdf)  
**作者**：Zelin Zhao, Petr Molodyk, Haotian Xue, Yongxin Chen  

**一句话要点**：提出Laplacian多尺度流匹配框架，通过并行处理提升图像生成质量与效率。

**关键词**：图像生成, 流匹配, 多尺度表示, 拉普拉斯金字塔, 混合变换器, 因果注意力

## 3 点简述
- 核心问题：传统流匹配方法在图像生成中面临多尺度处理效率低和需要显式桥接过程的问题。
- 方法要点：利用拉普拉斯金字塔残差分解图像，通过因果注意力机制的混合变换器架构并行处理多尺度表示。
- 实验或效果：在CelebA-HQ和ImageNet上实现更优样本质量，减少GFLOPs并加速推理，可扩展至1024×1024分辨率。

## 摘要（原文）

> In this paper, we present Laplacian multiscale flow matching (LapFlow), a novel framework that enhances flow matching by leveraging multi-scale representations for image generative modeling. Our approach decomposes images into Laplacian pyramid residuals and processes different scales in parallel through a mixture-of-transformers (MoT) architecture with causal attention mechanisms. Unlike previous cascaded approaches that require explicit renoising between scales, our model generates multi-scale representations in parallel, eliminating the need for bridging processes. The proposed multi-scale architecture not only improves generation quality but also accelerates the sampling process and promotes scaling flow matching methods. Through extensive experimentation on CelebA-HQ and ImageNet, we demonstrate that our method achieves superior sample quality with fewer GFLOPs and faster inference compared to single-scale and multi-scale flow matching baselines. The proposed model scales effectively to high-resolution generation (up to 1024$\times$1024) while maintaining lower computational overhead.

