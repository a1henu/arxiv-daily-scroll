---
layout: default
title: Direct transfer of optimized controllers to similar systems using dimensionless MPC
---

# Direct transfer of optimized controllers to similar systems using dimensionless MPC
**arXiv**：[2512.08667v1](https://arxiv.org/abs/2512.08667) · [PDF](https://arxiv.org/pdf/2512.08667.pdf)  
**作者**：Josip Kir Hromatko, Shambhuraj Sawant, Šandor Ileš, Sébastien Gros  

**一句话要点**：提出基于无量纲模型预测控制的直接控制器迁移方法，以解决相似系统间控制器转移需额外调优的问题。

**关键词**：无量纲模型预测控制, 控制器迁移, 动态相似性, 参数优化, 缩比实验

## 3 点简述
- 核心问题：缩比模型实验中控制器迁移至全尺寸系统常需额外调优，增加成本与复杂性。
- 方法要点：通过无量纲模型预测控制，实现优化控制器在动态相似系统间的直接迁移，并支持多尺度数据用于参数优化。
- 实验或效果：在倒立摆起摆和赛车控制问题中，结合强化学习或贝叶斯优化调参，验证了方法的有效性。

## 摘要（原文）

> Scaled model experiments are commonly used in various engineering fields to reduce experimentation costs and overcome constraints associated with full-scale systems. The relevance of such experiments relies on dimensional analysis and the principle of dynamic similarity. However, transferring controllers to full-scale systems often requires additional tuning. In this paper, we propose a method to enable a direct controller transfer using dimensionless model predictive control, tuned automatically for closed-loop performance. With this reformulation, the closed-loop behavior of an optimized controller transfers directly to a new, dynamically similar system. Additionally, the dimensionless formulation allows for the use of data from systems of different scales during parameter optimization. We demonstrate the method on a cartpole swing-up and a car racing problem, applying either reinforcement learning or Bayesian optimization for tuning the controller parameters. Software used to obtain the results in this paper is publicly available at https://github.com/josipkh/dimensionless-mpcrl.

