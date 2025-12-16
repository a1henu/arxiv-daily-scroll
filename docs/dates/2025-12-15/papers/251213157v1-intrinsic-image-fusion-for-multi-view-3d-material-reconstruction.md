---
layout: default
title: Intrinsic Image Fusion for Multi-View 3D Material Reconstruction
---

# Intrinsic Image Fusion for Multi-View 3D Material Reconstruction
**arXiv**：[2512.13157v1](https://arxiv.org/abs/2512.13157) · [PDF](https://arxiv.org/pdf/2512.13157.pdf)  
**作者**：Peter Kocsis, Lukas Höllein, Matthias Nießner  

**一句话要点**：提出内在图像融合方法，从多视角图像重建高质量物理材质

**关键词**：多视角材质重建, 内在图像分解, 扩散模型, 参数优化, 路径追踪, 材质解缠

## 3 点简述
- 核心问题：多视角材质重建高度欠约束，依赖昂贵且噪声的路径追踪分析合成方法
- 方法要点：融合单视角先验，通过扩散模型生成候选分解，并优化低维参数函数以减少不一致性
- 实验或效果：在合成和真实场景中优于现有方法，实现清晰材质解缠，适合高质量重光照

## 摘要（原文）

> We introduce Intrinsic Image Fusion, a method that reconstructs high-quality physically based materials from multi-view images. Material reconstruction is highly underconstrained and typically relies on analysis-by-synthesis, which requires expensive and noisy path tracing. To better constrain the optimization, we incorporate single-view priors into the reconstruction process. We leverage a diffusion-based material estimator that produces multiple, but often inconsistent, candidate decompositions per view. To reduce the inconsistency, we fit an explicit low-dimensional parametric function to the predictions. We then propose a robust optimization framework using soft per-view prediction selection together with confidence-based soft multi-view inlier set to fuse the most consistent predictions of the most confident views into a consistent parametric material space. Finally, we use inverse path tracing to optimize for the low-dimensional parameters. Our results outperform state-of-the-art methods in material disentanglement on both synthetic and real scenes, producing sharp and clean reconstructions suitable for high-quality relighting.

