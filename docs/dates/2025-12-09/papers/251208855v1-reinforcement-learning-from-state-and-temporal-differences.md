---
layout: default
title: Reinforcement Learning From State and Temporal Differences
---

# Reinforcement Learning From State and Temporal Differences
**arXiv**：[2512.08855v1](https://arxiv.org/abs/2512.08855) · [PDF](https://arxiv.org/pdf/2512.08855.pdf)  
**作者**：Lex Weaver, Jonathan Baxter  

**一句话要点**：提出STD(λ)方法，通过优化状态相对值解决TD(λ)在策略改进中的次优问题。

**关键词**：强化学习, 时序差分学习, 函数逼近, 策略改进, 状态相对值, 二元决策

## 3 点简述
- 核心问题：TD(λ)在函数逼近中最小化状态值平方误差，但策略改进更依赖状态相对排序。
- 方法要点：引入STD(λ)，在二元决策问题中基于状态相对值训练函数逼近器，理论证明单调策略改进。
- 实验或效果：在双状态系统、三状态系统和西洋双陆棋中验证TD(λ)次优，STD(λ)在双状态系统和acrobot变体上成功演示。

## 摘要（原文）

> TD($λ$) with function approximation has proved empirically successful for some complex reinforcement learning problems. For linear approximation, TD($λ$) has been shown to minimise the squared error between the approximate value of each state and the true value. However, as far as policy is concerned, it is error in the relative ordering of states that is critical, rather than error in the state values. We illustrate this point, both in simple two-state and three-state systems in which TD($λ$)--starting from an optimal policy--converges to a sub-optimal policy, and also in backgammon. We then present a modified form of TD($λ$), called STD($λ$), in which function approximators are trained with respect to relative state values on binary decision problems. A theoretical analysis, including a proof of monotonic policy improvement for STD($λ$) in the context of the two-state system, is presented, along with a comparison with Bertsekas' differential training method [1]. This is followed by successful demonstrations of STD($λ$) on the two-state system and a variation on the well known acrobot problem.

