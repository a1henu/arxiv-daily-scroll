---
layout: default
title: Gaussian Belief Propagation Network for Depth Completion
---

# Gaussian Belief Propagation Network for Depth Completion
**arXiv**：[2601.21291v1](https://arxiv.org/abs/2601.21291) · [PDF](https://arxiv.org/pdf/2601.21291.pdf)  
**作者**：Jie Tang, Pingping Xie, Jian Li, Ping Tan  

**一句话要点**：提出高斯置信传播网络，结合深度学习与概率图模型解决深度补全中稀疏数据挑战。

**关键词**：深度补全, 高斯置信传播, 概率图模型, 稀疏数据处理, 自适应图结构, 端到端学习

## 3 点简述
- 深度补全任务中，稀疏不规则深度数据在深度网络中处理困难，限制性能，尤其在高度稀疏时。
- GBPN通过图模型构建网络动态构建场景特定马尔可夫随机场，并利用高斯置信传播进行推断，学习自适应非局部边以捕获长程空间依赖。
- 在NYUv2和KITTI基准测试中达到SOTA，在不同稀疏度、模式和数据集上表现出优越性能、鲁棒性和泛化能力。

## 摘要（原文）

> Depth completion aims to predict a dense depth map from a color image with sparse depth measurements. Although deep learning methods have achieved state-of-the-art (SOTA), effectively handling the sparse and irregular nature of input depth data in deep networks remains a significant challenge, often limiting performance, especially under high sparsity. To overcome this limitation, we introduce the Gaussian Belief Propagation Network (GBPN), a novel hybrid framework synergistically integrating deep learning with probabilistic graphical models for end-to-end depth completion. Specifically, a scene-specific Markov Random Field (MRF) is dynamically constructed by the Graphical Model Construction Network (GMCN), and then inferred via Gaussian Belief Propagation (GBP) to yield the dense depth distribution. Crucially, the GMCN learns to construct not only the data-dependent potentials of MRF but also its structure by predicting adaptive non-local edges, enabling the capture of complex, long-range spatial dependencies. Furthermore, we enhance GBP with a serial \& parallel message passing scheme, designed for effective information propagation, particularly from sparse measurements. Extensive experiments demonstrate that GBPN achieves SOTA performance on the NYUv2 and KITTI benchmarks. Evaluations across varying sparsity levels, sparsity patterns, and datasets highlight GBPN's superior performance, notable robustness, and generalizable capability.

