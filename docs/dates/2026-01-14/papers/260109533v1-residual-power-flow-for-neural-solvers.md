---
layout: default
title: Residual Power Flow for Neural Solvers
---

# Residual Power Flow for Neural Solvers
**arXiv**：[2601.09533v1](https://arxiv.org/abs/2601.09533) · [PDF](https://arxiv.org/pdf/2601.09533.pdf)  
**作者**：Jochen Stiasny, Jochen Cremer  

**一句话要点**：提出残差潮流公式以提升神经求解器在电力系统任务中的灵活性与学习性能

**关键词**：残差潮流, 神经求解器, 电力系统优化, 预测-优化方法, 交流最优潮流

## 3 点简述
- 核心问题：神经求解器评估速度快但任务适应性差，限制实际应用，需可重用基础求解器。
- 方法要点：基于基尔霍夫定律构建残差函数量化运行条件不可行性，通过最小化残差求解电压，引入松弛变量实现交流可行性。
- 实验或效果：在IEEE 9总线系统上，结合预测-优化方法解决多种任务，验证了准确性和灵活性。

## 摘要（原文）

> The energy transition challenges operational tasks based on simulations and optimisation. These computations need to be fast and flexible as the grid is ever-expanding, and renewables' uncertainty requires a flexible operational environment. Learned approximations, proxies or surrogates -- we refer to them as Neural Solvers -- excel in terms of evaluation speed, but are inflexible with respect to adjusting to changing tasks. Hence, neural solvers are usually applicable to highly specific tasks, which limits their usefulness in practice; a widely reusable, foundational neural solver is required. Therefore, this work proposes the Residual Power Flow (RPF) formulation. RPF formulates residual functions based on Kirchhoff's laws to quantify the infeasibility of an operating condition. The minimisation of the residuals determines the voltage solution; an additional slack variable is needed to achieve AC-feasibility. RPF forms a natural, foundational subtask of tasks subject to power flow constraints. We propose to learn RPF with neural solvers to exploit their speed. Furthermore, RPF improves learning performance compared to common power flow formulations. To solve operational tasks, we integrate the neural solver in a Predict-then-Optimise (PO) approach to combine speed and flexibility. The case study investigates the IEEE 9-bus system and three tasks (AC Optimal Power Flow (OPF), power-flow and quasi-steady state power flow) solved by PO. The results demonstrate the accuracy and flexibility of learning with RPF.

