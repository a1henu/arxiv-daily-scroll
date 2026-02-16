---
layout: default
title: Learning to Approximate Uniform Facility Location via Graph Neural Networks
---

# Learning to Approximate Uniform Facility Location via Graph Neural Networks
**arXiv**：[2602.13155v1](https://arxiv.org/abs/2602.13155) · [PDF](https://arxiv.org/pdf/2602.13155.pdf)  
**作者**：Chendi Qian, Christopher Morris, Stefanie Jegelka, Christian Sohler  

**一句话要点**：提出基于图神经网络的统一设施选址近似算法，结合学习与理论保证

**关键词**：图神经网络, 近似算法, 组合优化, 设施选址, 消息传递神经网络, 可微模型

## 3 点简述
- 针对统一设施选址问题，现有学习法依赖监督数据或强化学习，计算开销大且缺乏理论保证
- 开发全可微消息传递神经网络，嵌入近似算法原理，无需求解器监督或离散松弛
- 实验显示优于标准非学习近似算法，接近整数线性规划，并提供可证明的近似与泛化保证

## 摘要（原文）

> There has been a growing interest in using neural networks, especially message-passing neural networks (MPNNs), to solve hard combinatorial optimization problems heuristically. However, existing learning-based approaches for hard combinatorial optimization tasks often rely on supervised training data, reinforcement learning, or gradient estimators, leading to significant computational overhead, unstable training, or a lack of provable performance guarantees. In contrast, classical approximation algorithms offer such performance guarantees under worst-case inputs but are non-differentiable and unable to adaptively exploit structural regularities in natural input distributions. We address this dichotomy with the fundamental example of Uniform Facility Location (UniFL), a variant of the combinatorial facility location problem with applications in clustering, data summarization, logistics, and supply chain design. We develop a fully differentiable MPNN model that embeds approximation-algorithmic principles while avoiding the need for solver supervision or discrete relaxations. Our approach admits provable approximation and size generalization guarantees to much larger instances than seen during training. Empirically, we show that our approach outperforms standard non-learned approximation algorithms in terms of solution quality, closing the gap with computationally intensive integer linear programming approaches. Overall, this work provides a step toward bridging learning-based methods and approximation algorithms for discrete optimization.

