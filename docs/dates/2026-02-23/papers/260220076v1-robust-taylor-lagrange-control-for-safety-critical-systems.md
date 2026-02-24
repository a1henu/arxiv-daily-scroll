---
layout: default
title: Robust Taylor-Lagrange Control for Safety-Critical Systems
---

# Robust Taylor-Lagrange Control for Safety-Critical Systems
**arXiv**：[2602.20076v1](https://arxiv.org/abs/2602.20076) · [PDF](https://arxiv.org/pdf/2602.20076.pdf)  
**作者**：Wei Xiao, Christos Cassandras, Anni Li  

**一句话要点**：提出鲁棒泰勒-拉格朗日控制方法以解决安全关键系统中的可行性保持问题

**关键词**：安全关键控制, 控制屏障函数, 泰勒-拉格朗日控制, 可行性保持, 自适应巡航控制, 鲁棒控制

## 3 点简述
- 核心问题：泰勒-拉格朗日控制方法存在可行性保持问题，如采样间效应。
- 方法要点：使用高阶泰勒展开与拉格朗日余项，使控制量在当前时间显式出现，减少超参数。
- 实验或效果：通过自适应巡航控制问题验证有效性，并与现有方法比较。

## 摘要（原文）

> Solving safety-critical control problem has widely adopted the Control Barrier Function (CBF) method. However, the existence of a CBF is only a sufficient condition for system safety. The recently proposed Taylor-Lagrange Control (TLC) method addresses this limitation, but is vulnerable to the feasibility preservation problem (e.g., inter-sampling effect). In this paper, we propose a robust TLC (rTLC) method to address the feasibility preservation problem. Specifically, the rTLC method expands the safety function at an order higher than the relative degree of the function using Taylor's expansion with Lagrange remainder, which allows the control to explicitly show up at the current time instead of the future time in the TLC method. The rTLC method naturally addresses the feasibility preservation problem with only one hyper-parameter (the discretization time interval size during implementation), which is much less than its counterparts. Finally, we illustrate the effectiveness of the proposed rTLC method through an adaptive cruise control problem, and compare it with existing safety-critical control methods.

