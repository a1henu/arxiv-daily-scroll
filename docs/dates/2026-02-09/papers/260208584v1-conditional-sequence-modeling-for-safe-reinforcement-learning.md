---
layout: default
title: Conditional Sequence Modeling for Safe Reinforcement Learning
---

# Conditional Sequence Modeling for Safe Reinforcement Learning
**arXiv**：[2602.08584v1](https://arxiv.org/abs/2602.08584) · [PDF](https://arxiv.org/pdf/2602.08584.pdf)  
**作者**：Wensong Bai, Chao Zhang, Qihang Xu, Chufan Chen, Chenhao Zhou, Hui Qian  

**一句话要点**：提出RCDT方法，基于条件序列建模实现离线安全强化学习的零成本阈值适应部署。

**关键词**：离线安全强化学习, 条件序列建模, 零样本部署, 成本阈值适应, 轨迹重加权, Q值正则化

## 3 点简述
- 核心问题：离线安全强化学习中，现有方法因预定义成本阈值导致策略泛化性和部署灵活性受限。
- 方法要点：RCDT结合拉格朗日式成本惩罚与自适应系数，引入奖励-成本感知轨迹重加权和Q值正则化优化回报-成本权衡。
- 实验或效果：在DSRL基准测试中，RCDT在回报-成本权衡上优于基线方法，提升了离线安全强化学习性能。

## 摘要（原文）

> Offline safe reinforcement learning (RL) aims to learn policies from a fixed dataset while maximizing performance under cumulative cost constraints. In practice, deployment requirements often vary across scenarios, necessitating a single policy that can adapt zero-shot to different cost thresholds. However, most existing offline safe RL methods are trained under a pre-specified threshold, yielding policies with limited generalization and deployment flexibility across cost thresholds. Motivated by recent progress in conditional sequence modeling (CSM), which enables flexible goal-conditioned control by specifying target returns, we propose RCDT, a CSM-based method that supports zero-shot deployment across multiple cost thresholds within a single trained policy. RCDT is the first CSM-based offline safe RL algorithm that integrates a Lagrangian-style cost penalty with an auto-adaptive penalty coefficient. To avoid overly conservative behavior and achieve a more favorable return--cost trade-off, a reward--cost-aware trajectory reweighting mechanism and Q-value regularization are further incorporated. Extensive experiments on the DSRL benchmark demonstrate that RCDT consistently improves return--cost trade-offs over representative baselines, advancing the state-of-the-art in offline safe RL.

