---
layout: default
title: The geometry of invariant learning: an information-theoretic analysis of data augmentation and generalization
---

# The geometry of invariant learning: an information-theoretic analysis of data augmentation and generalization
**arXiv**：[2602.14423v1](https://arxiv.org/abs/2602.14423) · [PDF](https://arxiv.org/pdf/2602.14423.pdf)  
**作者**：Abdelali Bouyahia, Frédéric LeBlanc, Mario Marchand  

**一句话要点**：提出信息论框架分析数据增强对泛化和不变性学习的影响

**关键词**：数据增强, 泛化理论, 信息论分析, 不变性学习, 几何分析

## 3 点简述
- 核心问题：数据增强的理论作用未完全理解，需系统分析其对泛化的影响
- 方法要点：基于互信息界，建模增强分布，推导分解为三项的泛化界
- 实验或效果：数值实验验证理论界能可靠追踪和预测真实泛化差距

## 摘要（原文）

> Data augmentation is one of the most widely used techniques to improve generalization in modern machine learning, often justified by its ability to promote invariance to label-irrelevant transformations. However, its theoretical role remains only partially understood. In this work, we propose an information-theoretic framework that systematically accounts for the effect of augmentation on generalization and invariance learning. Our approach builds upon mutual information-based bounds, which relate the generalization gap to the amount of information a learning algorithm retains about its training data. We extend this framework by modeling the augmented distribution as a composition of the original data distribution with a distribution over transformations, which naturally induces an orbit-averaged loss function. Under mild sub-Gaussian assumptions on the loss function and the augmentation process, we derive a new generalization bound that decompose the expected generalization gap into three interpretable terms: (1) a distributional divergence between the original and augmented data, (2) a stability term measuring the algorithm dependence on training data, and (3) a sensitivity term capturing the effect of augmentation variability. To connect our bounds to the geometry of the augmentation group, we introduce the notion of group diameter, defined as the maximal perturbation that augmentations can induce in the input space. The group diameter provides a unified control parameter that bounds all three terms and highlights an intrinsic trade-off: small diameters preserve data fidelity but offer limited regularization, while large diameters enhance stability at the cost of increased bias and sensitivity. We validate our theoretical bounds with numerical experiments, demonstrating that it reliably tracks and predicts the behavior of the true generalization gap.

