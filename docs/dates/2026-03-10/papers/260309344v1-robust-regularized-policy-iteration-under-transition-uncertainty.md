---
layout: default
title: Robust Regularized Policy Iteration under Transition Uncertainty
---

# Robust Regularized Policy Iteration under Transition Uncertainty
**arXiv**：[2603.09344v1](https://arxiv.org/abs/2603.09344) · [PDF](https://arxiv.org/pdf/2603.09344.pdf)  
**作者**：Hongqiang Lin, Zhenghui Fu, Weihao Tang, Pengfei Wang, Yiding Sun, Qixian Huang, Dongxu Zhang  

**一句话要点**：提出鲁棒正则化策略迭代以解决离线强化学习中的分布偏移和转移不确定性

**关键词**：离线强化学习, 鲁棒优化, 策略迭代, 分布偏移, 转移不确定性, KL正则化

## 3 点简述
- 核心问题：离线强化学习在分布偏移下性能下降，策略可能访问值估计不可靠的分布外状态-动作对。
- 方法要点：将离线强化学习建模为鲁棒策略优化，用KL正则化替代难解的最大-最小双层目标，基于鲁棒正则化贝尔曼算子设计高效策略迭代。
- 实验或效果：在D4RL基准测试中平均性能强，多数环境优于PMDB等基线，Q值在认知不确定性高区域下降，策略避免不可靠动作。

## 摘要（原文）

> Offline reinforcement learning (RL) enables data-efficient and safe policy learning without online exploration, but its performance often degrades under distribution shift. The learned policy may visit out-of-distribution state-action pairs where value estimates and learned dynamics are unreliable. To address policy-induced extrapolation and transition uncertainty in a unified framework, we formulate offline RL as robust policy optimization, treating the transition kernel as a decision variable within an uncertainty set and optimizing the policy against the worst-case dynamics. We propose Robust Regularized Policy Iteration (RRPI), which replaces the intractable max-min bilevel objective with a tractable KL-regularized surrogate and derives an efficient policy iteration procedure based on a robust regularized Bellman operator. We provide theoretical guarantees by showing that the proposed operator is a $γ$-contraction and that iteratively updating the surrogate yields monotonic improvement of the original robust objective with convergence. Experiments on D4RL benchmarks demonstrate that RRPI achieves strong average performance, outperforming recent baselines including percentile-based methods such as PMDB on the majority of environments while remaining competitive on the rest. Moreover, RRPI exhibits robust behavior. The learned $Q$-values decrease in regions with higher epistemic uncertainty, suggesting that the resulting policy avoids unreliable out-of-distribution actions under transition uncertainty.

