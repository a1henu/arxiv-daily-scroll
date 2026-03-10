---
layout: default
title: The Boiling Frog Threshold: Criticality and Blindness in World Model-Based Anomaly Detection Under Gradual Drift
---

# The Boiling Frog Threshold: Criticality and Blindness in World Model-Based Anomaly Detection Under Gradual Drift
**arXiv**：[2603.08455v1](https://arxiv.org/abs/2603.08455) · [PDF](https://arxiv.org/pdf/2603.08455.pdf)  
**作者**：Zhe Hong  

**一句话要点**：揭示基于世界模型的异常检测在渐变漂移下的临界阈值及其三因素交互机制

**关键词**：异常检测, 世界模型, 渐变漂移, 临界阈值, 强化学习, 环境动态

## 3 点简述
- 研究RL代理在观测渐变漂移下的异常检测临界阈值ε*，分析其普遍存在性与形状不变性
- 发现正弦漂移对所有检测器均不可检测，表明这是世界模型固有属性而非检测器缺陷
- 实验表明ε*遵循检测器参数幂律，但跨环境预测失败，揭示环境动态结构是关键缺失变量

## 摘要（原文）

> When an RL agent's observations are gradually corrupted, at what drift rate does it "wake up" -- and what determines this boundary? We study world model-based self-monitoring under continuous observation drift across four MuJoCo environments, three detector families (z-score, variance, percentile), and three model capacities. We find that (1) a sharp detection threshold $\varepsilon^*$ exists universally: below it, drift is absorbed as normal variation; above it, detection occurs rapidly. The threshold's existence and sigmoid shape are invariant across all detector families and model capacities, though its position depends on the interaction between detector sensitivity, noise floor structure, and environment dynamics. (2) Sinusoidal drift is completely undetectable by all detector families -- including variance and percentile detectors with no temporal smoothing -- establishing this as a world model property rather than a detector artifact. (3) Within each environment, $\varepsilon^*$ follows a power law in detector parameters ($R^2 = 0.89$-$0.97$), but cross-environment prediction fails ($R^2 = 0.45$), revealing that the missing variable is environment-specific dynamics structure $\partial \mathrm{PE}/\partial\varepsilon$. (4) In fragile environments, agents collapse before any detector can fire ("collapse before awareness"), creating a fundamentally unmonitorable failure mode. Our results reframe $\varepsilon^*$ from an emergent world model property to a three-way interaction between noise floor, detector, and environment dynamics, providing a more defensible and empirically grounded account of self-monitoring boundaries in RL agents.

