---
layout: default
title: Spectral Representation-based Reinforcement Learning
---

# Spectral Representation-based Reinforcement Learning
**arXiv**：[2512.15036v1](https://arxiv.org/abs/2512.15036) · [PDF](https://arxiv.org/pdf/2512.15036.pdf)  
**作者**：Chenxiao Gao, Haotian Sun, Na Li, Dale Schuurmans, Bo Dai  

**一句话要点**：提出基于谱表示的强化学习框架，以解决大状态动作空间中函数近似的理论模糊、优化不稳定和计算成本高问题。

**关键词**：谱表示, 强化学习, 转移算子, 部分可观测马尔可夫决策过程, 函数近似, 系统动态抽象

## 3 点简述
- 核心问题：强化学习在大状态动作空间中使用函数近似时，存在理论模糊、优化不稳定和计算成本高的问题。
- 方法要点：基于转移算子的谱分解构建谱表示，为策略优化提供系统动态的有效抽象和清晰理论表征。
- 实验或效果：在DeepMind Control Suite的20多个挑战性任务上验证，性能达到或超越当前最先进的模型无关和基于模型的基线方法。

## 摘要（原文）

> In real-world applications with large state and action spaces, reinforcement learning (RL) typically employs function approximations to represent core components like the policies, value functions, and dynamics models. Although powerful approximations such as neural networks offer great expressiveness, they often present theoretical ambiguities, suffer from optimization instability and exploration difficulty, and incur substantial computational costs in practice. In this paper, we introduce the perspective of spectral representations as a solution to address these difficulties in RL. Stemming from the spectral decomposition of the transition operator, this framework yields an effective abstraction of the system dynamics for subsequent policy optimization while also providing a clear theoretical characterization. We reveal how to construct spectral representations for transition operators that possess latent variable structures or energy-based structures, which implies different learning methods to extract spectral representations from data. Notably, each of these learning methods realizes an effective RL algorithm under this framework. We also provably extend this spectral view to partially observable MDPs. Finally, we validate these algorithms on over 20 challenging tasks from the DeepMind Control Suite, where they achieve performances comparable or superior to current state-of-the-art model-free and model-based baselines.

