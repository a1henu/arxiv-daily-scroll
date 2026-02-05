---
layout: default
title: Rationality Measurement and Theory for Reinforcement Learning Agents
---

# Rationality Measurement and Theory for Reinforcement Learning Agents
**arXiv**：[2602.04737v1](https://arxiv.org/abs/2602.04737) · [PDF](https://arxiv.org/pdf/2602.04737.pdf)  
**作者**：Kejiang Qian, Amos Storkey, Fengxiang He  

**一句话要点**：提出强化学习智能体的理性度量与理论框架，以评估部署中的决策合理性。

**关键词**：强化学习, 理性度量, 泛化理论, 环境偏移, 正则化, 领域随机化

## 3 点简述
- 核心问题：强化学习智能体的理性属性在部署中至关重要，但缺乏系统度量与理论分析。
- 方法要点：定义理性风险及其差距，分解为环境偏移和算法泛化性，并用Wasserstein距离和Rademacher复杂度上界。
- 实验或效果：实验验证理论假设，支持正则化器和领域随机化的益处，以及环境偏移的危害。

## 摘要（原文）

> This paper proposes a suite of rationality measures and associated theory for reinforcement learning agents, a property increasingly critical yet rarely explored. We define an action in deployment to be perfectly rational if it maximises the hidden true value function in the steepest direction. The expected value discrepancy of a policy's actions against their rational counterparts, culminating over the trajectory in deployment, is defined to be expected rational risk; an empirical average version in training is also defined. Their difference, termed as rational risk gap, is decomposed into (1) an extrinsic component caused by environment shifts between training and deployment, and (2) an intrinsic one due to the algorithm's generalisability in a dynamic environment. They are upper bounded by, respectively, (1) the $1$-Wasserstein distance between transition kernels and initial state distributions in training and deployment, and (2) the empirical Rademacher complexity of the value function class. Our theory suggests hypotheses on the benefits from regularisers (including layer normalisation, $\ell_2$ regularisation, and weight normalisation) and domain randomisation, as well as the harm from environment shifts. Experiments are in full agreement with these hypotheses. The code is available at https://github.com/EVIEHub/Rationality.

