---
layout: default
title: Performative Policy Gradient: Optimality in Performative Reinforcement Learning
---

# Performative Policy Gradient: Optimality in Performative Reinforcement Learning
**arXiv**：[2512.20576v1](https://arxiv.org/abs/2512.20576) · [PDF](https://arxiv.org/pdf/2512.20576.pdf)  
**作者**：Debabrota Basu, Udvas Das, Brahim Driss, Uddalak Mukherjee  

**一句话要点**：提出Performative Policy Gradient算法，以解决强化学习中策略部署后引发环境动态变化的最优性问题。

**关键词**：Performative强化学习, 策略梯度算法, 分布偏移, 最优策略, 熵正则化

## 3 点简述
- 核心问题：标准强化学习忽略策略部署后对环境动态的影响，导致性能下降。
- 方法要点：基于performative性能差异引理和策略梯度定理，设计PePG算法，确保策略在自身引发的分布偏移下保持最优。
- 实验或效果：在标准performative RL环境中，PePG优于标准策略梯度算法和现有追求稳定性的performative RL算法。

## 摘要（原文）

> Post-deployment machine learning algorithms often influence the environments they act in, and thus shift the underlying dynamics that the standard reinforcement learning (RL) methods ignore. While designing optimal algorithms in this performative setting has recently been studied in supervised learning, the RL counterpart remains under-explored. In this paper, we prove the performative counterparts of the performance difference lemma and the policy gradient theorem in RL, and further introduce the Performative Policy Gradient algorithm (PePG). PePG is the first policy gradient algorithm designed to account for performativity in RL. Under softmax parametrisation, and also with and without entropy regularisation, we prove that PePG converges to performatively optimal policies, i.e. policies that remain optimal under the distribution shifts induced by themselves. Thus, PePG significantly extends the prior works in Performative RL that achieves performative stability but not optimality. Furthermore, our empirical analysis on standard performative RL environments validate that PePG outperforms standard policy gradient algorithms and the existing performative RL algorithms aiming for stability.

