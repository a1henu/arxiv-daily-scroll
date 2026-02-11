---
layout: default
title: Grounding LTL Tasks in Sub-Symbolic RL Environments for Zero-Shot Generalization
---

# Grounding LTL Tasks in Sub-Symbolic RL Environments for Zero-Shot Generalization
**arXiv**：[2602.09761v1](https://arxiv.org/abs/2602.09761) · [PDF](https://arxiv.org/pdf/2602.09761.pdf)  
**作者**：Matteo Pannacci, Andrea Fanti, Elena Umili, Roberto Capobianco  

**一句话要点**：提出联合训练多任务策略与符号接地器的方法，以在子符号RL环境中实现零样本泛化。

**关键词**：强化学习, 线性时序逻辑, 符号接地, 多任务学习, 零样本泛化, 神经奖励机

## 3 点简述
- 核心问题：在子符号环境中训练RL代理遵循线性时序逻辑指令，无需先验符号映射知识。
- 方法要点：通过神经奖励机半监督训练符号接地器，仅使用原始观察和稀疏奖励。
- 实验或效果：在视觉环境中性能接近真实符号接地，优于现有子符号环境方法。

## 摘要（原文）

> In this work we address the problem of training a Reinforcement Learning agent to follow multiple temporally-extended instructions expressed in Linear Temporal Logic in sub-symbolic environments. Previous multi-task work has mostly relied on knowledge of the mapping between raw observations and symbols appearing in the formulae. We drop this unrealistic assumption by jointly training a multi-task policy and a symbol grounder with the same experience. The symbol grounder is trained only from raw observations and sparse rewards via Neural Reward Machines in a semi-supervised fashion. Experiments on vision-based environments show that our method achieves performance comparable to using the true symbol grounding and significantly outperforms state-of-the-art methods for sub-symbolic environments.

