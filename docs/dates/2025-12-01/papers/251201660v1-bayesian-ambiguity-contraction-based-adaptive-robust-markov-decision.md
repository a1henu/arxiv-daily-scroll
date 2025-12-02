---
layout: default
title: Bayesian Ambiguity Contraction-based Adaptive Robust Markov Decision Processes for Adversarial Surveillance Missions
---

# Bayesian Ambiguity Contraction-based Adaptive Robust Markov Decision Processes for Adversarial Surveillance Missions
**arXiv**：[2512.01660v1](https://arxiv.org/abs/2512.01660) · [PDF](https://arxiv.org/pdf/2512.01660.pdf)  
**作者**：Jimin Choi, Max Z. Li  

**一句话要点**：提出基于贝叶斯模糊集收缩的自适应鲁棒马尔可夫决策过程，用于对抗性监视任务

**关键词**：自适应鲁棒马尔可夫决策过程, 对抗性监视, 贝叶斯模糊集收缩, 协作作战飞机, 智能监视与侦察, 模型不确定性

## 3 点简述
- 核心问题：在对抗性环境中，静态鲁棒马尔可夫决策过程无法适应新观测，导致模型不确定性和实时决策挑战。
- 方法要点：通过交替移动和感知状态建模任务，增量消除不一致威胁模型，实现从保守到激进行为的策略优化。
- 实验或效果：在多种网络拓扑下，相比名义和静态鲁棒规划器，获得更高任务奖励和更少暴露事件。

## 摘要（原文）

> Collaborative Combat Aircraft (CCAs) are envisioned to enable autonomous Intelligence, Surveillance, and Reconnaissance (ISR) missions in contested environments, where adversaries may act strategically to deceive or evade detection. These missions pose challenges due to model uncertainty and the need for safe, real-time decision-making. Robust Markov Decision Processes (RMDPs) provide worst-case guarantees but are limited by static ambiguity sets that capture initial uncertainty without adapting to new observations. This paper presents an adaptive RMDP framework tailored to ISR missions with CCAs. We introduce a mission-specific formulation in which aircraft alternate between movement and sensing states. Adversarial tactics are modeled as a finite set of transition kernels, each capturing assumptions about how adversarial sensing or environmental conditions affect rewards. Our approach incrementally refines policies by eliminating inconsistent threat models, allowing agents to shift from conservative to aggressive behaviors while maintaining robustness. We provide theoretical guarantees showing that the adaptive planner converges as credible sets contract to the true threat and maintains safety under uncertainty. Experiments under Gaussian and non-Gaussian threat models across diverse network topologies show higher mission rewards and fewer exposure events compared to nominal and static robust planners.

