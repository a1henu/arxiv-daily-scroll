---
layout: default
title: Dyna-Style Reinforcement Learning Modeling and Control of Non-linear Dynamics
---

# Dyna-Style Reinforcement Learning Modeling and Control of Non-linear Dynamics
**arXiv**：[2512.21081v1](https://arxiv.org/abs/2512.21081) · [PDF](https://arxiv.org/pdf/2512.21081.pdf)  
**作者**：Karim Abdelsalam, Zeyad Gamal, Ayman El-Badawy  

**一句话要点**：提出SINDy-TD3框架以解决非线性系统控制中的样本效率问题

**关键词**：非线性系统控制, 强化学习, 数据驱动建模, 样本效率, 双旋翼系统

## 3 点简述
- 核心问题：非线性系统控制面临样本效率低和鲁棒性挑战
- 方法要点：结合SINDy数据驱动建模与TD3强化学习，通过合成数据提升训练效率
- 实验或效果：在双旋翼系统上验证，显示优于直接强化学习的精度和鲁棒性

## 摘要（原文）

> Controlling systems with complex, nonlinear dynamics poses a significant challenge, particularly in achieving efficient and robust control. In this paper, we propose a Dyna-Style Reinforcement Learning control framework that integrates Sparse Identification of Nonlinear Dynamics (SINDy) with Twin Delayed Deep Deterministic Policy Gradient (TD3) reinforcement learning. SINDy is used to identify a data-driven model of the system, capturing its key dynamics without requiring an explicit physical model. This identified model is used to generate synthetic rollouts that are periodically injected into the reinforcement learning replay buffer during training on the real environment, enabling efficient policy learning with limited data available. By leveraging this hybrid approach, we mitigate the sample inefficiency of traditional model-free reinforcement learning methods while ensuring accurate control of nonlinear systems. To demonstrate the effectiveness of this framework, we apply it to a bi-rotor system as a case study, evaluating its performance in stabilization and trajectory tracking. The results show that our SINDy-TD3 approach achieves superior accuracy and robustness compared to direct reinforcement learning techniques, highlighting the potential of combining data-driven modeling with reinforcement learning for complex dynamical systems.

