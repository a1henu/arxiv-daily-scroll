---
layout: default
title: Gaussian Belief Propagation Network for Depth Completion
---

# Gaussian Belief Propagation Network for Depth Completion
**arXiv**：[2601.21291v1](https://arxiv.org/abs/2601.21291) · [PDF](https://arxiv.org/pdf/2601.21291.pdf)  
**作者**：Jie Tang, Pingping Xie, Jian Li, Ping Tan  

**一句话要点**：提出高斯置信传播网络，结合深度学习与概率图模型解决稀疏深度补全问题。

**关键词**：深度补全, 高斯置信传播, 马尔可夫随机场, 稀疏深度处理, 非局部边缘预测, 混合框架

## 3 点简述
- 核心问题：深度补全中稀疏不规则深度数据在深度网络中处理困难，限制性能。
- 方法要点：动态构建场景特定马尔可夫随机场，通过高斯置信传播推断密集深度分布。
- 实验或效果：在NYUv2和KITTI基准上达到SOTA，展现强鲁棒性和泛化能力。

## 摘要（原文）

> Depth completion aims to predict a dense depth map from a color image with sparse depth measurements. Although deep learning methods have achieved state-of-the-art (SOTA), effectively handling the sparse and irregular nature of input depth data in deep networks remains a significant challenge, often limiting performance, especially under high sparsity. To overcome this limitation, we introduce the Gaussian Belief Propagation Network (GBPN), a novel hybrid framework synergistically integrating deep learning with probabilistic graphical models for end-to-end depth completion. Specifically, a scene-specific Markov Random Field (MRF) is dynamically constructed by the Graphical Model Construction Network (GMCN), and then inferred via Gaussian Belief Propagation (GBP) to yield the dense depth distribution. Crucially, the GMCN learns to construct not only the data-dependent potentials of MRF but also its structure by predicting adaptive non-local edges, enabling the capture of complex, long-range spatial dependencies. Furthermore, we enhance GBP with a serial \& parallel message passing scheme, designed for effective information propagation, particularly from sparse measurements. Extensive experiments demonstrate that GBPN achieves SOTA performance on the NYUv2 and KITTI benchmarks. Evaluations across varying sparsity levels, sparsity patterns, and datasets highlight GBPN's superior performance, notable robustness, and generalizable capability.

