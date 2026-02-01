---
layout: default
title: Deep QP Safety Filter: Model-free Learning for Reachability-based Safety Filter
---

# Deep QP Safety Filter: Model-free Learning for Reachability-based Safety Filter
**arXiv**：[2601.21297v1](https://arxiv.org/abs/2601.21297) · [PDF](https://arxiv.org/pdf/2601.21297.pdf)  
**作者**：Byeongjun Kim, H. Jin Kim  

**一句话要点**：提出Deep QP Safety Filter，结合可达性分析与无模型学习，为黑盒动力系统提供数据驱动的安全层。

**关键词**：安全过滤器, 无模型学习, 可达性分析, 二次规划, 神经网络, 黑盒系统

## 3 点简述
- 核心问题：为黑盒动力系统设计无模型的安全过滤器，避免预收敛失败并加速学习。
- 方法要点：结合Hamilton-Jacobi可达性与无模型学习，通过收缩损失训练神经网络学习QP安全过滤器。
- 实验或效果：在多种动力系统和RL任务中，显著减少失败并提升回报，适用于非光滑值函数。

## 摘要（原文）

> We introduce Deep QP Safety Filter, a fully data-driven safety layer for black-box dynamical systems. Our method learns a Quadratic-Program (QP) safety filter without model knowledge by combining Hamilton-Jacobi (HJ) reachability with model-free learning. We construct contraction-based losses for both the safety value and its derivatives, and train two neural networks accordingly. In the exact setting, the learned critic converges to the viscosity solution (and its derivative), even for non-smooth values. Across diverse dynamical systems -- even including a hybrid system -- and multiple RL tasks, Deep QP Safety Filter substantially reduces pre-convergence failures while accelerating learning toward higher returns than strong baselines, offering a principled and practical route to safe, model-free control.

