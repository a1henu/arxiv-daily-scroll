---
layout: default
title: GaMO: Geometry-aware Multi-view Diffusion Outpainting for Sparse-View 3D Reconstruction
---

# GaMO: Geometry-aware Multi-view Diffusion Outpainting for Sparse-View 3D Reconstruction
**arXiv**：[2512.25073v1](https://arxiv.org/abs/2512.25073) · [PDF](https://arxiv.org/pdf/2512.25073.pdf)  
**作者**：Yi-Chuan Huang, Hao-Jen Chien, Chin-Yang Lin, Ying-Huan Chen, Yu-Lun Liu  

**一句话要点**：提出GaMO框架，通过多视角外绘解决稀疏视角3D重建中的几何不一致与覆盖不足问题。

**关键词**：稀疏视角3D重建, 多视角外绘, 几何一致性, 零样本扩散模型, 计算效率优化

## 3 点简述
- 核心问题：现有方法在稀疏视角下存在覆盖不足、几何不一致和计算成本高的问题。
- 方法要点：采用多视角外绘扩展已知视角的视野，无需训练，保持几何一致性。
- 实验或效果：在Replica和ScanNet++上优于先前方法，速度提升25倍，处理时间低于10分钟。

## 摘要（原文）

> Recent advances in 3D reconstruction have achieved remarkable progress in high-quality scene capture from dense multi-view imagery, yet struggle when input views are limited. Various approaches, including regularization techniques, semantic priors, and geometric constraints, have been implemented to address this challenge. Latest diffusion-based methods have demonstrated substantial improvements by generating novel views from new camera poses to augment training data, surpassing earlier regularization and prior-based techniques. Despite this progress, we identify three critical limitations in these state-of-the-art approaches: inadequate coverage beyond known view peripheries, geometric inconsistencies across generated views, and computationally expensive pipelines. We introduce GaMO (Geometry-aware Multi-view Outpainter), a framework that reformulates sparse-view reconstruction through multi-view outpainting. Instead of generating new viewpoints, GaMO expands the field of view from existing camera poses, which inherently preserves geometric consistency while providing broader scene coverage. Our approach employs multi-view conditioning and geometry-aware denoising strategies in a zero-shot manner without training. Extensive experiments on Replica and ScanNet++ demonstrate state-of-the-art reconstruction quality across 3, 6, and 9 input views, outperforming prior methods in PSNR and LPIPS, while achieving a $25\times$ speedup over SOTA diffusion-based methods with processing time under 10 minutes. Project page: https://yichuanh.github.io/GaMO/

