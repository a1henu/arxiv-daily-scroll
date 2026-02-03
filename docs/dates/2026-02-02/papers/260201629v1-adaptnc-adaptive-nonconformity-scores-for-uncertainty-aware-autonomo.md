---
layout: default
title: AdaptNC: Adaptive Nonconformity Scores for Uncertainty-Aware Autonomous Systems in Dynamic Environments
---

# AdaptNC: Adaptive Nonconformity Scores for Uncertainty-Aware Autonomous Systems in Dynamic Environments
**arXiv**：[2602.01629v1](https://arxiv.org/abs/2602.01629) · [PDF](https://arxiv.org/pdf/2602.01629.pdf)  
**作者**：Renukanandan Tumu, Aditya Singh, Rahul Mangharam  

**一句话要点**：提出AdaptNC框架，通过联合在线调整非一致性分数和阈值，以在动态环境中优化自主系统的不确定性量化。

**关键词**：共形预测, 不确定性量化, 在线适应, 非一致性分数, 动态环境, 自主系统

## 3 点简述
- 核心问题：标准共形预测在分布偏移下因静态非一致性分数导致预测区域保守且体积低效。
- 方法要点：AdaptNC结合自适应重加权优化分数函数，并引入回放缓冲机制稳定覆盖度。
- 实验或效果：在多种机器人基准测试中，AdaptNC显著减少预测区域体积，同时保持目标覆盖水平。

## 摘要（原文）

> Rigorous uncertainty quantification is essential for the safe deployment of autonomous systems in unconstrained environments. Conformal Prediction (CP) provides a distribution-free framework for this task, yet its standard formulations rely on exchangeability assumptions that are violated by the distribution shifts inherent in real-world robotics. Existing online CP methods maintain target coverage by adaptively scaling the conformal threshold, but typically employ a static nonconformity score function. We show that this fixed geometry leads to highly conservative, volume-inefficient prediction regions when environments undergo structural shifts. To address this, we propose \textbf{AdaptNC}, a framework for the joint online adaptation of both the nonconformity score parameters and the conformal threshold. AdaptNC leverages an adaptive reweighting scheme to optimize score functions, and introduces a replay buffer mechanism to mitigate the coverage instability that occurs during score transitions. We evaluate AdaptNC on diverse robotic benchmarks involving multi-agent policy changes, environmental changes and sensor degradation. Our results demonstrate that AdaptNC significantly reduces prediction region volume compared to state-of-the-art threshold-only baselines while maintaining target coverage levels.

