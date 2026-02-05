---
layout: default
title: MirrorLA: Reflecting Feature Map for Vision Linear Attention
---

# MirrorLA: Reflecting Feature Map for Vision Linear Attention
**arXiv**：[2602.04346v1](https://arxiv.org/abs/2602.04346) · [PDF](https://arxiv.org/pdf/2602.04346.pdf)  
**作者**：Weikang Meng, Liangyu Huo, Yadan Luo, Yaowei Wang, Yingjian Li, Zheng Zhang  

**一句话要点**：提出MirrorLA框架，通过可学习反射优化线性注意力特征图，提升视觉任务性能。

**关键词**：线性注意力, 特征图优化, Householder反射, 视觉Transformer, 计算效率, 表示学习

## 3 点简述
- 核心问题：线性注意力因非负约束导致特征信息丢失，性能落后于softmax注意力。
- 方法要点：使用Householder反射主动重定向特征几何，保留负域语义信息，结合多尺度设计优化表示密度。
- 实验或效果：在标准基准测试中达到最优性能，实现线性效率且不牺牲表示保真度。

## 摘要（原文）

> Linear attention significantly reduces the computational complexity of Transformers from quadratic to linear, yet it consistently lags behind softmax-based attention in performance. We identify the root cause of this degradation as the non-negativity constraint imposed on kernel feature maps: standard projections like ReLU act as "passive truncation" operators, indiscriminately discarding semantic information residing in the negative domain. We propose MirrorLA, a geometric framework that substitutes passive truncation with active reorientation. By leveraging learnable Householder reflections, MirrorLA rotates the feature geometry into the non-negative orthant to maximize information retention. Our approach restores representational density through a cohesive, multi-scale design: it first optimizes local discriminability via block-wise isometries, stabilizes long-context dynamics using variance-aware modulation to diversify activations, and finally, integrates dispersed subspaces via cross-head reflections to induce global covariance mixing. MirrorLA achieves state-of-the-art performance across standard benchmarks, demonstrating that strictly linear efficiency can be achieved without compromising representational fidelity.

