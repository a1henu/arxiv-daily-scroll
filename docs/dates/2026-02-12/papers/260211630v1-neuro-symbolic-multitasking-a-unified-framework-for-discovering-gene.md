---
layout: default
title: Neuro-Symbolic Multitasking: A Unified Framework for Discovering Generalizable Solutions to PDE Families
---

# Neuro-Symbolic Multitasking: A Unified Framework for Discovering Generalizable Solutions to PDE Families
**arXiv**：[2602.11630v1](https://arxiv.org/abs/2602.11630) · [PDF](https://arxiv.org/pdf/2602.11630.pdf)  
**作者**：Yipeng Huang, Dejun Xu, Zexin Lin, Zhenzhong Wang, Min Jiang  

**一句话要点**：提出神经辅助多任务符号PDE求解框架NMIPS，以高效发现PDE族解析解

**关键词**：偏微分方程求解, 神经符号计算, 多任务优化, 解析解发现, 计算效率提升

## 3 点简述
- 核心问题：传统数值方法求解PDE族计算成本高，机器学习方法缺乏解析解的可解释性
- 方法要点：采用多因子优化同时发现PDE解析解，设计仿射转移方法在PDE族间传递数学结构
- 实验或效果：在多个案例中相比基线提升精度约35.7%，并提供可解释解析解

## 摘要（原文）

> Solving Partial Differential Equations (PDEs) is fundamental to numerous scientific and engineering disciplines. A common challenge arises from solving the PDE families, which are characterized by sharing an identical mathematical structure but varying in specific parameters. Traditional numerical methods, such as the finite element method, need to independently solve each instance within a PDE family, which incurs massive computational cost. On the other hand, while recent advancements in machine learning PDE solvers offer impressive computational speed and accuracy, their inherent ``black-box" nature presents a considerable limitation. These methods primarily yield numerical approximations, thereby lacking the crucial interpretability provided by analytical expressions, which are essential for deeper scientific insight. To address these limitations, we propose a neuro-assisted multitasking symbolic PDE solver framework for PDE family solving, dubbed NMIPS. In particular, we employ multifactorial optimization to simultaneously discover the analytical solutions of PDEs. To enhance computational efficiency, we devise an affine transfer method by transferring learned mathematical structures among PDEs in a family, avoiding solving each PDE from scratch. Experimental results across multiple cases demonstrate promising improvements over existing baselines, achieving up to a $\sim$35.7% increase in accuracy while providing interpretable analytical solutions.

