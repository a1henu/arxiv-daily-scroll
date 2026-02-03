---
layout: default
title: Learning Sparse Visual Representations via Spatial-Semantic Factorization
---

# Learning Sparse Visual Representations via Spatial-Semantic Factorization
**arXiv**：[2602.01905v1](https://arxiv.org/abs/2602.01905) · [PDF](https://arxiv.org/pdf/2602.01905.pdf)  
**作者**：Theodore Zhengde Zhao, Sid Kiblawi, Jianwei Yang, Naoto Usuyama, Reuben Tan, Noel C Codella, Tristan Naumann, Hoifung Poon, Mu Wei  

**一句话要点**：提出STELLAR框架，通过空间-语义分解解决自监督学习中语义理解与图像重建的冲突。

**关键词**：自监督学习, 空间-语义分解, 稀疏表示, 图像重建, 语义理解, 视觉表示学习

## 3 点简述
- 自监督学习中，语义理解与图像重建存在冲突：全局语义方法丢弃空间信息，生成方法缺乏高层抽象。
- STELLAR将视觉特征分解为语义概念及其空间分布的乘积，实现语义与空间解耦，支持增强对齐和像素级重建。
- 实验表明，仅用16个稀疏令牌即可实现高质量重建（2.60 FID）和接近密集骨干的语义性能（79.10% ImageNet准确率）。

## 摘要（原文）

> Self-supervised learning (SSL) faces a fundamental conflict between semantic understanding and image reconstruction. High-level semantic SSL (e.g., DINO) relies on global tokens that are forced to be location-invariant for augmentation alignment, a process that inherently discards the spatial coordinates required for reconstruction. Conversely, generative SSL (e.g., MAE) preserves dense feature grids for reconstruction but fails to produce high-level abstractions. We introduce STELLAR, a framework that resolves this tension by factorizing visual features into a low-rank product of semantic concepts and their spatial distributions. This disentanglement allows us to perform DINO-style augmentation alignment on the semantic tokens while maintaining the precise spatial mapping in the localization matrix necessary for pixel-level reconstruction. We demonstrate that as few as 16 sparse tokens under this factorized form are sufficient to simultaneously support high-quality reconstruction (2.60 FID) and match the semantic performance of dense backbones (79.10% ImageNet accuracy). Our results highlight STELLAR as a versatile sparse representation that bridges the gap between discriminative and generative vision by strategically separating semantic identity from spatial geometry. Code available at https://aka.ms/stellar.

