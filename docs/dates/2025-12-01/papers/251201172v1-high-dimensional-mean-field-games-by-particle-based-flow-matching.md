---
layout: default
title: High-dimensional Mean-Field Games by Particle-based Flow Matching
---

# High-dimensional Mean-Field Games by Particle-based Flow Matching
**arXiv**：[2512.01172v1](https://arxiv.org/abs/2512.01172) · [PDF](https://arxiv.org/pdf/2512.01172.pdf)  
**作者**：Jiajia Yu, Junghwan Lee, Yao Xie, Xiuyuan Cheng  

**一句话要点**：提出基于粒子的流匹配方法以解决高维平均场博弈的计算挑战

**关键词**：平均场博弈, 流匹配, 高维计算, 最优传输, 生成模型, 粒子方法

## 3 点简述
- 核心问题：高维平均场博弈因计算和分析障碍难以求解，影响其在最优传输和生成模型等应用。
- 方法要点：采用近端定点方案，结合粒子更新和流神经网络训练，在无模拟方式下匹配轨迹速度。
- 实验或效果：在非势能平均场博弈和高维最优传输问题中表现良好，理论证明在凸性假设下收敛性提升。

## 摘要（原文）

> Mean-field games (MFGs) study the Nash equilibrium of systems with a continuum of interacting agents, which can be formulated as the fixed-point of optimal control problems. They provide a unified framework for a variety of applications, including optimal transport (OT) and generative models. Despite their broad applicability, solving high-dimensional MFGs remains a significant challenge due to fundamental computational and analytical obstacles. In this work, we propose a particle-based deep Flow Matching (FM) method to tackle high-dimensional MFG computation. In each iteration of our proximal fixed-point scheme, particles are updated using first-order information, and a flow neural network is trained to match the velocity of the sample trajectories in a simulation-free manner. Theoretically, in the optimal control setting, we prove that our scheme converges to a stationary point sublinearly, and upgrade to linear (exponential) convergence under additional convexity assumptions. Our proof uses FM to induce an Eulerian coordinate (density-based) from a Lagrangian one (particle-based), and this also leads to certain equivalence results between the two formulations for MFGs when the Eulerian solution is sufficiently regular. Our method demonstrates promising performance on non-potential MFGs and high-dimensional OT problems cast as MFGs through a relaxed terminal-cost formulation.

