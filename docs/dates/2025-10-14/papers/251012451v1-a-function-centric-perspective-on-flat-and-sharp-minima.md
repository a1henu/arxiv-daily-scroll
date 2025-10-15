---
layout: default
title: A Function Centric Perspective On Flat and Sharp Minima
---

# A Function Centric Perspective On Flat and Sharp Minima
**arXiv**：[2510.12451v1](https://arxiv.org/abs/2510.12451) · [PDF](https://arxiv.org/pdf/2510.12451.pdf)  
**作者**：Israel Mason-Williams, Gabryel Mason-Williams, Helen Yannakoudakis  

**一句话要点**：提出函数中心视角，重新评估平坦与尖锐极小值在深度学习泛化中的作用。

**关键词**：深度学习泛化, 损失景观几何, 正则化方法, 尖锐极小值, 函数复杂度

## 3 点简述
- 核心问题：平坦极小值与泛化性能的关联在理论和实践中存在例外，需要更深入理解。
- 方法要点：将尖锐性视为函数依赖属性，通过正则化实验探索其对泛化的影响。
- 实验或效果：正则化下尖锐极小值常伴随更好泛化、校准、鲁棒性和功能一致性。

## 摘要（原文）

> Flat minima are widely believed to correlate with improved generalisation in
> deep neural networks. However, this connection has proven more nuanced in
> recent studies, with both theoretical counterexamples and empirical exceptions
> emerging in the literature. In this paper, we revisit the role of sharpness in
> model performance, proposing that sharpness is better understood as a
> function-dependent property rather than a reliable indicator of poor
> generalisation. We conduct extensive empirical studies, from single-objective
> optimisation to modern image classification tasks, showing that sharper minima
> often emerge when models are regularised (e.g., via SAM, weight decay, or data
> augmentation), and that these sharp minima can coincide with better
> generalisation, calibration, robustness, and functional consistency. Across a
> range of models and datasets, we find that baselines without regularisation
> tend to converge to flatter minima yet often perform worse across all safety
> metrics. Our findings demonstrate that function complexity, rather than
> flatness alone, governs the geometry of solutions, and that sharper minima can
> reflect more appropriate inductive biases (especially under regularisation),
> calling for a function-centric reappraisal of loss landscape geometry.

