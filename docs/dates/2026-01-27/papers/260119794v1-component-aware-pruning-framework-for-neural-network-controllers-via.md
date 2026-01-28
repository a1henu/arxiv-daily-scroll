---
layout: default
title: Component-Aware Pruning Framework for Neural Network Controllers via Gradient-Based Importance Estimation
---

# Component-Aware Pruning Framework for Neural Network Controllers via Gradient-Based Importance Estimation
**arXiv**：[2601.19794v1](https://arxiv.org/abs/2601.19794) · [PDF](https://arxiv.org/pdf/2601.19794.pdf)  
**作者**：Ganesh Sundaram, Jonas Ulmen, Daniel Görges  

**一句话要点**：提出基于梯度的组件感知剪枝框架，以解决多组件神经网络控制器的高计算复杂度问题。

**关键词**：神经网络剪枝, 组件感知剪枝, 梯度重要性估计, 模型压缩, 多组件架构, 计算复杂度优化

## 3 点简述
- 核心问题：多组件神经网络控制器计算复杂度高，传统剪枝方法难以捕捉功能重要性。
- 方法要点：利用梯度信息计算梯度累积、Fisher信息和贝叶斯不确定性三种重要性指标。
- 实验或效果：在自编码器和TD-MPC代理上验证，揭示结构依赖性和动态重要性变化。

## 摘要（原文）

> The transition from monolithic to multi-component neural architectures in advanced neural network controllers poses substantial challenges due to the high computational complexity of the latter. Conventional model compression techniques for complexity reduction, such as structured pruning based on norm-based metrics to estimate the relative importance of distinct parameter groups, often fail to capture functional significance. This paper introduces a component-aware pruning framework that utilizes gradient information to compute three distinct importance metrics during training: Gradient Accumulation, Fisher Information, and Bayesian Uncertainty. Experimental results with an autoencoder and a TD-MPC agent demonstrate that the proposed framework reveals critical structural dependencies and dynamic shifts in importance that static heuristics often miss, supporting more informed compression decisions.

