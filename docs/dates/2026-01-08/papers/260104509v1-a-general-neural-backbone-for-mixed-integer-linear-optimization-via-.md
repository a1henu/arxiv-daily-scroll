---
layout: default
title: A General Neural Backbone for Mixed-Integer Linear Optimization via Dual Attention
---

# A General Neural Backbone for Mixed-Integer Linear Optimization via Dual Attention
**arXiv**：[2601.04509v1](https://arxiv.org/abs/2601.04509) · [PDF](https://arxiv.org/pdf/2601.04509.pdf)  
**作者**：Peixin Huang, Yaoxin Wu, Yining Ma, Cathy Wu, Wen Song, Wei Zhang  

**一句话要点**：提出基于双注意力机制的通用神经骨干网络，以增强混合整数线性规划的表示学习能力。

**关键词**：混合整数线性规划, 注意力机制, 图神经网络, 表示学习, 组合优化

## 3 点简述
- 核心问题：传统图神经网络在混合整数线性规划中受限于局部机制，表示能力不足。
- 方法要点：设计双注意力机制，在变量和约束间并行执行自注意力和交叉注意力，实现全局信息交换。
- 实验或效果：在多个基准测试中，该方法优于现有基线，验证了注意力架构在优化任务中的有效性。

## 摘要（原文）

> Mixed-integer linear programming (MILP), a widely used modeling framework for combinatorial optimization, are central to many scientific and engineering applications, yet remains computationally challenging at scale. Recent advances in deep learning address this challenge by representing MILP instances as variable-constraint bipartite graphs and applying graph neural networks (GNNs) to extract latent structural patterns and enhance solver efficiency. However, this architecture is inherently limited by the local-oriented mechanism, leading to restricted representation power and hindering neural approaches for MILP. Here we present an attention-driven neural architecture that learns expressive representations beyond the pure graph view. A dual-attention mechanism is designed to perform parallel self- and cross-attention over variables and constraints, enabling global information exchange and deeper representation learning. We apply this general backbone to various downstream tasks at the instance level, element level, and solving state level. Extensive experiments across widely used benchmarks show consistent improvements of our approach over state-of-the-art baselines, highlighting attention-based neural architectures as a powerful foundation for learning-enhanced mixed-integer linear optimization.

