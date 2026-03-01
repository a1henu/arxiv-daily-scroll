---
layout: default
title: QSIM: Mitigating Overestimation in Multi-Agent Reinforcement Learning via Action Similarity Weighted Q-Learning
---

# QSIM: Mitigating Overestimation in Multi-Agent Reinforcement Learning via Action Similarity Weighted Q-Learning
**arXiv**：[2602.22786v1](https://arxiv.org/abs/2602.22786) · [PDF](https://arxiv.org/pdf/2602.22786.pdf)  
**作者**：Yuanjun Li, Bin Zhang, Hao Chen, Zhouyang Jiang, Dapeng Li, Zhiwei Xu  

**一句话要点**：提出QSIM框架，通过动作相似性加权Q学习缓解多智能体强化学习中的Q值高估问题。

**关键词**：多智能体强化学习, 值分解, Q值高估, 动作相似性, 学习稳定性, 联合动作空间

## 3 点简述
- 核心问题：值分解方法因使用max算子导致Q值系统性高估，影响学习稳定性。
- 方法要点：基于动作相似性重构TD目标，加权整合近贪婪联合动作空间的Q值。
- 实验或效果：可无缝集成多种值分解方法，提升性能与稳定性，显著缓解高估。

## 摘要（原文）

> Value decomposition (VD) methods have achieved remarkable success in cooperative multi-agent reinforcement learning (MARL). However, their reliance on the max operator for temporal-difference (TD) target calculation leads to systematic Q-value overestimation. This issue is particularly severe in MARL due to the combinatorial explosion of the joint action space, which often results in unstable learning and suboptimal policies. To address this problem, we propose QSIM, a similarity weighted Q-learning framework that reconstructs the TD target using action similarity. Instead of using the greedy joint action directly, QSIM forms a similarity weighted expectation over a structured near-greedy joint action space. This formulation allows the target to integrate Q-values from diverse yet behaviorally related actions while assigning greater influence to those that are more similar to the greedy choice. By smoothing the target with structurally relevant alternatives, QSIM effectively mitigates overestimation and improves learning stability. Extensive experiments demonstrate that QSIM can be seamlessly integrated with various VD methods, consistently yielding superior performance and stability compared to the original algorithms. Furthermore, empirical analysis confirms that QSIM significantly mitigates the systematic value overestimation in MARL. Code is available at https://github.com/MaoMaoLYJ/pymarl-qsim.

