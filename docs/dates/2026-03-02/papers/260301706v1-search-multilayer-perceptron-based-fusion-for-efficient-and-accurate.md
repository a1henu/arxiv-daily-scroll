---
layout: default
title: Search Multilayer Perceptron-Based Fusion for Efficient and Accurate Siamese Tracking
---

# Search Multilayer Perceptron-Based Fusion for Efficient and Accurate Siamese Tracking
**arXiv**：[2603.01706v1](https://arxiv.org/abs/2603.01706) · [PDF](https://arxiv.org/pdf/2603.01706.pdf)  
**作者**：Tianqi Shen, Huakao Lin, Ning An  

**一句话要点**：提出基于多层感知机的融合模块与可微分神经架构搜索，以解决孪生跟踪中精度与效率的失衡问题。

**关键词**：孪生跟踪, 多层感知机融合, 可微分神经架构搜索, 精度-效率平衡, 实时跟踪

## 3 点简述
- 核心问题：卷积或Transformer融合在资源受限硬件上难以高效实现像素级交互，导致精度与效率失衡。
- 方法要点：设计MLP-based融合模块实现像素级交互，并通过定制化松弛策略的DNAS优化通道宽度与深度。
- 实验或效果：在多个跟踪基准上达到先进精度-效率平衡，并在GPU和NPU上保持实时性能。

## 摘要（原文）

> Siamese visual trackers have recently advanced through increasingly sophisticated fusion mechanisms built on convolutional or Transformer architectures. However, both struggle to deliver pixel-level interactions efficiently on resource-constrained hardware, leading to a persistent accuracy-efficiency imbalance. Motivated by this limitation, we redesign the Siamese neck with a simple yet effective Multilayer Perception (MLP)-based fusion module that enables pixel-level interaction with minimal structural overhead. Nevertheless, naively stacking MLP blocks introduces a new challenge: computational cost can scale quadratically with channel width. To overcome this, we construct a hierarchical search space of carefully designed MLP modules and introduce a customized relaxation strategy that enables differentiable neural architecture search (DNAS) to decouple channel-width optimization from other architectural choices. This targeted decoupling automatically balances channel width and depth, yielding a low-complexity architecture. The resulting tracker achieves state-of-the-art accuracy-efficiency trade-offs. It ranks among the top performers on four general-purpose and three aerial tracking benchmarks, while maintaining real-time performance on both resource-constrained Graphics Processing Units (GPUs) and Neural Processing Units (NPUs).

