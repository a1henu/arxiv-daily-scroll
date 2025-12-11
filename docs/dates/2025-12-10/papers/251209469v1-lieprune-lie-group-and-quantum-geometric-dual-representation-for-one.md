---
layout: default
title: LiePrune: Lie Group and Quantum Geometric Dual Representation for One-Shot Structured Pruning of Quantum Neural Networks
---

# LiePrune: Lie Group and Quantum Geometric Dual Representation for One-Shot Structured Pruning of Quantum Neural Networks
**arXiv**：[2512.09469v1](https://arxiv.org/abs/2512.09469) · [PDF](https://arxiv.org/pdf/2512.09469.pdf)  
**作者**：Haijian Shao, Bowen Yang, Wei Liu, Xing Deng, Yingtao Jiang  

**一句话要点**：提出LiePrune框架，利用李群和量子几何对量子神经网络进行一次性结构化剪枝

**关键词**：量子神经网络, 结构化剪枝, 李群表示, 量子几何, 一次性压缩, 参数化量子电路

## 3 点简述
- 量子神经网络面临参数过多、贫瘠高原和硬件限制等可扩展性问题
- 基于李群-李代数对偶空间和量子几何特征空间，实现原理性冗余检测和压缩
- 在量子分类、生成建模和量子化学任务中实现超10倍压缩，性能无损失或提升

## 摘要（原文）

> Quantum neural networks (QNNs) and parameterized quantum circuits (PQCs) are key building blocks for near-term quantum machine learning. However, their scalability is constrained by excessive parameters, barren plateaus, and hardware limitations. We propose LiePrune, the first mathematically grounded one-shot structured pruning framework for QNNs that leverages Lie group structure and quantum geometric information. Each gate is jointly represented in a Lie group--Lie algebra dual space and a quantum geometric feature space, enabling principled redundancy detection and aggressive compression. Experiments on quantum classification (MNIST, FashionMNIST), quantum generative modeling (Bars-and-Stripes), and quantum chemistry (LiH VQE) show that LiePrune achieves over $10\times$ compression with negligible or even improved task performance, while providing provable guarantees on redundancy detection, functional approximation, and computational complexity.

