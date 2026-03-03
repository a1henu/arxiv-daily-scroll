---
layout: default
title: CHLU: The Causal Hamiltonian Learning Unit as a Symplectic Primitive for Deep Learning
---

# CHLU: The Causal Hamiltonian Learning Unit as a Symplectic Primitive for Deep Learning
**arXiv**：[2603.01768v1](https://arxiv.org/abs/2603.01768) · [PDF](https://arxiv.org/pdf/2603.01768.pdf)  
**作者**：Pratik Jawahar, Maurizio Pierini  

**一句话要点**：提出因果哈密顿学习单元以解决深度学习中的记忆-稳定性权衡问题

**关键词**：因果哈密顿学习单元, 辛积分, 相空间守恒, 深度学习原语, 时间动态建模, 生成模型

## 3 点简述
- 当前处理时间动态的深度学习原语存在离散不稳定或连续耗散的根本二分法
- CHLU通过强制相对论哈密顿结构和辛积分，严格守恒相空间体积
- 在MNIST数据集上展示了CHLU的生成能力作为原理验证

## 摘要（原文）

> Current deep learning primitives dealing with temporal dynamics suffer from a fundamental dichotomy: they are either discrete and unstable (LSTMs) \citep{pascanu_difficulty_2013}, leading to exploding or vanishing gradients; or they are continuous and dissipative (Neural ODEs) \citep{dupont_augmented_2019}, which destroy information over time to ensure stability. We propose the \textbf{Causal Hamiltonian Learning Unit} (pronounced: \textit{clue}), a novel Physics-grounded computational learning primitive. By enforcing a Relativistic Hamiltonian structure and utilizing symplectic integration, a CHLU strictly conserves phase-space volume, as an attempt to solve the memory-stability trade-off. We show that the CHLU is designed for infinite-horizon stability, as well as controllable noise filtering. We then demonstrate a CHLU's generative ability using the MNIST dataset as a proof-of-principle.

