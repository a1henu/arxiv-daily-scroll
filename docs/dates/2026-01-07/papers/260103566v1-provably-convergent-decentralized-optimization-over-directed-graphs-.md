---
layout: default
title: Provably Convergent Decentralized Optimization over Directed Graphs under Generalized Smoothness
---

# Provably Convergent Decentralized Optimization over Directed Graphs under Generalized Smoothness
**arXiv**：[2601.03566v1](https://arxiv.org/abs/2601.03566) · [PDF](https://arxiv.org/pdf/2601.03566.pdf)  
**作者**：Yanan Bo, Yongqiang Wang  

**一句话要点**：提出基于广义平滑性的去中心化优化方法，在定向图上实现收敛，适用于异构数据环境。

**关键词**：去中心化优化, 广义平滑性, 梯度追踪, 梯度裁剪, 定向图, 异构数据

## 3 点简述
- 研究去中心化优化在广义(L0, L1)-平滑性下的问题，放宽经典Lipschitz平滑性假设，适应梯度快速变化场景。
- 结合梯度追踪与梯度裁剪技术，设计裁剪阈值，确保在定向通信图上准确收敛，无需梯度差异有界假设。
- 在LIBSVM和CIFAR-10数据集上实验，使用正则化逻辑回归和卷积神经网络，验证方法稳定性和更快收敛速度。

## 摘要（原文）

> Decentralized optimization has become a fundamental tool for large-scale learning systems; however, most existing methods rely on the classical Lipschitz smoothness assumption, which is often violated in problems with rapidly varying gradients. Motivated by this limitation, we study decentralized optimization under the generalized $(L_0, L_1)$-smoothness framework, in which the Hessian norm is allowed to grow linearly with the gradient norm, thereby accommodating rapidly varying gradients beyond classical Lipschitz smoothness. We integrate gradient-tracking techniques with gradient clipping and carefully design the clipping threshold to ensure accurate convergence over directed communication graphs under generalized smoothness. In contrast to existing distributed optimization results under generalized smoothness that require a bounded gradient dissimilarity assumption, our results remain valid even when the gradient dissimilarity is unbounded, making the proposed framework more applicable to realistic heterogeneous data environments. We validate our approach via numerical experiments on standard benchmark datasets, including LIBSVM and CIFAR-10, using regularized logistic regression and convolutional neural networks, demonstrating superior stability and faster convergence over existing methods.

