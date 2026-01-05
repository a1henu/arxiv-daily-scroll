---
layout: default
title: Optimal Transport-Based Decentralized Multi-Agent Distribution Matching
---

# Optimal Transport-Based Decentralized Multi-Agent Distribution Matching
**arXiv**：[2601.00548v1](https://arxiv.org/abs/2601.00548) · [PDF](https://arxiv.org/pdf/2601.00548.pdf)  
**作者**：Kooktae Lee  

**一句话要点**：提出基于最优传输的去中心化多智能体分布匹配框架，实现仅依赖局部信息的终端分布达成。

**关键词**：多智能体系统, 最优传输, 去中心化控制, 分布匹配, Wasserstein距离, 局部信息

## 3 点简述
- 核心问题：多智能体系统如何通过去中心化控制达成指定终端空间分布，避免直接求解全局最优传输问题。
- 方法要点：将分布匹配目标重构为可处理的每智能体决策过程，引入顺序权重更新规则和基于记忆的校正机制。
- 实验或效果：仿真显示框架在去中心化操作下实现有效且可扩展的分布匹配，收敛性在线性和非线性动态下得到保证。

## 摘要（原文）

> This paper presents a decentralized control framework for distribution matching in multi-agent systems (MAS), where agents collectively achieve a prescribed terminal spatial distribution. The problem is formulated using optimal transport (Wasserstein distance), which provides a principled measure of distributional discrepancy and serves as the basis for the control design. To avoid solving the global optimal transport problem directly, the distribution-matching objective is reformulated into a tractable per-agent decision process, enabling each agent to identify its desired terminal locations using only locally available information. A sequential weight-update rule is introduced to construct feasible local transport plans, and a memory-based correction mechanism is incorporated to maintain reliable operation under intermittent and range-limited communication. Convergence guarantees are established, showing cycle-wise improvement of a surrogate transport cost under both linear and nonlinear agent dynamics. Simulation results demonstrate that the proposed framework achieves effective and scalable distribution matching while operating fully in a decentralized manner.

