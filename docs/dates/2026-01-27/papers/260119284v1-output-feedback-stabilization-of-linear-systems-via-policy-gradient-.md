---
layout: default
title: Output Feedback Stabilization of Linear Systems via Policy Gradient Methods
---

# Output Feedback Stabilization of Linear Systems via Policy Gradient Methods
**arXiv**：[2601.19284v1](https://arxiv.org/abs/2601.19284) · [PDF](https://arxiv.org/pdf/2601.19284.pdf)  
**作者**：Ankang Zhang, Ming Chi, Xiaoling Wang, Lintao Ye  

**一句话要点**：提出基于策略梯度的输出反馈算法以稳定未知部分可观线性系统

**关键词**：输出反馈稳定, 策略梯度方法, 部分可观系统, 无模型学习, 线性动态系统

## 3 点简述
- 针对部分可观线性系统，研究无模型输出反馈的稳定问题
- 利用零阶策略梯度更新，基于系统轨迹收敛至稳定点
- 通过数值实验验证算法有效性并分析样本复杂度

## 摘要（原文）

> Stabilizing a dynamical system is a fundamental problem that serves as a cornerstone for many complex tasks in the field of control systems. The problem becomes challenging when the system model is unknown. Among the Reinforcement Learning (RL) algorithms that have been successfully applied to solve problems pertaining to unknown linear dynamical systems, the policy gradient (PG) method stands out due to its ease of implementation and can solve the problem in a model-free manner. However, most of the existing works on PG methods for unknown linear dynamical systems assume full-state feedback. In this paper, we take a step towards model-free learning for partially observable linear dynamical systems with output feedback and focus on the fundamental stabilization problem of the system. We propose an algorithmic framework that stretches the boundary of PG methods to the problem without global convergence guarantees. We show that by leveraging zeroth-order PG update based on system trajectories and its convergence to stationary points, the proposed algorithms return a stabilizing output feedback policy for discrete-time linear dynamical systems. We also explicitly characterize the sample complexity of our algorithm and verify the effectiveness of the algorithm using numerical examples.

