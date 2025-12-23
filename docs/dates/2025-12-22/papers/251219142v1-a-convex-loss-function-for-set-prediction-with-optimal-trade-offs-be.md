---
layout: default
title: A Convex Loss Function for Set Prediction with Optimal Trade-offs Between Size and Conditional Coverage
---

# A Convex Loss Function for Set Prediction with Optimal Trade-offs Between Size and Conditional Coverage
**arXiv**：[2512.19142v1](https://arxiv.org/abs/2512.19142) · [PDF](https://arxiv.org/pdf/2512.19142.pdf)  
**作者**：Francis Bach  

**一句话要点**：提出基于Choquet积分的凸损失函数，优化集合预测中条件覆盖与大小的权衡。

**关键词**：集合预测, 条件覆盖, 凸损失函数, Choquet积分, 子模优化, 监督学习

## 3 点简述
- 核心问题：监督学习中集合预测需平衡条件概率覆盖与集合大小，传统方法侧重边际覆盖。
- 方法要点：利用Choquet积分构建凸损失函数，支持非递减子模函数度量大小，实现最优权衡。
- 实验或效果：在合成数据集上验证，分类和回归任务中优于追求边际覆盖的方法。

## 摘要（原文）

> We consider supervised learning problems in which set predictions provide explicit uncertainty estimates. Using Choquet integrals (a.k.a. Lov{á}sz extensions), we propose a convex loss function for nondecreasing subset-valued functions obtained as level sets of a real-valued function. This loss function allows optimal trade-offs between conditional probabilistic coverage and the ''size'' of the set, measured by a non-decreasing submodular function. We also propose several extensions that mimic loss functions and criteria for binary classification with asymmetric losses, and show how to naturally obtain sets with optimized conditional coverage. We derive efficient optimization algorithms, either based on stochastic gradient descent or reweighted least-squares formulations, and illustrate our findings with a series of experiments on synthetic datasets for classification and regression tasks, showing improvements over approaches that aim for marginal coverage.

