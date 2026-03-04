---
layout: default
title: Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis
---

# Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis
**arXiv**：[2603.02866v1](https://arxiv.org/abs/2603.02866) · [PDF](https://arxiv.org/pdf/2603.02866.pdf)  
**作者**：Kaiqiang Xiong, Zhanke Wang, Ronggang Wang  

**一句话要点**：提出多模态先验引导的重要性采样，用于稀疏视角新视图合成中的分层3D高斯泼溅

**关键词**：稀疏视角新视图合成, 3D高斯泼溅, 多模态先验, 重要性采样, 分层表示, 几何感知采样

## 3 点简述
- 核心问题：稀疏视角下新视图合成易受纹理过拟合和噪声影响，导致细节恢复不准确。
- 方法要点：融合光度渲染残差、语义先验和几何先验，指导精细高斯注入，实现从粗到细的分层表示。
- 实验或效果：在多个稀疏视角基准测试中达到最先进重建效果，DTU数据集PSNR提升最高0.3 dB。

## 摘要（原文）

> We present multimodal-prior-guided importance sampling as the central mechanism for hierarchical 3D Gaussian Splatting (3DGS) in sparse-view novel view synthesis. Our sampler fuses complementary cues { -- } photometric rendering residuals, semantic priors, and geometric priors { -- } to produce a robust, local recoverability estimate that directly drives where to inject fine Gaussians. Built around this sampling core, our framework comprises (1) a coarse-to-fine Gaussian representation that encodes global shape with a stable coarse layer and selectively adds fine primitives where the multimodal metric indicates recoverable detail; and (2) a geometric-aware sampling and retention policy that concentrates refinement on geometrically critical and complex regions while protecting newly added primitives in underconstrained areas from premature pruning. By prioritizing regions supported by consistent multimodal evidence rather than raw residuals alone, our method alleviates overfitting texture-induced errors and suppresses noise from pose/appearance inconsistencies. Experiments on diverse sparse-view benchmarks demonstrate state-of-the-art reconstructions, with up to +0.3 dB PSNR on DTU.

