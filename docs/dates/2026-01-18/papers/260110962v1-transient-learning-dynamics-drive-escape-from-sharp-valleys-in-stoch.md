---
layout: default
title: Transient learning dynamics drive escape from sharp valleys in Stochastic Gradient Descent
---

# Transient learning dynamics drive escape from sharp valleys in Stochastic Gradient Descent
**arXiv**：[2601.10962v1](https://arxiv.org/abs/2601.10962) · [PDF](https://arxiv.org/pdf/2601.10962.pdf)  
**作者**：Ning Yang, Yikuan Zhang, Qi Ouyang, Chao Tang, Yuhai Tu  

**一句话要点**：揭示SGD通过瞬态学习动力学逃离尖锐谷并偏好平坦解的物理机制

**关键词**：随机梯度下降, 学习动力学, 损失景观, 泛化能力, 非平衡机制, 优化算法

## 3 点简述
- 核心问题：SGD为何偏好平坦解以提升泛化能力，其动力学起源不明
- 方法要点：分析SGD学习动力学，提出非平衡机制和有效势能模型解释解选择
- 实验或效果：数值实验显示瞬态探索相和冻结机制，噪声增强延迟冻结促进平坦最小化

## 摘要（原文）

> Stochastic gradient descent (SGD) is central to deep learning, yet the dynamical origin of its preference for flatter, more generalizable solutions remains unclear. Here, by analyzing SGD learning dynamics, we identify a nonequilibrium mechanism governing solution selection. Numerical experiments reveal a transient exploratory phase in which SGD trajectories repeatedly escape sharp valleys and transition toward flatter regions of the loss landscape. By using a tractable physical model, we show that the SGD noise reshapes the landscape into an effective potential that favors flat solutions. Crucially, we uncover a transient freezing mechanism: as training proceeds, growing energy barriers suppress inter-valley transitions and ultimately trap the dynamics within a single basin. Increasing the SGD noise strength delays this freezing, which enhances convergence to flatter minima. Together, these results provide a unified physical framework linking learning dynamics, loss-landscape geometry, and generalization, and suggest principles for the design of more effective optimization algorithms.

