---
layout: default
title: Sample-Efficient Neurosymbolic Deep Reinforcement Learning
---

# Sample-Efficient Neurosymbolic Deep Reinforcement Learning
**arXiv**：[2601.02850v1](https://arxiv.org/abs/2601.02850) · [PDF](https://arxiv.org/pdf/2601.02850.pdf)  
**作者**：Celeste Veronese, Daniele Meli, Alessandro Farinelli  

**一句话要点**：提出神经符号深度强化学习方法，利用符号知识提升样本效率和泛化能力。

**关键词**：神经符号强化学习, 样本效率, 泛化能力, 逻辑规则, 稀疏奖励, 网格世界

## 3 点简述
- 深度强化学习样本效率低、泛化差，尤其在稀疏奖励和长规划任务中。
- 集成符号知识，将简单任务的部分策略作为先验，通过逻辑规则在线推理指导训练。
- 在网格世界变体实验中，性能优于基线，加速收敛并增强可解释性。

## 摘要（原文）

> Reinforcement Learning (RL) is a well-established framework for sequential decision-making in complex environments. However, state-of-the-art Deep RL (DRL) algorithms typically require large training datasets and often struggle to generalize beyond small-scale training scenarios, even within standard benchmarks. We propose a neuro-symbolic DRL approach that integrates background symbolic knowledge to improve sample efficiency and generalization to more challenging, unseen tasks. Partial policies defined for simple domain instances, where high performance is easily attained, are transferred as useful priors to accelerate learning in more complex settings and avoid tuning DRL parameters from scratch. To do so, partial policies are represented as logical rules, and online reasoning is performed to guide the training process through two mechanisms: (i) biasing the action distribution during exploration, and (ii) rescaling Q-values during exploitation. This neuro-symbolic integration enhances interpretability and trustworthiness while accelerating convergence, particularly in sparse-reward environments and tasks with long planning horizons. We empirically validate our methodology on challenging variants of gridworld environments, both in the fully observable and partially observable setting. We show improved performance over a state-of-the-art reward machine baseline.

