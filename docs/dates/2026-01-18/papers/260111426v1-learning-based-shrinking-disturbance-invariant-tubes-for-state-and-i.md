---
layout: default
title: Learning-Based Shrinking Disturbance-Invariant Tubes for State- and Input-Dependent Uncertainty
---

# Learning-Based Shrinking Disturbance-Invariant Tubes for State- and Input-Dependent Uncertainty
**arXiv**：[2601.11426v1](https://arxiv.org/abs/2601.11426) · [PDF](https://arxiv.org/pdf/2601.11426.pdf)  
**作者**：Abdelrahman Ramadan, Sidney Givigi  

**一句话要点**：提出基于学习的收缩扰动不变管构建框架，用于状态和输入依赖不确定性下的安全认证。

**关键词**：扰动不变管, 高斯过程学习, 模型预测控制, 集合不变性, 安全认证

## 3 点简述
- 核心问题：在状态和输入依赖不确定性下，构建收缩扰动不变管以解决集合验证与扰动模型间的循环依赖。
- 方法要点：利用高斯过程后验生成可信椭球，通过两时间尺度方案分离学习与迭代，确保集合单调嵌套和硬约束保持。
- 实验或效果：双积分器案例显示，在数据丰富区域管截面收缩，同时保持不变性，验证了方法的有效性。

## 摘要（原文）

> We develop a learning-based framework for constructing shrinking disturbance-invariant tubes under state- and input-dependent uncertainty, intended as a building block for tube Model Predictive Control (MPC), and certify safety via a lifted, isotone (order-preserving) fixed-point map. Gaussian Process (GP) posteriors become $(1-α)$ credible ellipsoids, then polytopic outer sets for deterministic set operations. A two-time-scale scheme separates learning epochs, where these polytopes are frozen, from an inner, outside-in iteration that converges to a compact fixed point $Z^\star\!\subseteq\!\mathcal G$; its state projection is RPI for the plant. As data accumulate, disturbance polytopes tighten, and the associated tubes nest monotonically, resolving the circular dependence between the set to be verified and the disturbance model while preserving hard constraints. A double-integrator study illustrates shrinking tube cross-sections in data-rich regions while maintaining invariance.

