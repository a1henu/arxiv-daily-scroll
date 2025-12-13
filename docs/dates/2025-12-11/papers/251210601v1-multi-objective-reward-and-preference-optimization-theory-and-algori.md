---
layout: default
title: Multi-Objective Reward and Preference Optimization: Theory and Algorithms
---

# Multi-Objective Reward and Preference Optimization: Theory and Algorithms
**arXiv**：[2512.10601v1](https://arxiv.org/abs/2512.10601) · [PDF](https://arxiv.org/pdf/2512.10601.pdf)  
**作者**：Akhil Agnihotri  

**一句话要点**：提出多目标约束强化学习框架与算法，涵盖平均成本、有限时域和偏好学习场景。

**关键词**：约束强化学习, 偏好学习, 策略优化, 平均成本马尔可夫决策过程, 模型对齐, 后验采样

## 3 点简述
- 核心问题：约束强化学习在平均成本、有限时域和人类偏好学习中的理论与算法挑战。
- 方法要点：开发ACPO、e-COP、warmPref-PS、PSPL和MOPO算法，集成敏感性分析、信任域更新和后验采样。
- 实验或效果：在安全关键环境中实现理论保证和最优性能，提升对齐大型语言模型的鲁棒性和可扩展性。

## 摘要（原文）

> This thesis develops theoretical frameworks and algorithms that advance constrained reinforcement learning (RL) across control, preference learning, and alignment of large language models. The first contribution addresses constrained Markov Decision Processes (CMDPs) under the average-cost criterion through the Average-Constrained Policy Optimization (ACPO) algorithm. ACPO integrates sensitivity analysis with trust-region updates to ensure stable constraint handling, achieving state-of-the-art empirical performance with theoretical guarantees. Constrained RL is then extended to finite-horizon settings via e-COP, the first policy optimization method for episodic CMDPs. Built on an episodic policy difference lemma, e-COP offers provable performance, simplicity, and scalability in safety-critical environments. The thesis then investigates reinforcement learning from human preferences. warmPref-PS introduces a posterior sampling strategy for linear bandits that integrates offline preference data from heterogeneous raters into online learning. Explicit modeling of rater competence yields substantial regret reduction and more efficient data collection for RLHF. The PSPL algorithm further advances preference-based RL by jointly sampling reward models and transition dynamics from pairwise trajectory comparisons, providing Bayesian simple-regret guarantees and robust empirical identification of optimal policies. The final contribution applies these methods to large-scale model alignment. A multi-objective constrained optimization view yields MOPO, an iterative algorithm with closed-form updates that scales to multi-billion-parameter language models and remains robust across alignment settings. Collectively, the thesis unifies constrained RL across average-cost, episodic, and preference-driven paradigms, delivering theoretical advances and practical tools for safe and aligned decision-making.

