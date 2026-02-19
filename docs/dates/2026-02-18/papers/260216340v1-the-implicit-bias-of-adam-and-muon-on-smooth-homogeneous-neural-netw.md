---
layout: default
title: The Implicit Bias of Adam and Muon on Smooth Homogeneous Neural Networks
---

# The Implicit Bias of Adam and Muon on Smooth Homogeneous Neural Networks
**arXiv**：[2602.16340v1](https://arxiv.org/abs/2602.16340) · [PDF](https://arxiv.org/pdf/2602.16340.pdf)  
**作者**：Eitan Gronich, Gal Vardi  

**一句话要点**：分析动量优化器在平滑齐次神经网络中的隐式偏差，扩展至Adam等算法

**关键词**：隐式偏差, 动量优化器, 齐次模型, 最速下降, 边界最大化, Adam算法

## 3 点简述
- 研究动量优化器在齐次模型中的隐式偏差，扩展最速下降理论
- 证明Muon、MomentumGD等算法近似最速下降轨迹，偏向KKT点
- 实验验证优化器选择决定最大化边界的范数类型，支持理论分析

## 摘要（原文）

> We study the implicit bias of momentum-based optimizers on homogeneous models. We first extend existing results on the implicit bias of steepest descent in homogeneous models to normalized steepest descent with an optional learning rate schedule. We then show that for smooth homogeneous models, momentum steepest descent algorithms like Muon (spectral norm), MomentumGD ($\ell_2$ norm), and Signum ($\ell_\infty$ norm) are approximate steepest descent trajectories under a decaying learning rate schedule, proving that these algorithms too have a bias towards KKT points of the corresponding margin maximization problem. We extend the analysis to Adam (without the stability constant), which maximizes the $\ell_\infty$ margin, and to Muon-Signum and Muon-Adam, which maximize a hybrid norm. Our experiments corroborate the theory and show that the identity of the margin maximized depends on the choice of optimizer. Overall, our results extend earlier lines of work on steepest descent in homogeneous models and momentum-based optimizers in linear models.

