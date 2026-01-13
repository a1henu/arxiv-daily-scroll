---
layout: default
title: Puzzle it Out: Local-to-Global World Model for Offline Multi-Agent Reinforcement Learning
---

# Puzzle it Out: Local-to-Global World Model for Offline Multi-Agent Reinforcement Learning
**arXiv**：[2601.07463v1](https://arxiv.org/abs/2601.07463) · [PDF](https://arxiv.org/pdf/2601.07463.pdf)  
**作者**：Sijia li, Xinran Li, Shibo Chen, Jun Zhang  

**一句话要点**：提出局部到全局世界模型以解决离线多智能体强化学习中的保守策略问题

**关键词**：离线多智能体强化学习, 世界模型, 不确定性估计, 数据增强, 策略泛化

## 3 点简述
- 离线多智能体强化学习中，现有方法因局限于数据集分布导致策略保守，难以泛化。
- 提出局部到全局世界模型，通过局部预测推断全局动态，提升准确性并捕获智能体间依赖。
- 引入不确定性感知采样机制，加权合成数据以减少误差传播，实验显示优于基准方法。

## 摘要（原文）

> Offline multi-agent reinforcement learning (MARL) aims to solve cooperative decision-making problems in multi-agent systems using pre-collected datasets. Existing offline MARL methods primarily constrain training within the dataset distribution, resulting in overly conservative policies that struggle to generalize beyond the support of the data. While model-based approaches offer a promising solution by expanding the original dataset with synthetic data generated from a learned world model, the high dimensionality, non-stationarity, and complexity of multi-agent systems make it challenging to accurately estimate the transitions and reward functions in offline MARL. Given the difficulty of directly modeling joint dynamics, we propose a local-to-global (LOGO) world model, a novel framework that leverages local predictions-which are easier to estimate-to infer global state dynamics, thus improving prediction accuracy while implicitly capturing agent-wise dependencies. Using the trained world model, we generate synthetic data to augment the original dataset, expanding the effective state-action space. To ensure reliable policy learning, we further introduce an uncertainty-aware sampling mechanism that adaptively weights synthetic data by prediction uncertainty, reducing approximation error propagation to policies. In contrast to conventional ensemble-based methods, our approach requires only an additional encoder for uncertainty estimation, significantly reducing computational overhead while maintaining accuracy. Extensive experiments across 8 scenarios against 8 baselines demonstrate that our method surpasses state-of-the-art baselines on standard offline MARL benchmarks, establishing a new model-based baseline for generalizable offline multi-agent learning.

