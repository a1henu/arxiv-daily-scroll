---
layout: default
title: A Single-Loop Bilevel Deep Learning Method for Optimal Control of Obstacle Problems
---

# A Single-Loop Bilevel Deep Learning Method for Optimal Control of Obstacle Problems
**arXiv**：[2601.04120v1](https://arxiv.org/abs/2601.04120) · [PDF](https://arxiv.org/pdf/2601.04120.pdf)  
**作者**：Yongcun Song, Shangzhi Zeng, Jin Zhang, Lvgang Zhang  

**一句话要点**：提出单层双层深度学习法以解决障碍物问题的最优控制计算挑战

**关键词**：最优控制, 障碍物问题, 双层优化, 深度学习, 单层算法, 无网格方法

## 3 点简述
- 核心问题：障碍物问题最优控制因非光滑、非线性及双层结构而计算困难
- 方法要点：采用约束嵌入神经网络近似状态与控制，提出单层随机一阶双层算法消除嵌套优化
- 实验或效果：在复杂域上测试，相比传统方法在降低计算成本的同时保持满意精度

## 摘要（原文）

> Optimal control of obstacle problems arises in a wide range of applications and is computationally challenging due to its nonsmoothness, nonlinearity, and bilevel structure. Classical numerical approaches rely on mesh-based discretization and typically require solving a sequence of costly subproblems. In this work, we propose a single-loop bilevel deep learning method, which is mesh-free, scalable to high-dimensional and complex domains, and avoids repeated solution of discretized subproblems. The method employs constraint-embedding neural networks to approximate the state and control and preserves the bilevel structure. To train the neural networks efficiently, we propose a Single-Loop Stochastic First-Order Bilevel Algorithm (S2-FOBA), which eliminates nested optimization and does not rely on restrictive lower-level uniqueness assumptions. We analyze the convergence behavior of S2-FOBA under mild assumptions. Numerical experiments on benchmark examples, including distributed and obstacle control problems with regular and irregular obstacles on complex domains, demonstrate that the proposed method achieves satisfactory accuracy while reducing computational cost compared to classical numerical methods.

