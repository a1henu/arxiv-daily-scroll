---
layout: default
title: Introduction to optimization methods for training SciML models
---

# Introduction to optimization methods for training SciML models
**arXiv**：[2601.10222v1](https://arxiv.org/abs/2601.10222) · [PDF](https://arxiv.org/pdf/2601.10222.pdf)  
**作者**：Alena Kopaničáková, Elisa Riccietti  

**一句话要点**：介绍优化方法以训练科学机器学习模型，强调问题结构对算法选择的影响

**关键词**：科学机器学习, 优化方法, 物理约束优化, 损失函数分析, 算法选择, 教程示例

## 3 点简述
- 核心问题：科学机器学习中物理约束导致损失函数全局耦合、刚性和强各向异性，限制标准随机方法有效性
- 方法要点：回顾一阶和二阶优化技术，包括确定性和随机设置，并讨论其适应物理约束和数据驱动模型
- 实验或效果：通过教程示例说明实践策略，并突出科学计算与科学机器学习交叉领域的开放研究方向

## 摘要（原文）

> Optimization is central to both modern machine learning (ML) and scientific machine learning (SciML), yet the structure of the underlying optimization problems differs substantially across these domains. Classical ML typically relies on stochastic, sample-separable objectives that favor first-order and adaptive gradient methods. In contrast, SciML often involves physics-informed or operator-constrained formulations in which differential operators induce global coupling, stiffness, and strong anisotropy in the loss landscape. As a result, optimization behavior in SciML is governed by the spectral properties of the underlying physical models rather than by data statistics, frequently limiting the effectiveness of standard stochastic methods and motivating deterministic or curvature-aware approaches. This document provides a unified introduction to optimization methods in ML and SciML, emphasizing how problem structure shapes algorithmic choices. We review first- and second-order optimization techniques in both deterministic and stochastic settings, discuss their adaptation to physics-constrained and data-driven SciML models, and illustrate practical strategies through tutorial examples, while highlighting open research directions at the interface of scientific computing and scientific machine learning.

