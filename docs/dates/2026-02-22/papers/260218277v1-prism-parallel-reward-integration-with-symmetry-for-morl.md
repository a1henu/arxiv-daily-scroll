---
layout: default
title: PRISM: Parallel Reward Integration with Symmetry for MORL
---

# PRISM: Parallel Reward Integration with Symmetry for MORL
**arXiv**：[2602.18277v1](https://arxiv.org/abs/2602.18277) · [PDF](https://arxiv.org/pdf/2602.18277.pdf)  
**作者**：Finn van der Knaap, Kejiang Qian, Zheng Xu, Fengxiang He  

**一句话要点**：提出PRISM算法以解决异构多目标强化学习中稀疏奖励信用分配难题

**关键词**：多目标强化学习, 稀疏奖励, 对称性归纳偏置, 反射等变性, 帕累托优化, MuJoCo基准

## 3 点简述
- 研究异构多目标强化学习，其中目标时间频率差异导致稀疏奖励学习效率低
- 提出PRISM算法，通过反射对称性归纳偏置对齐奖励通道，包含ReSymNet模型和SymReg正则器
- 在MuJoCo基准测试中，PRISM显著优于稀疏奖励基线和全密集奖励预言机，提升帕累托覆盖

## 摘要（原文）

> This work studies heterogeneous Multi-Objective Reinforcement Learning (MORL), where objectives can differ sharply in temporal frequency. Such heterogeneity allows dense objectives to dominate learning, while sparse long-horizon rewards receive weak credit assignment, leading to poor sample efficiency. We propose a Parallel Reward Integration with Symmetry (PRISM) algorithm that enforces reflectional symmetry as an inductive bias in aligning reward channels. PRISM introduces ReSymNet, a theory-motivated model that reconciles temporal-frequency mismatches across objectives, using residual blocks to learn a scaled opportunity value that accelerates exploration while preserving the optimal policy. We also propose SymReg, a reflectional equivariance regulariser that enforces agent mirroring and constrains policy search to a reflection-equivariant subspace. This restriction provably reduces hypothesis complexity and improves generalisation. Across MuJoCo benchmarks, PRISM consistently outperforms both a sparse-reward baseline and an oracle trained with full dense rewards, improving Pareto coverage and distributional balance: it achieves hypervolume gains exceeding 100\% over the baseline and up to 32\% over the oracle. The code is at \href{https://github.com/EVIEHub/PRISM}{https://github.com/EVIEHub/PRISM}.

