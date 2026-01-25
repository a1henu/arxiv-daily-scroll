---
layout: default
title: Beyond Predictive Uncertainty: Reliable Representation Learning with Structural Constraints
---

# Beyond Predictive Uncertainty: Reliable Representation Learning with Structural Constraints
**arXiv**：[2601.16174v1](https://arxiv.org/abs/2601.16174) · [PDF](https://arxiv.org/pdf/2601.16174.pdf)  
**作者**：Yiyao Yang  

**一句话要点**：提出可靠表示学习框架，通过结构约束建模表示级不确定性以提升表示可靠性

**关键词**：表示学习, 不确定性估计, 结构约束, 正则化, 归纳偏置

## 3 点简述
- 核心问题：传统不确定性估计仅关注预测阶段，默认表示可靠，但表示本身可能存在不确定性
- 方法要点：引入表示级不确定性建模，结合稀疏性等结构约束作为归纳偏置正则化表示空间
- 实验或效果：未知，但框架独立于模型架构，可集成多种表示学习方法

## 摘要（原文）

> Uncertainty estimation in machine learning has traditionally focused on the prediction stage, aiming to quantify confidence in model outputs while treating learned representations as deterministic and reliable by default. In this work, we challenge this implicit assumption and argue that reliability should be regarded as a first-class property of learned representations themselves. We propose a principled framework for reliable representation learning that explicitly models representation-level uncertainty and leverages structural constraints as inductive biases to regularize the space of feasible representations. Our approach introduces uncertainty-aware regularization directly in the representation space, encouraging representations that are not only predictive but also stable, well-calibrated, and robust to noise and structural perturbations. Structural constraints, such as sparsity, relational structure, or feature-group dependencies, are incorporated to define meaningful geometry and reduce spurious variability in learned representations, without assuming fully correct or noise-free structure. Importantly, the proposed framework is independent of specific model architectures and can be integrated with a wide range of representation learning methods.

