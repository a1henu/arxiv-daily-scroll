---
layout: default
title: Preserving Continuous Symmetry in Discrete Spaces: Geometric-Aware Quantization for SO(3)-Equivariant GNNs
---

# Preserving Continuous Symmetry in Discrete Spaces: Geometric-Aware Quantization for SO(3)-Equivariant GNNs
**arXiv**：[2603.05343v1](https://arxiv.org/abs/2603.05343) · [PDF](https://arxiv.org/pdf/2603.05343.pdf)  
**作者**：Haoyu Zhou, Ping Xue, Hao Zhang, Tianfan Fu  

**一句话要点**：提出几何感知量化框架以在离散空间中保持SO(3)等变性GNN的连续对称性

**关键词**：等变图神经网络, 几何感知量化, SO(3)对称性, 分子模拟, 低比特量化, 计算加速

## 3 点简述
- 核心问题：低比特量化破坏SO(3)等变性结构，导致误差和守恒律违反
- 方法要点：采用幅度-方向解耦量化、对称感知训练策略和鲁棒注意力归一化
- 实验或效果：在rMD17基准上，W4A8模型匹配FP32精度，推理加速2.39倍，内存减少4倍

## 摘要（原文）

> Equivariant Graph Neural Networks (GNNs) are essential for physically consistent molecular simulations but suffer from high computational costs and memory bottlenecks, especially with high-order representations. While low-bit quantization offers a solution, applying it naively to rotation-sensitive features destroys the SO(3)-equivariant structure, leading to significant errors and violations of conservation laws. To address this issue, in this work, we propose a Geometric-Aware Quantization (GAQ) framework that compresses and accelerates equivariant models while rigorously preserving continuous symmetry in discrete spaces. Our approach introduces three key contributions: (1) a Magnitude-Direction Decoupled Quantization (MDDQ) scheme that separates invariant lengths from equivariant orientations to maintain geometric fidelity; (2) a symmetry-aware training strategy that treats scalar and vector features with distinct quantization schedules; and (3) a robust attention normalization mechanism to stabilize gradients in low-bit regimes. Experiments on the rMD17 benchmark demonstrate that our W4A8 models match the accuracy of FP32 baselines (9.31 meV vs. 23.20 meV) while reducing Local Equivariance Error (LEE) by over 30x compared to naive quantization. On consumer hardware, GAQ achieves 2.39x inference speedup and 4x memory reduction, enabling stable, energy-conserving molecular dynamics simulations for nanosecond timescales.

