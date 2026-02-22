---
layout: default
title: Dataless Weight Disentanglement in Task Arithmetic via Kronecker-Factored Approximate Curvature
---

# Dataless Weight Disentanglement in Task Arithmetic via Kronecker-Factored Approximate Curvature
**arXiv**：[2602.17385v1](https://arxiv.org/abs/2602.17385) · [PDF](https://arxiv.org/pdf/2602.17385.pdf)  
**作者**：Angelo Porrello, Pietro Buzzega, Felix Dangel, Thomas Sommariva, Riccardo Salami, Lorenzo Bonicelli, Simone Calderara  

**一句话要点**：提出基于Kronecker分解近似曲率的无数据权重解耦方法，以解决任务算术中的交叉任务干扰问题。

**关键词**：任务算术, 权重解耦, Kronecker分解近似曲率, 无数据正则化, 表示漂移, 交叉任务干扰

## 3 点简述
- 任务算术中多任务向量组合易导致交叉任务干扰和表示漂移，影响性能。
- 通过将表示漂移正则化为曲率矩阵近似问题，采用Kronecker分解近似曲率实现无数据正则化。
- 在任务添加和否定中达到先进效果，复杂度恒定且无需调优，提升鲁棒性。

## 摘要（原文）

> Task Arithmetic yields a modular, scalable way to adapt foundation models. Combining multiple task vectors, however, can lead to cross-task interference, causing representation drift and degraded performance. Representation drift regularization provides a natural remedy to disentangle task vectors; however, existing approaches typically require external task data, conflicting with modularity and data availability constraints (e.g., privacy requirements). We propose a dataless approach by framing regularization against representation drift as a curvature matrix approximation problem. This allows us to leverage well-established techniques; in particular, we adopt Kronecker-Factored Approximate Curvature and obtain a practical regularizer that achieves state-of-the-art results in task addition and negation. Our method has constant complexity in the number of tasks and promotes robustness to task vector rescaling, eliminating the need for held-out tuning.

