---
layout: default
title: Constrained Group Relative Policy Optimization
---

# Constrained Group Relative Policy Optimization
**arXiv**：[2602.05863v1](https://arxiv.org/abs/2602.05863) · [PDF](https://arxiv.org/pdf/2602.05863.pdf)  
**作者**：Roger Girgis, Rodrigue de Schaetzen, Luke Rowe, Azalée Robitaille, Christopher Pal, Liam Paull  

**一句话要点**：提出约束组相对策略优化以解决带行为约束的策略学习问题

**关键词**：约束策略优化, 拉格朗日松弛, 优势估计, 机器人学习, 多模态基础模型

## 3 点简述
- 核心问题：GRPO扩展至带显式行为约束场景时，优势估计中的多分量处理可能导致约束学习失效
- 方法要点：基于拉格朗日松弛，引入标量化优势构造以保持奖励与约束项间的权衡
- 实验或效果：在网格世界和机器人任务中验证方法，提升约束满足度和任务成功率

## 摘要（原文）

> While Group Relative Policy Optimization (GRPO) has emerged as a scalable framework for critic-free policy learning, extending it to settings with explicit behavioral constraints remains underexplored. We introduce Constrained GRPO, a Lagrangian-based extension of GRPO for constrained policy optimization. Constraints are specified via indicator cost functions, enabling direct optimization of violation rates through a Lagrangian relaxation. We show that a naive multi-component treatment in advantage estimation can break constrained learning: mismatched component-wise standard deviations distort the relative importance of the different objective terms, which in turn corrupts the Lagrangian signal and prevents meaningful constraint enforcement. We formally derive this effect to motivate our scalarized advantage construction that preserves the intended trade-off between reward and constraint terms. Experiments in a toy gridworld confirm the predicted optimization pathology and demonstrate that scalarizing advantages restores stable constraint control. In addition, we evaluate Constrained GRPO on robotics tasks, where it improves constraint satisfaction while increasing task success, establishing a simple and effective recipe for constrained policy optimization in embodied AI domains that increasingly rely on large multimodal foundation models.

