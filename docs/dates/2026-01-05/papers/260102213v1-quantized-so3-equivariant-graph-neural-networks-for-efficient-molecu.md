---
layout: default
title: Quantized SO(3)-Equivariant Graph Neural Networks for Efficient Molecular Property Prediction
---

# Quantized SO(3)-Equivariant Graph Neural Networks for Efficient Molecular Property Prediction
**arXiv**：[2601.02213v1](https://arxiv.org/abs/2601.02213) · [PDF](https://arxiv.org/pdf/2601.02213.pdf)  
**作者**：Haoyu Zhou, Ping Xue, Tianfan Fu, Hao Zhang  

**一句话要点**：提出量化SO(3)-等变图神经网络，以高效部署于分子性质预测场景。

**关键词**：等变图神经网络, 低比特量化, 分子性质预测, 注意力机制, 计算效率优化

## 3 点简述
- 核心问题：SO(3)-等变GNN计算成本高，难以在边缘设备部署。
- 方法要点：采用低比特量化，包括幅度-方向解耦量化、分支分离量化感知训练和注意力归一化。
- 实验或效果：在QM9和rMD17基准上，8位模型保持精度和等变性，推理加速2.37–2.73倍，模型大小减小4倍。

## 摘要（原文）

> Deploying 3D graph neural networks (GNNs) that are equivariant to 3D rotations (the group SO(3)) on edge devices is challenging due to their high computational cost. This paper addresses the problem by compressing and accelerating an SO(3)-equivariant GNN using low-bit quantization techniques. Specifically, we introduce three innovations for quantized equivariant transformers: (1) a magnitude-direction decoupled quantization scheme that separately quantizes the norm and orientation of equivariant (vector) features, (2) a branch-separated quantization-aware training strategy that treats invariant and equivariant feature channels differently in an attention-based $SO(3)$-GNN, and (3) a robustness-enhancing attention normalization mechanism that stabilizes low-precision attention computations. Experiments on the QM9 and rMD17 molecular benchmarks demonstrate that our 8-bit models achieve accuracy on energy and force predictions comparable to full-precision baselines with markedly improved efficiency. We also conduct ablation studies to quantify the contribution of each component to maintain accuracy and equivariance under quantization, using the Local error of equivariance (LEE) metric. The proposed techniques enable the deployment of symmetry-aware GNNs in practical chemistry applications with 2.37--2.73x faster inference and 4x smaller model size, without sacrificing accuracy or physical symmetry.

