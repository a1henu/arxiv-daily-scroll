---
layout: default
title: A Systems-Theoretic View on the Convergence of Algorithms under Disturbances
---

# A Systems-Theoretic View on the Convergence of Algorithms under Disturbances
**arXiv**：[2512.17598v1](https://arxiv.org/abs/2512.17598) · [PDF](https://arxiv.org/pdf/2512.17598.pdf)  
**作者**：Guner Dilsad Er, Sebastian Trimpe, Michael Muehlebach  

**一句话要点**：提出系统理论框架以分析算法在扰动下的收敛性

**关键词**：算法收敛性, 系统理论, 扰动分析, Lyapunov定理, 分布式学习, 隐私保护

## 3 点简述
- 核心问题：算法在复杂系统中受扰动影响，传统孤立分析不适用
- 方法要点：利用逆Lyapunov定理推导扰动下的稳定性界和收敛率
- 实验或效果：应用于分布式学习、机器学习泛化、隐私保护等场景

## 摘要（原文）

> Algorithms increasingly operate within complex physical, social, and engineering systems where they are exposed to disturbances, noise, and interconnections with other dynamical systems. This article extends known convergence guarantees of an algorithm operating in isolation (i.e., without disturbances) and systematically derives stability bounds and convergence rates in the presence of such disturbances. By leveraging converse Lyapunov theorems, we derive key inequalities that quantify the impact of disturbances. We further demonstrate how our result can be utilized to assess the effects of disturbances on algorithmic performance in a wide variety of applications, including communication constraints in distributed learning, sensitivity in machine learning generalization, and intentional noise injection for privacy. This underpins the role of our result as a unifying tool for algorithm analysis in the presence of noise, disturbances, and interconnections with other dynamical systems.

