---
layout: default
title: Logic-Guided Vector Fields for Constrained Generative Modeling
---

# Logic-Guided Vector Fields for Constrained Generative Modeling
**arXiv**：[2602.02009v1](https://arxiv.org/abs/2602.02009) · [PDF](https://arxiv.org/pdf/2602.02009.pdf)  
**作者**：Ali Baheri  

**一句话要点**：提出逻辑引导向量场以增强流匹配生成模型中的约束执行能力

**关键词**：神经符号系统, 流匹配生成模型, 逻辑约束, 向量场, 约束生成建模, 可微松弛

## 3 点简述
- 核心问题：生成模型缺乏在生成时强制执行声明性约束的机制
- 方法要点：结合训练时逻辑损失和推理时约束梯度调整，注入可微逻辑约束
- 实验或效果：在三个案例中减少约束违反59-82%，提升分布保真度或可行性

## 摘要（原文）

> Neuro-symbolic systems aim to combine the expressive structure of symbolic logic with the flexibility of neural learning; yet, generative models typically lack mechanisms to enforce declarative constraints at generation time. We propose Logic-Guided Vector Fields (LGVF), a neuro-symbolic framework that injects symbolic knowledge, specified as differentiable relaxations of logical constraints, into flow matching generative models. LGVF couples two complementary mechanisms: (1) a training-time logic loss that penalizes constraint violations along continuous flow trajectories, with weights that emphasize correctness near the target distribution; and (2) an inference-time adjustment that steers sampling using constraint gradients, acting as a lightweight, logic-informed correction to the learned dynamics. We evaluate LGVF on three constrained generation case studies spanning linear, nonlinear, and multi-region feasibility constraints. Across all settings, LGVF reduces constraint violations by 59-82% compared to standard flow matching and achieves the lowest violation rates in each case. In the linear and ring settings, LGVF also improves distributional fidelity as measured by MMD, while in the multi-obstacle setting, we observe a satisfaction-fidelity trade-off, with improved feasibility but increased MMD. Beyond quantitative gains, LGVF yields constraint-aware vector fields exhibiting emergent obstacle-avoidance behavior, routing samples around forbidden regions without explicit path planning.

