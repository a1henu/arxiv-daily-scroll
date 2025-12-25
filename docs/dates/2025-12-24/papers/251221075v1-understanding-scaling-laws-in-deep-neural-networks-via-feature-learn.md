---
layout: default
title: Understanding Scaling Laws in Deep Neural Networks via Feature Learning Dynamics
---

# Understanding Scaling Laws in Deep Neural Networks via Feature Learning Dynamics
**arXiv**：[2512.21075v1](https://arxiv.org/abs/2512.21075) · [PDF](https://arxiv.org/pdf/2512.21075.pdf)  
**作者**：Zihan Yao, Ruoyu Wu, Tianxiang Gao  

**一句话要点**：提出神经特征动力学以解析深度残差网络中的缩放定律与特征学习机制

**关键词**：缩放定律, 特征学习, 残差网络, 无限深度极限, 超参数迁移, 学习率校正

## 3 点简述
- 核心问题：深度缩放定律缺乏理论解释，深度-muP在多层残差块中失效
- 方法要点：推导单层残差块的神经特征动力学，在无限宽深极限下分析特征学习
- 实验或效果：提出深度感知学习率校正，恢复超参数迁移并提升深度ResNet性能

## 摘要（原文）

> The empirical success of deep learning is often attributed to scaling laws that predict consistent gains as model, data, and compute grow; however, large models can exhibit training instability and diminishing returns, suggesting that scaling laws describe what success looks like but not when and why scaling succeeds or fails. A central obstacle is the lack of a rigorous understanding of feature learning at large depth. While muP characterizes feature-learning dynamics in the infinite-width limit and enables hyperparameter transfer across width, its depth extension (depth-muP) breaks down for residual blocks with more than one internal layer. We derive Neural Feature Dynamics (NFD) for ResNets with single-layer residual blocks, characterizing feature learning via a coupled forward-backward stochastic system in the joint infinite-width and infinite-depth limit. In this regime, NFD identifies when scaling-law trends persist and explains diminishing returns. It also reveals a vanishing mechanism induced by the 1/sqrt(depth) residual scaling under which the gradient-independence assumption (GIA), known to fail during training at finite depth, becomes provably valid again at infinite depth, yielding an analytically tractable regime for end-to-end feature learning. Motivated by this insight, we study two-layer residual blocks and show that the same mechanism causes feature-learning collapse in the first internal layer at large depth, providing a structural explanation for the empirical failure of depth-muP. Based on this diagnosis, we propose a depth-aware learning-rate correction that counteracts the collapse and empirically restores depth-wise hyperparameter transfer, yielding stronger performance in deeper ResNets.

