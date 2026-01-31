---
layout: default
title: Constrained Meta Reinforcement Learning with Provable Test-Time Safety
---

# Constrained Meta Reinforcement Learning with Provable Test-Time Safety
**arXiv**：[2601.21845v1](https://arxiv.org/abs/2601.21845) · [PDF](https://arxiv.org/pdf/2601.21845.pdf)  
**作者**：Tingting Ni, Maryam Kamgarpour  

**一句话要点**：提出带可证明测试时安全性的约束元强化学习算法，以解决测试任务中的安全与样本效率问题。

**关键词**：元强化学习, 约束强化学习, 测试时安全性, 样本复杂度, 可证明保证

## 3 点简述
- 核心问题：如何在约束元强化学习中确保测试任务策略的安全性，同时降低样本复杂度。
- 方法要点：通过训练期间学习策略的细化，提供可证明的安全性和样本复杂度保证。
- 实验或效果：推导匹配下界，表明样本复杂度是紧的，支持更快学习最优策略。

## 摘要（原文）

> Meta reinforcement learning (RL) allows agents to leverage experience across a distribution of tasks on which the agent can train at will, enabling faster learning of optimal policies on new test tasks. Despite its success in improving sample complexity on test tasks, many real-world applications, such as robotics and healthcare, impose safety constraints during testing. Constrained meta RL provides a promising framework for integrating safety into meta RL. An open question in constrained meta RL is how to ensure the safety of the policy on the real-world test task, while reducing the sample complexity and thus, enabling faster learning of optimal policies. To address this gap, we propose an algorithm that refines policies learned during training, with provable safety and sample complexity guarantees for learning a near optimal policy on the test tasks. We further derive a matching lower bound, showing that this sample complexity is tight.

