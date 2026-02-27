---
layout: default
title: GIFSplat: Generative Prior-Guided Iterative Feed-Forward 3D Gaussian Splatting from Sparse Views
---

# GIFSplat: Generative Prior-Guided Iterative Feed-Forward 3D Gaussian Splatting from Sparse Views
**arXiv**：[2602.22571v1](https://arxiv.org/abs/2602.22571) · [PDF](https://arxiv.org/pdf/2602.22571.pdf)  
**作者**：Tianyu Chen, Wei Xiang, Kang Han, Yu Lu, Di Wu, Gaowen Liu, Ramana Rao Kompella  

**一句话要点**：提出GIFSplat，一种基于生成先验的迭代前馈3D高斯溅射框架，用于稀疏视图重建。

**关键词**：3D高斯溅射, 稀疏视图重建, 前馈网络, 迭代优化, 生成先验蒸馏, 无梯度适应

## 3 点简述
- 核心问题：现有前馈方法在稀疏视图下性能受限，难以平衡生成先验引入与推理效率。
- 方法要点：采用迭代残差更新逐步优化3D场景，并通过蒸馏扩散先验实现无梯度适应。
- 实验或效果：在多个数据集上优于基线，PSNR提升达+2.1 dB，保持秒级推理时间。

## 摘要（原文）

> Feed-forward 3D reconstruction offers substantial runtime advantages over per-scene optimization, which remains slow at inference and often fragile under sparse views. However, existing feed-forward methods still have potential for further performance gains, especially for out-of-domain data, and struggle to retain second-level inference time once a generative prior is introduced. These limitations stem from the one-shot prediction paradigm in existing feed-forward pipeline: models are strictly bounded by capacity, lack inference-time refinement, and are ill-suited for continuously injecting generative priors. We introduce GIFSplat, a purely feed-forward iterative refinement framework for 3D Gaussian Splatting from sparse unposed views. A small number of forward-only residual updates progressively refine current 3D scene using rendering evidence, achieve favorable balance between efficiency and quality. Furthermore, we distill a frozen diffusion prior into Gaussian-level cues from enhanced novel renderings without gradient backpropagation or ever-increasing view-set expansion, thereby enabling per-scene adaptation with generative prior while preserving feed-forward efficiency. Across DL3DV, RealEstate10K, and DTU, GIFSplat consistently outperforms state-of-the-art feed-forward baselines, improving PSNR by up to +2.1 dB, and it maintains second-scale inference time without requiring camera poses or any test-time gradient optimization.

