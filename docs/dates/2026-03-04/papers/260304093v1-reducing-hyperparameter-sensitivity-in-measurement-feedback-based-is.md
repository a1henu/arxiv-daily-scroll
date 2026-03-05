---
layout: default
title: Reducing hyperparameter sensitivity in measurement-feedback based Ising machines
---

# Reducing hyperparameter sensitivity in measurement-feedback based Ising machines
**arXiv**：[2603.04093v1](https://arxiv.org/abs/2603.04093) · [PDF](https://arxiv.org/pdf/2603.04093.pdf)  
**作者**：Toon Sevenants, Guy Van der Sande, Guy Verschaffelt  

**一句话要点**：提出降低测量反馈伊辛机超参数敏感性的方法，以解决离散时间实现中的性能限制问题。

**关键词**：伊辛机, 超参数优化, 测量反馈架构, 组合优化, 硬件求解器, 离散时间系统

## 3 点简述
- 核心问题：离散时间测量反馈伊辛机的有效超参数范围远小于连续时间模型，影响实际性能。
- 方法要点：分析超参数敏感性差异，提出降低敏感性的方法，适用于测量反馈架构。
- 实验或效果：通过实验验证了所提方法的有效性，提升了伊辛机的实用性和稳定性。

## 摘要（原文）

> Analog Ising machines have been proposed as heuristic hardware solvers for combinatorial optimization problems, with the potential to outperform conventional approaches, provided that their hyperparameters are carefully tuned. Their temporal evolution is often described using time-continuous dynamics. However, most experimental implementations rely on measurement-feedback architectures that operate in a time-discrete manner. We observe that in such setups, the range of effective hyperparameters is substantially smaller than in the envisioned time-continuous analog Ising machine. In this paper, we analyze this discrepancy and discuss its impact on the practical operation of Ising machines. Next, we propose and experimentally verify a method to reduce the sensitivity to hyperparameter selection of these measurement-feedback architectures.

