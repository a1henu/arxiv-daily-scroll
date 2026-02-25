---
layout: default
title: Fuz-RL: A Fuzzy-Guided Robust Framework for Safe Reinforcement Learning under Uncertainty
---

# Fuz-RL: A Fuzzy-Guided Robust Framework for Safe Reinforcement Learning under Uncertainty
**arXiv**：[2602.20729v1](https://arxiv.org/abs/2602.20729) · [PDF](https://arxiv.org/pdf/2602.20729.pdf)  
**作者**：Xu Wan, Chao Yang, Cheng Yang, Jie Song, Mingyang Sun  

**一句话要点**：提出Fuz-RL框架，通过模糊测度引导解决不确定环境下的安全强化学习问题。

**关键词**：安全强化学习, 模糊测度, 鲁棒决策, Choquet积分, 不确定性处理, 模型无关框架

## 3 点简述
- 核心问题：真实环境中多源不确定性对安全强化学习的可解释风险评估和鲁棒决策构成挑战。
- 方法要点：基于Choquet积分开发模糊Bellman算子，估计鲁棒值函数，避免min-max优化。
- 实验或效果：在安全控制场景中，模型无关地集成现有基线，显著提升不确定条件下的安全性和控制性能。

## 摘要（原文）

> Safe Reinforcement Learning (RL) is crucial for achieving high performance while ensuring safety in real-world applications. However, the complex interplay of multiple uncertainty sources in real environments poses significant challenges for interpretable risk assessment and robust decision-making. To address these challenges, we propose Fuz-RL, a fuzzy measure-guided robust framework for safe RL. Specifically, our framework develops a novel fuzzy Bellman operator for estimating robust value functions using Choquet integrals. Theoretically, we prove that solving the Fuz-RL problem (in Constrained Markov Decision Process (CMDP) form) is equivalent to solving distributionally robust safe RL problems (in robust CMDP form), effectively avoiding min-max optimization. Empirical analyses on safe-control-gym and safety-gymnasium scenarios demonstrate that Fuz-RL effectively integrates with existing safe RL baselines in a model-free manner, significantly improving both safety and control performance under various types of uncertainties in observation, action, and dynamics.

