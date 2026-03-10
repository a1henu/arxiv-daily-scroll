---
layout: default
title: Structural Causal Bottleneck Models
---

# Structural Causal Bottleneck Models
**arXiv**：[2603.08682v1](https://arxiv.org/abs/2603.08682) · [PDF](https://arxiv.org/pdf/2603.08682.pdf)  
**作者**：Simon Bing, Jonas Wahl, Jakob Runge  

**一句话要点**：提出结构因果瓶颈模型以解决高维变量因果效应估计中的维度问题

**关键词**：结构因果模型, 因果瓶颈, 维度缩减, 因果效应估计, 迁移学习

## 3 点简述
- 核心问题：高维变量因果效应估计复杂，需降维但保持因果结构
- 方法要点：假设因果效应仅依赖于低维瓶颈统计量，提供灵活降维框架
- 实验或效果：在低样本迁移学习中展示瓶颈对效应估计的益处

## 摘要（原文）

> We introduce structural causal bottleneck models (SCBMs), a novel class of structural causal models. At the core of SCBMs lies the assumption that causal effects between high-dimensional variables only depend on low-dimensional summary statistics, or bottlenecks, of the causes. SCBMs provide a flexible framework for task-specific dimension reduction while being estimable via standard, simple learning algorithms in practice. We analyse identifiability in SCBMs, connect them to information bottlenecks in the sense of Tishby & Zaslavsky (2015), and illustrate how to estimate them experimentally. We also demonstrate the benefit of bottlenecks for effect estimation in low-sample transfer learning settings. We argue that SCBMs provide an alternative to existing causal dimension reduction frameworks like causal representation learning or causal abstraction learning.

