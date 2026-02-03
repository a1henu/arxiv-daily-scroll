---
layout: default
title: Full-Batch Gradient Descent Outperforms One-Pass SGD: Sample Complexity Separation in Single-Index Learning
---

# Full-Batch Gradient Descent Outperforms One-Pass SGD: Sample Complexity Separation in Single-Index Learning
**arXiv**：[2602.02431v1](https://arxiv.org/abs/2602.02431) · [PDF](https://arxiv.org/pdf/2602.02431.pdf)  
**作者**：Filip Kovačević, Hong Chang Ji, Denny Wu, Mahdi Soltanolkotabi, Marco Mondelli  

**一句话要点**：证明全批次梯度下降在单索引学习中优于单次随机梯度下降，通过截断激活实现样本复杂度分离。

**关键词**：梯度下降, 单索引模型, 样本复杂度, 优化理论, 统计学习

## 3 点简述
- 研究全批次梯度下降与单次随机梯度下降在单索引模型学习中的统计效率差异。
- 通过截断激活函数，全批次梯度下降在约d个样本时展现有利优化景观，超越单次随机梯度下降。
- 轨迹分析表明，全批次梯度下降在平方损失上从初始化出发，约d个样本和对数步数可实现强恢复。

## 摘要（原文）

> It is folklore that reusing training data more than once can improve the statistical efficiency of gradient-based learning. However, beyond linear regression, the theoretical advantage of full-batch gradient descent (GD, which always reuses all the data) over one-pass stochastic gradient descent (online SGD, which uses each data point only once) remains unclear. In this work, we consider learning a $d$-dimensional single-index model with a quadratic activation, for which it is known that one-pass SGD requires $n\gtrsim d\log d$ samples to achieve weak recovery. We first show that this $\log d$ factor in the sample complexity persists for full-batch spherical GD on the correlation loss; however, by simply truncating the activation, full-batch GD exhibits a favorable optimization landscape at $n \simeq d$ samples, thereby outperforming one-pass SGD (with the same activation) in statistical efficiency. We complement this result with a trajectory analysis of full-batch GD on the squared loss from small initialization, showing that $n \gtrsim d$ samples and $T \gtrsim\log d$ gradient steps suffice to achieve strong (exact) recovery.

