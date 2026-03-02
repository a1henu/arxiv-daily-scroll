---
layout: default
title: A distributed semismooth Newton based augmented Lagrangian method for distributed optimization
---

# A distributed semismooth Newton based augmented Lagrangian method for distributed optimization
**arXiv**：[2602.23854v1](https://arxiv.org/abs/2602.23854) · [PDF](https://arxiv.org/pdf/2602.23854.pdf)  
**作者**：Qihao Ma, Chengjing Wang, Peipei Tang, Dunbiao Niu, Aimin Xu  

**一句话要点**：提出分布式半光滑牛顿增广拉格朗日方法以解决网络优化问题

**关键词**：分布式优化, 增广拉格朗日法, 半光滑牛顿法, 网络通信, 加速近端梯度法, 收敛分析

## 3 点简述
- 核心问题：网络优化中全局目标为局部成本函数和，通信限于相邻代理。
- 方法要点：采用增广拉格朗日法重构约束问题，子问题用分布式半光滑牛顿法近似求解。
- 实验或效果：理论保证收敛，数值实验显示优于现有分布式算法。

## 摘要（原文）

> This paper proposes a novel distributed semismooth Newton based augmented Lagrangian method for solving a class of optimization problems over networks, where the global objective is defined as the sum of locally held cost functions, and communication is restricted to neighboring agents. Specifically, we employ the augmented Lagrangian method to solve an equivalently reformulated constrained version of the original problem. Each resulting subproblem is solved inexactly via a distributed semismooth Newton method. By fully leveraging the structure of the generalized Hessian, a distributed accelerated proximal gradient method is proposed to compute the Newton direction efficiently, eliminating the need to communicate with full Hessian matrices. Theoretical results are also obtained to guarantee the convergence of the proposed algorithm. Numerical experiments demonstrate the efficiency and superiority of our algorithm compared to state-of-the-art distributed algorithms.

