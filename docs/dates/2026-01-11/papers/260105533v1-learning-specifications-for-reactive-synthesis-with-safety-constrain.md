---
layout: default
title: Learning specifications for reactive synthesis with safety constraints
---

# Learning specifications for reactive synthesis with safety constraints
**arXiv**：[2601.05533v1](https://arxiv.org/abs/2601.05533) · [PDF](https://arxiv.org/pdf/2601.05533.pdf)  
**作者**：Kandai Watanabe, Nicholas Renninger, Sriram Sankaranarayanan, Morteza Lahijanian  

**一句话要点**：提出基于安全约束的PDFA学习与多目标反应式合成方法，使机器人能在动态环境中执行复杂任务。

**关键词**：反应式合成, 安全约束学习, 概率确定性有限自动机, 多目标优化, 机器人任务执行

## 3 点简述
- 核心问题：从演示中学习任务规范，确保机器人行为在动态环境中安全且符合用户偏好。
- 方法要点：通过安全约束学习PDFA，并设计多目标反应式合成算法生成满足任务与成本权衡的策略。
- 实验或效果：实验验证算法有效，学习PDFA无安全违规，合成策略能平衡任务完成、机器人成本和用户偏好。

## 摘要（原文）

> This paper presents a novel approach to learning from demonstration that enables robots to autonomously execute complex tasks in dynamic environments. We model latent tasks as probabilistic formal languages and introduce a tailored reactive synthesis framework that balances robot costs with user task preferences. Our methodology focuses on safety-constrained learning and inferring formal task specifications as Probabilistic Deterministic Finite Automata (PDFA). We adapt existing evidence-driven state merging algorithms and incorporate safety requirements throughout the learning process to ensure that the learned PDFA always complies with safety constraints. Furthermore, we introduce a multi-objective reactive synthesis algorithm that generates deterministic strategies that are guaranteed to satisfy the PDFA task while optimizing the trade-offs between user preferences and robot costs, resulting in a Pareto front of optimal solutions. Our approach models the interaction as a two-player game between the robot and the environment, accounting for dynamic changes. We present a computationally-tractable value iteration algorithm to generate the Pareto front and the corresponding deterministic strategies. Comprehensive experimental results demonstrate the effectiveness of our algorithms across various robots and tasks, showing that the learned PDFA never includes unsafe behaviors and that synthesized strategies consistently achieve the task while meeting both the robot cost and user-preference requirements.

