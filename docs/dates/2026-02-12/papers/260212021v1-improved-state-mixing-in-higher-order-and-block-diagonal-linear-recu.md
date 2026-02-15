---
layout: default
title: Improved state mixing in higher-order and block diagonal linear recurrent networks
---

# Improved state mixing in higher-order and block diagonal linear recurrent networks
**arXiv**：[2602.12021v1](https://arxiv.org/abs/2602.12021) · [PDF](https://arxiv.org/pdf/2602.12021.pdf)  
**作者**：Igor Dubinin, Antonio Orvieto, Felix Effenberger  

**一句话要点**：提出高阶和块对角线性循环网络以增强状态混合，提升线性序列模型的表达力与效率平衡。

**关键词**：线性循环网络, 状态空间模型, 序列建模, 表达力增强, 计算效率, 结构化状态混合

## 3 点简述
- 线性循环网络因对角状态转移限制表达力，而密集或非线性模型计算成本高。
- 引入高阶线性循环单元和块对角线性循环单元，通过结构化状态混合增强表达力。
- 在合成序列建模和语言建模中，块对角线性循环单元性能匹配或超越基线，高阶单元参数效率高。

## 摘要（原文）

> Linear recurrent networks (LRNNs) and linear state space models (SSMs) promise computational and memory efficiency on long-sequence modeling tasks, yet their diagonal state transitions limit expressivity. Dense and nonlinear architectures (e.g., LSTMs) on the other hand are provably more expressive, but computationally costly. Here, we explore how expressivity in LRNNs can be increased via richer state mixing across time and channels while maintaining competitive efficiency. Specifically, we introduce two structured LRNN architectures: (i) Higher-order Linear Recurrent Units (H-LRU), which generalize first-order recurrence to higher order, mixing multiple past states, and (ii) Block-Diagonal LRUs (BD-LRU), which enable dense intra-block channel mixing. Per-channel (H-LRU) or per-row (BD-LRU) L1-normalization of selective gates stabilizes training and allows for scaling window/block sizes. A parallel-scan implementation of the proposed architectures keeps the throughput competitive with diagonal LRNNs for moderate orders (H-LRU) and block sizes (BD-LRU). In synthetic sequence modeling tasks, the performance of BD-LRU matches or exceeds those of linear SSMs (Mamba), low-rank LRNNs (DeltaNet) and LSTM baselines, while H-LRU is found to be the most parameter-efficient in compression task. In both synthetic sequence modeling and language modeling, our results indicate that the structure of state mixing rather than width alone shapes expressivity of LRNNs, offering a practical route to closing the efficiency-expressivity gap in linear sequence models.

