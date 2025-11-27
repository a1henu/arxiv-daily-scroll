---
layout: default
title: SUPN: Shallow Universal Polynomial Networks
---

# SUPN: Shallow Universal Polynomial Networks
**arXiv**：[2511.21414v1](https://arxiv.org/abs/2511.21414) · [PDF](https://arxiv.org/pdf/2511.21414.pdf)  
**作者**：Zachary Morrow, Michael Penwarden, Brian Chen, Aurya Javeed, Akil Narayan, John D. Jakeman  

**一句话要点**：提出浅层通用多项式网络以降低函数逼近的参数需求

**关键词**：函数逼近, 多项式网络, 参数优化, 浅层网络, 数值实验

## 3 点简述
- 深度网络和KANs参数过多，导致优化困难和泛化误差不稳定
- 用单层可学习多项式替换隐藏层，结合深度网络与多项式优势
- 实验显示SUPNs在参数相同下误差和变异性低于DNNs和KANs

## 摘要（原文）

> Deep neural networks (DNNs) and Kolmogorov-Arnold networks (KANs) are popular methods for function approximation due to their flexibility and expressivity. However, they typically require a large number of trainable parameters to produce a suitable approximation. Beyond making the resulting network less transparent, overparameterization creates a large optimization space, likely producing local minima in training that have quite different generalization errors. In this case, network initialization can have an outsize impact on the model's out-of-sample accuracy. For these reasons, we propose shallow universal polynomial networks (SUPNs). These networks replace all but the last hidden layer with a single layer of polynomials with learnable coefficients, leveraging the strengths of DNNs and polynomials to achieve sufficient expressivity with far fewer parameters. We prove that SUPNs converge at the same rate as the best polynomial approximation of the same degree, and we derive explicit formulas for quasi-optimal SUPN parameters. We complement theory with an extensive suite of numerical experiments involving SUPNs, DNNs, KANs, and polynomial projection in one, two, and ten dimensions, consisting of over 13,000 trained models. On the target functions we numerically studied, for a given number of trainable parameters, the approximation error and variability are often lower for SUPNs than for DNNs and KANs by an order of magnitude. In our examples, SUPNs even outperform polynomial projection on non-smooth functions.

