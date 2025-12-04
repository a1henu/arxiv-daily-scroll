---
layout: default
title: CoGraM: Context-sensitive granular optimization method with rollback for robust model fusion
---

# CoGraM: Context-sensitive granular optimization method with rollback for robust model fusion
**arXiv**：[2512.03610v1](https://arxiv.org/abs/2512.03610) · [PDF](https://arxiv.org/pdf/2512.03610.pdf)  
**作者**：Julius Lenz  

**一句话要点**：提出CoGraM方法以解决联邦学习中无需重训练的神经网络融合不准确和不稳定的问题

**关键词**：神经网络融合, 联邦学习, 上下文敏感优化, 回滚机制, 损失对齐

## 3 点简述
- 核心问题：联邦学习中权重平均或Fisher融合等方法常导致精度损失和结果不稳定
- 方法要点：多阶段、上下文敏感、基于损失的迭代优化，跨层级对齐决策并引入回滚机制
- 实验或效果：相比Fisher等方法，CoGraM能显著提升融合网络的性能

## 摘要（原文）

> Merging neural networks without retraining is central to federated and distributed learning. Common methods such as weight averaging or Fisher merging often lose accuracy and are unstable across seeds. CoGraM (Contextual Granular Merging) is a multi-stage, context-sensitive, loss-based, and iterative optimization method across layers, neurons, and weight levels that aligns decisions with loss differences and thresholds and prevents harmful updates through rollback. CoGraM is an optimization method that addresses the weaknesses of methods such as Fisher and can significantly improve the merged network.

