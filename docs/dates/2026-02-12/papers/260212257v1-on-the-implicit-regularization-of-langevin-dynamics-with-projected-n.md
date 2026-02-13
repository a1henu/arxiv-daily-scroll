---
layout: default
title: On the implicit regularization of Langevin dynamics with projected noise
---

# On the implicit regularization of Langevin dynamics with projected noise
**arXiv**：[2602.12257v1](https://arxiv.org/abs/2602.12257) · [PDF](https://arxiv.org/pdf/2602.12257.pdf)  
**作者**：Govind Menon, Austin J. Stromme, Adrien Vacher  

**一句话要点**：研究投影噪声朗之万动力学，揭示对称性在过参数化模型中的隐式正则化效应。

**关键词**：朗之万动力学, 隐式正则化, 对称性, 随机梯度下降, 过参数化模型, 群作用

## 3 点简述
- 核心问题：对称性如何影响过参数化模型的随机梯度下降优化过程。
- 方法要点：分析噪声投影到等距群作用正交方向的朗之万动力学模型。
- 实验或效果：证明投影噪声动力学等价于各向同性扩散加额外漂移项，该漂移与群轨道体积负对数成正比。

## 摘要（原文）

> We study Langevin dynamics with noise projected onto the directions orthogonal to an isometric group action. This mathematical model is introduced to shed new light on the effects of symmetry on stochastic gradient descent for over-parametrized models. Our main result identifies a novel form of implicit regularization: when the initial and target density are both invariant under the group action, Langevin dynamics with projected noise is equivalent in law to Langevin dynamics with isotropic diffusion but with an additional drift term proportional to the negative log volume of the group orbit. We prove this result by constructing a coupling of the two processes via a third process on the group itself, and identify the additional drift as the mean curvature of the orbits.

