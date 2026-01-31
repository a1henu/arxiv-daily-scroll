---
layout: default
title: Learning to Optimize Job Shop Scheduling Under Structural Uncertainty
---

# Learning to Optimize Job Shop Scheduling Under Structural Uncertainty
**arXiv**：[2601.21389v1](https://arxiv.org/abs/2601.21389) · [PDF](https://arxiv.org/pdf/2601.21389.pdf)  
**作者**：Rui Zhang, Jianwei Niu, Xuefeng Liu, Shaojie Tang, Jing Yuan  

**一句话要点**：提出UP-AAC方法以解决作业车间调度中的结构不确定性挑战

**关键词**：作业车间调度, 结构不确定性, 强化学习, 非对称架构, 注意力机制

## 3 点简述
- 核心问题：作业车间调度面临结构不确定性，即作业路径选择由未知情境因素决定，导致现有方法信用分配错误。
- 方法要点：采用非对称架构，演员接收随机状态，评论家接收事后重构的确定状态，以学习更准确的价值函数，降低策略梯度方差。
- 实验或效果：在基准实例上，该方法在减少完工时间方面优于现有方法，验证了其有效性。

## 摘要（原文）

> The Job-Shop Scheduling Problem (JSSP), under various forms of manufacturing uncertainty, has recently attracted considerable research attention. Most existing studies focus on parameter uncertainty, such as variable processing times, and typically adopt the actor-critic framework. In this paper, we explore a different but prevalent form of uncertainty in JSSP: structural uncertainty. Structural uncertainty arises when a job may follow one of several routing paths, and the selection is determined not by policy, but by situational factors (e.g., the quality of intermediate products) that cannot be known in advance. Existing methods struggle to address this challenge due to incorrect credit assignment: a high-quality action may be unfairly penalized if it is followed by a time-consuming path. To address this problem, we propose a novel method named UP-AAC. In contrast to conventional actor-critic methods, UP-AAC employs an asymmetric architecture. While its actor receives a standard stochastic state, the critic is crucially provided with a deterministic state reconstructed in hindsight. This design allows the critic to learn a more accurate value function, which in turn provides a lower-variance policy gradient to the actor, leading to more stable learning. In addition, we design an attention-based Uncertainty Perception Model (UPM) to enhance the actor's scheduling decisions. Extensive experiments demonstrate that our method outperforms existing approaches in reducing makespan on benchmark instances.

