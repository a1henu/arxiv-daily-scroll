---
layout: default
title: Solving Inverse PDE Problems using Minimization Methods and AI
---

# Solving Inverse PDE Problems using Minimization Methods and AI
**arXiv**：[2603.01731v1](https://arxiv.org/abs/2603.01731) · [PDF](https://arxiv.org/pdf/2603.01731.pdf)  
**作者**：Noura Helwani, Sophie Moufawad, Georges Sakr  

**一句话要点**：对比数值方法与PINN求解微分方程正反问题，验证其在复杂系统中的有效性

**关键词**：微分方程求解, 物理信息神经网络, 参数估计, 多孔介质方程, 数值方法

## 3 点简述
- 研究微分方程正反问题，对比传统数值方法与AI技术
- 使用逻辑方程验证PINN性能，并针对多孔介质方程构建求解器
- PINN能以竞争性计算成本准确估计解，适用于复杂系统

## 摘要（原文）

> Many physical and engineering systems require solving direct problems to predict behavior and inverse problems to determine unknown parameters from measurement. In this work, we study both aspects for systems governed by differential equations, contrasting well-established numerical methods with new AI-based techniques, specifically Physics-Informed Neural Networks (PINNs). We first analyze the logistic differential equation, using its closed-form solution to verify numerical schemes and validate PINN performance. We then address the Porous Medium Equation (PME), a nonlinear partial differential equation with no general closed-form solution, building strong solvers of the direct problem and testing techniques for parameter estimation in the inverse problem. Our results suggest that PINNs can closely estimate solutions at competitive computational cost, and thus propose an effective tool for solving both direct and inverse problems for complex systems.

