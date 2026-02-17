---
layout: default
title: RNM-TD3: N:M Semi-structured Sparse Reinforcement Learning From Scratch
---

# RNM-TD3: N:M Semi-structured Sparse Reinforcement Learning From Scratch
**arXiv**：[2602.14578v1](https://arxiv.org/abs/2602.14578) · [PDF](https://arxiv.org/pdf/2602.14578.pdf)  
**作者**：Isam Vrce, Andreas Kassler, Gökçe Aydos  

**一句话要点**：提出RNM-TD3框架，首次在强化学习中实现N:M结构化稀疏训练

**关键词**：结构化稀疏, 深度强化学习, 硬件加速, 模型压缩, 连续控制

## 3 点简述
- 现有DRL稀疏方法多为非结构化，硬件加速受限且性能易受损
- 采用行级N:M稀疏模式，保持与专用加速器的兼容性
- 在连续控制任务中，2:4稀疏度下性能提升达14%，1:8稀疏度仍具竞争力

## 摘要（原文）

> Sparsity is a well-studied technique for compressing deep neural networks (DNNs) without compromising performance. In deep reinforcement learning (DRL), neural networks with up to 5% of their original weights can still be trained with minimal performance loss compared to their dense counterparts. However, most existing methods rely on unstructured fine-grained sparsity, which limits hardware acceleration opportunities due to irregular computation patterns. Structured coarse-grained sparsity enables hardware acceleration, yet typically degrades performance and increases pruning complexity. In this work, we present, to the best of our knowledge, the first study on N:M structured sparsity in RL, which balances compression, performance, and hardware efficiency. Our framework enforces row-wise N:M sparsity throughout training for all networks in off-policy RL (TD3), maintaining compatibility with accelerators that support N:M sparse matrix operations. Experiments on continuous-control benchmarks show that RNM-TD3, our N:M sparse agent, outperforms its dense counterpart at 50%-75% sparsity (e.g., 2:4 and 1:4), achieving up to a 14% increase in performance at 2:4 sparsity on the Ant environment. RNM-TD3 remains competitive even at 87.5% sparsity (1:8), while enabling potential training speedups.

