---
layout: default
title: T-REGS: Minimum Spanning Tree Regularization for Self-Supervised Learning
---

# T-REGS: Minimum Spanning Tree Regularization for Self-Supervised Learning
**arXiv**：[2510.23484v1](https://arxiv.org/abs/2510.23484) · [PDF](https://arxiv.org/pdf/2510.23484.pdf)  
**作者**：Julie Mordacq, David Loiseaux, Vicky Kalogeiton, Steve Oudot  

**一句话要点**：提出T-REGS正则化框架，通过最小生成树长度缓解自监督学习中的维度坍缩和分布不均匀问题。

**关键词**：自监督学习, 正则化方法, 最小生成树, 维度坍缩, 分布均匀性, 表示学习

## 3 点简述
- 自监督学习中存在维度坍缩和分布不均匀问题，影响表示质量。
- T-REGS利用最小生成树长度作为正则项，理论上在紧致黎曼流形上同时缓解坍缩和促进均匀性。
- 在合成数据和经典基准测试中验证了T-REGS提升表示质量的有效性。

## 摘要（原文）

> Self-supervised learning (SSL) has emerged as a powerful paradigm for
> learning representations without labeled data, often by enforcing invariance to
> input transformations such as rotations or blurring. Recent studies have
> highlighted two pivotal properties for effective representations: (i) avoiding
> dimensional collapse-where the learned features occupy only a low-dimensional
> subspace, and (ii) enhancing uniformity of the induced distribution. In this
> work, we introduce T-REGS, a simple regularization framework for SSL based on
> the length of the Minimum Spanning Tree (MST) over the learned representation.
> We provide theoretical analysis demonstrating that T-REGS simultaneously
> mitigates dimensional collapse and promotes distribution uniformity on
> arbitrary compact Riemannian manifolds. Several experiments on synthetic data
> and on classical SSL benchmarks validate the effectiveness of our approach at
> enhancing representation quality.

