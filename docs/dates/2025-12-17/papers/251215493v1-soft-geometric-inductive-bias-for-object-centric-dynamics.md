---
layout: default
title: Soft Geometric Inductive Bias for Object Centric Dynamics
---

# Soft Geometric Inductive Bias for Object Centric Dynamics
**arXiv**：[2512.15493v1](https://arxiv.org/abs/2512.15493) · [PDF](https://arxiv.org/pdf/2512.15493.pdf)  
**作者**：Hampus Linander, Conor Heins, Alexander Tschantz, Marco Perin, Christopher Buckley  

**一句话要点**：提出基于几何代数神经网络的物体中心世界模型，以软几何归纳偏置提升多物体场景的物理动力学建模性能。

**关键词**：几何代数神经网络, 软几何归纳偏置, 物体中心世界模型, 物理动力学建模, 多物体场景

## 3 点简述
- 核心问题：精确群等变性在对称性被破坏时可能降低物理动力学学习性能。
- 方法要点：利用几何代数神经网络构建物体中心世界模型，提供软几何归纳偏置。
- 实验或效果：在2D刚体动力学模拟环境中，模型在长时程预测中展现出比非等变性基线更好的物理保真度。

## 摘要（原文）

> Equivariance is a powerful prior for learning physical dynamics, yet exact group equivariance can degrade performance if the symmetries are broken. We propose object-centric world models built with geometric algebra neural networks, providing a soft geometric inductive bias. Our models are evaluated using simulated environments of 2d rigid body dynamics with static obstacles, where we train for next-step predictions autoregressively. For long-horizon rollouts we show that the soft inductive bias of our models results in better performance in terms of physical fidelity compared to non-equivariant baseline models. The approach complements recent soft-equivariance ideas and aligns with the view that simple, well-chosen priors can yield robust generalization. These results suggest that geometric algebra offers an effective middle ground between hand-crafted physics and unstructured deep nets, delivering sample-efficient dynamics models for multi-object scenes.

