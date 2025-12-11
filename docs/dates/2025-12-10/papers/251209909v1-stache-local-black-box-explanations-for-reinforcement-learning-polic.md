---
layout: default
title: STACHE: Local Black-Box Explanations for Reinforcement Learning Policies
---

# STACHE: Local Black-Box Explanations for Reinforcement Learning Policies
**arXiv**：[2512.09909v1](https://arxiv.org/abs/2512.09909) · [PDF](https://arxiv.org/pdf/2512.09909.pdf)  
**作者**：Andrew Elashkin, Orna Grumberg  

**一句话要点**：提出STACHE框架，为离散马尔可夫游戏中的强化学习策略生成局部黑盒解释

**关键词**：强化学习解释, 黑盒解释, 局部解释, 反事实分析, 策略调试

## 3 点简述
- 核心问题：强化学习代理在稀疏奖励或安全关键环境中行为不可预测，需可靠调试工具
- 方法要点：基于分解状态空间，通过搜索算法生成鲁棒性区域和最小反事实的复合解释
- 实验或效果：在Gymnasium环境中验证，能解释策略动作并捕捉训练中策略逻辑的演变

## 摘要（原文）

> Reinforcement learning agents often behave unexpectedly in sparse-reward or safety-critical environments, creating a strong need for reliable debugging and verification tools. In this paper, we propose STACHE, a comprehensive framework for generating local, black-box explanations for an agent's specific action within discrete Markov games. Our method produces a Composite Explanation consisting of two complementary components: (1) a Robustness Region, the connected neighborhood of states where the agent's action remains invariant, and (2) Minimal Counterfactuals, the smallest state perturbations required to alter that decision. By exploiting the structure of factored state spaces, we introduce an exact, search-based algorithm that circumvents the fidelity gaps of surrogate models. Empirical validation on Gymnasium environments demonstrates that our framework not only explains policy actions, but also effectively captures the evolution of policy logic during training - from erratic, unstable behavior to optimized, robust strategies - providing actionable insights into agent sensitivity and decision boundaries.

