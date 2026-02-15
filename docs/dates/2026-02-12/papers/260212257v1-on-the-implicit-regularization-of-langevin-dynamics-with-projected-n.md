---
layout: default
title: On the implicit regularization of Langevin dynamics with projected noise
---

# On the implicit regularization of Langevin dynamics with projected noise
**arXiv**：[2602.12257v1](https://arxiv.org/abs/2602.12257) · [PDF](https://arxiv.org/pdf/2602.12257.pdf)  
**作者**：Govind Menon, Austin J. Stromme, Adrien Vacher  

**一句话要点**：提出投影噪声朗之万动力学，揭示对称性在过参数化模型中的隐式正则化效应

**关键词**：朗之万动力学, 隐式正则化, 对称性, 随机梯度下降, 过参数化模型, 投影噪声

## 3 点简述
- 研究对称性对过参数化模型随机梯度下降的影响
- 证明投影噪声朗之万动力学等价于带额外漂移项的朗之万动力学
- 额外漂移项与群轨道体积负对数成正比，解释为轨道平均曲率

## 摘要（原文）

> We study Langevin dynamics with noise projected onto the directions orthogonal to an isometric group action. This mathematical model is introduced to shed new light on the effects of symmetry on stochastic gradient descent for over-parametrized models. Our main result identifies a novel form of implicit regularization: when the initial and target density are both invariant under the group action, Langevin dynamics with projected noise is equivalent in law to Langevin dynamics with isotropic diffusion but with an additional drift term proportional to the negative log volume of the group orbit. We prove this result by constructing a coupling of the two processes via a third process on the group itself, and identify the additional drift as the mean curvature of the orbits.

