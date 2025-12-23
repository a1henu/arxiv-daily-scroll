---
layout: default
title: Learning General Policies with Policy Gradient Methods
---

# Learning General Policies with Policy Gradient Methods
**arXiv**：[2512.19366v1](https://arxiv.org/abs/2512.19366) · [PDF](https://arxiv.org/pdf/2512.19366.pdf)  
**作者**：Simon Ståhlberg, Blai Bonet, Hector Geffner  

**一句话要点**：提出基于策略梯度的通用策略学习方法，结合组合方法与深度强化学习以提升泛化能力。

**关键词**：通用策略学习, 策略梯度方法, 图神经网络, 强化学习泛化, 组合规划方法

## 3 点简述
- 核心问题：强化学习在泛化方面存在挑战，需学习适用于领域所有实例的通用策略。
- 方法要点：将策略建模为状态转移分类器，使用图神经网络表示策略，避免特征池和可扩展性瓶颈。
- 实验或效果：在基准测试中，策略梯度方法学习到的策略泛化能力接近组合方法，并处理了GNN表达限制和最优性-泛化权衡。

## 摘要（原文）

> While reinforcement learning methods have delivered remarkable results in a number of settings, generalization, i.e., the ability to produce policies that generalize in a reliable and systematic way, has remained a challenge. The problem of generalization has been addressed formally in classical planning where provable correct policies that generalize over all instances of a given domain have been learned using combinatorial methods. The aim of this work is to bring these two research threads together to illuminate the conditions under which (deep) reinforcement learning approaches, and in particular, policy optimization methods, can be used to learn policies that generalize like combinatorial methods do. We draw on lessons learned from previous combinatorial and deep learning approaches, and extend them in a convenient way. From the former, we model policies as state transition classifiers, as (ground) actions are not general and change from instance to instance. From the latter, we use graph neural networks (GNNs) adapted to deal with relational structures for representing value functions over planning states, and in our case, policies. With these ingredients in place, we find that actor-critic methods can be used to learn policies that generalize almost as well as those obtained using combinatorial approaches while avoiding the scalability bottleneck and the use of feature pools. Moreover, the limitations of the DRL methods on the benchmarks considered have little to do with deep learning or reinforcement learning algorithms, and result from the well-understood expressive limitations of GNNs, and the tradeoff between optimality and generalization (general policies cannot be optimal in some domains). Both of these limitations are addressed without changing the basic DRL methods by adding derived predicates and an alternative cost structure to optimize.

