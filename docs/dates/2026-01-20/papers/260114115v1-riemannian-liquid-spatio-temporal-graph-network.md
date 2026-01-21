---
layout: default
title: Riemannian Liquid Spatio-Temporal Graph Network
---

# Riemannian Liquid Spatio-Temporal Graph Network
**arXiv**：[2601.14115v1](https://arxiv.org/abs/2601.14115) · [PDF](https://arxiv.org/pdf/2601.14115.pdf)  
**作者**：Liangsi Lu, Jingchao Wang, Zhaorong Dai, Hanqian Liu, Yang Shi  

**一句话要点**：提出黎曼流形上的液态时空图网络，以解决非欧几里得图结构建模中的几何失真问题。

**关键词**：黎曼流形, 时空图网络, 连续时间建模, 非欧几里得几何, 图神经网络, 常微分方程

## 3 点简述
- 核心问题：液态时间常数网络局限于欧几里得空间，建模非欧几里得图结构时产生几何失真，降低表示质量。
- 方法要点：结合连续时间液态动力学与黎曼流形几何归纳偏置，在弯曲流形上直接建模图演化的常微分方程。
- 实验或效果：在真实世界基准测试中，RLSTG在复杂结构图上表现出优越性能，并提供理论保证。

## 摘要（原文）

> Liquid Time-Constant networks (LTCs), a type of continuous-time graph neural network, excel at modeling irregularly-sampled dynamics but are fundamentally confined to Euclidean space. This limitation introduces significant geometric distortion when representing real-world graphs with inherent non-Euclidean structures (e.g., hierarchies and cycles), degrading representation quality. To overcome this limitation, we introduce the Riemannian Liquid Spatio-Temporal Graph Network (RLSTG), a framework that unifies continuous-time liquid dynamics with the geometric inductive biases of Riemannian manifolds. RLSTG models graph evolution through an Ordinary Differential Equation (ODE) formulated directly on a curved manifold, enabling it to faithfully capture the intrinsic geometry of both structurally static and dynamic spatio-temporal graphs. Moreover, we provide rigorous theoretical guarantees for RLSTG, extending stability theorems of LTCs to the Riemannian domain and quantifying its expressive power via state trajectory analysis. Extensive experiments on real-world benchmarks demonstrate that, by combining advanced temporal dynamics with a Riemannian spatial representation, RLSTG achieves superior performance on graphs with complex structures. Project Page: https://rlstg.github.io

