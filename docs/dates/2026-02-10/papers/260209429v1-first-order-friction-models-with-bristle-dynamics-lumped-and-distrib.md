---
layout: default
title: First-order friction models with bristle dynamics: lumped and distributed formulations
---

# First-order friction models with bristle dynamics: lumped and distributed formulations
**arXiv**：[2602.09429v1](https://arxiv.org/abs/2602.09429) · [PDF](https://arxiv.org/pdf/2602.09429.pdf)  
**作者**：Luigi Romano, Ole Morten Aamo, Jan Åslund, Erik Frisk  

**一句话要点**：提出基于物理推导的一阶动态摩擦模型，以模拟刷毛动力学并支持控制设计。

**关键词**：动态摩擦模型, 刷毛动力学, 稳定性分析, 分布模型, 控制设计

## 3 点简述
- 核心问题：现有速率依赖摩擦模型多基于经验，缺乏物理可解释性。
- 方法要点：从物理原理出发，通过反转摩擦特性近似刷毛动力学，推导出类似LuGre模型的新模型。
- 实验或效果：通过经典实验评估摩擦行为，并与LuGre模型对比验证相似性和差异。

## 摘要（原文）

> Dynamic models, particularly rate-dependent models, have proven effective in capturing the key phenomenological features of frictional processes, whilst also possessing important mathematical properties that facilitate the design of control and estimation algorithms. However, many rate-dependent formulations are built on empirical considerations, whereas physical derivations may offer greater interpretability. In this context, starting from fundamental physical principles, this paper introduces a novel class of first-order dynamic friction models that approximate the dynamics of a bristle element by inverting the friction characteristic. Amongst the developed models, a specific formulation closely resembling the LuGre model is derived using a simple rheological equation for the bristle element. This model is rigorously analyzed in terms of stability and passivity -- important properties that support the synthesis of observers and controllers. Furthermore, a distributed version, formulated as a hyperbolic partial differential equation (PDE), is presented, which enables the modeling of frictional processes commonly encountered in rolling contact phenomena. The tribological behavior of the proposed description is evaluated through classical experiments and validated against the response predicted by the LuGre model, revealing both notable similarities and key differences.

