---
layout: default
title: All ERMs Can Fail in Stochastic Convex Optimization Lower Bounds in Linear Dimension
---

# All ERMs Can Fail in Stochastic Convex Optimization Lower Bounds in Linear Dimension
**arXiv**：[2602.08350v1](https://arxiv.org/abs/2602.08350) · [PDF](https://arxiv.org/pdf/2602.08350.pdf)  
**作者**：Tal Burla, Roi Livni  

**一句话要点**：证明经验风险最小化器在样本量线性于维度时可能过拟合，并给出梯度下降泛化下界

**关键词**：随机凸优化, 经验风险最小化, 泛化下界, 梯度下降, 过拟合, 样本复杂度

## 3 点简述
- 研究随机凸优化中经验风险最小化器的样本复杂度，解决Feldman开放问题
- 构建实例显示样本量线性于维度时学习可行但ERM可能唯一且过拟合，扩展至近似ERM
- 基于构造给出梯度下降泛化下界Ω(√(ηT/m^1.5))，缩小与已知上界的指数级差距

## 摘要（原文）

> We study the sample complexity of the best-case Empirical Risk Minimizer in the setting of stochastic convex optimization. We show that there exists an instance in which the sample size is linear in the dimension, learning is possible, but the Empirical Risk Minimizer is likely to be unique and to overfit. This resolves an open question by Feldman. We also extend this to approximate ERMs.
>   Building on our construction we also show that (constrained) Gradient Descent potentially overfits when horizon and learning rate grow w.r.t sample size. Specifically we provide a novel generalization lower bound of $Ω\left(\sqrt{ηT/m^{1.5}}\right)$ for Gradient Descent, where $η$ is the learning rate, $T$ is the horizon and $m$ is the sample size. This narrows down, exponentially, the gap between the best known upper bound of $O(ηT/m)$ and existing lower bounds from previous constructions.

