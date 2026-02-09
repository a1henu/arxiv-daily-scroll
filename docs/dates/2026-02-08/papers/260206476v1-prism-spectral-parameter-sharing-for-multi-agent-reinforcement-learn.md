---
layout: default
title: Prism: Spectral Parameter Sharing for Multi-Agent Reinforcement Learning
---

# Prism: Spectral Parameter Sharing for Multi-Agent Reinforcement Learning
**arXiv**：[2602.06476v1](https://arxiv.org/abs/2602.06476) · [PDF](https://arxiv.org/pdf/2602.06476.pdf)  
**作者**：Kyungbeom Kim, Seungwon Oh, Kyung-Joong Kim  

**一句话要点**：提出Prism框架，通过谱域参数共享解决多智能体强化学习中的行为同质化问题。

**关键词**：多智能体强化学习, 参数共享, 谱域表示, 奇异值分解, 行为多样性, 资源效率

## 3 点简述
- 核心问题：传统全共享参数导致智能体行为同质化，影响多智能体强化学习的性能。
- 方法要点：利用奇异值分解在谱域表示共享网络，智能体共享奇异向量方向，学习不同的谱掩码以促进多样性。
- 实验或效果：在LBF、SMACv2和MaMuJoCo基准测试中，Prism实现竞争性性能并保持资源效率。

## 摘要（原文）

> Parameter sharing is a key strategy in multi-agent reinforcement learning (MARL) for improving scalability, yet conventional fully shared architectures often collapse into homogeneous behaviors. Recent methods introduce diversity through clustering, pruning, or masking, but typically compromise resource efficiency. We propose Prism, a parameter sharing framework that induces inter-agent diversity by representing shared networks in the spectral domain via singular value decomposition (SVD). All agents share the singular vector directions while learning distinct spectral masks on singular values. This mechanism encourages inter-agent diversity and preserves scalability. Extensive experiments on both homogeneous (LBF, SMACv2) and heterogeneous (MaMuJoCo) benchmarks show that Prism achieves competitive performance with superior resource efficiency.

