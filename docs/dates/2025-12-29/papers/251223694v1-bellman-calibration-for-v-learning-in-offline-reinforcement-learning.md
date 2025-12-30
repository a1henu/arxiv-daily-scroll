---
layout: default
title: Bellman Calibration for V-Learning in Offline Reinforcement Learning
---

# Bellman Calibration for V-Learning in Offline Reinforcement Learning
**arXiv**：[2512.23694v1](https://arxiv.org/abs/2512.23694) · [PDF](https://arxiv.org/pdf/2512.23694.pdf)  
**作者**：Lars van der Laan, Nathan Kallus  

**一句话要点**：提出迭代贝尔曼校准，用于离线强化学习中无限时域马尔可夫决策过程的价值预测校准。

**关键词**：离线强化学习, 价值校准, 贝尔曼方程, 无限时域马尔可夫决策过程, 双重稳健估计

## 3 点简述
- 核心问题：离线强化学习中，价值预测在无限时域下缺乏校准，可能导致策略评估不准确。
- 方法要点：通过迭代回归贝尔曼目标到模型预测，使用双重稳健伪结果处理离线数据，实现模型无关的后处理校准。
- 实验或效果：在弱假设下提供有限样本保证，无需贝尔曼完备性或可实现性，提升预测可靠性。

## 摘要（原文）

> We introduce Iterated Bellman Calibration, a simple, model-agnostic, post-hoc procedure for calibrating off-policy value predictions in infinite-horizon Markov decision processes. Bellman calibration requires that states with similar predicted long-term returns exhibit one-step returns consistent with the Bellman equation under the target policy. We adapt classical histogram and isotonic calibration to the dynamic, counterfactual setting by repeatedly regressing fitted Bellman targets onto a model's predictions, using a doubly robust pseudo-outcome to handle off-policy data. This yields a one-dimensional fitted value iteration scheme that can be applied to any value estimator. Our analysis provides finite-sample guarantees for both calibration and prediction under weak assumptions, and critically, without requiring Bellman completeness or realizability.

