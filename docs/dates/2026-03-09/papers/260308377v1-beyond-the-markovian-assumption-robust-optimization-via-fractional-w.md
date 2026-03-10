---
layout: default
title: Beyond the Markovian Assumption: Robust Optimization via Fractional Weyl Integrals in Imbalanced Data
---

# Beyond the Markovian Assumption: Robust Optimization via Fractional Weyl Integrals in Imbalanced Data
**arXiv**：[2603.08377v1](https://arxiv.org/abs/2603.08377) · [PDF](https://arxiv.org/pdf/2603.08377.pdf)  
**作者**：Gustavo A. Dorrego  

**一句话要点**：提出基于分数阶Weyl积分的优化算法，以解决不平衡数据中的过拟合问题。

**关键词**：分数阶微积分, 不平衡数据, 优化算法, 过拟合, 金融欺诈检测, 医疗诊断

## 3 点简述
- 标准梯度下降及其变体依赖局部马尔可夫更新，易受噪声和过拟合影响，尤其在不平衡数据中。
- 利用分数阶微积分，通过加权分数阶Weyl积分替代瞬时梯度，引入动态历史加权序列作为正则化器。
- 实验表明，该方法在医疗诊断中防止过拟合，在金融欺诈检测中PR-AUC提升约40%。

## 摘要（原文）

> Standard Gradient Descent and its modern variants assume local, Markovian weight updates, making them highly susceptible to noise and overfitting. This limitation becomes critically severe in extremely imbalanced datasets such as financial fraud detection where dominant class gradients systematically overwrite the subtle signals of the minority class. In this paper, we introduce a novel optimization algorithm grounded in Fractional Calculus. By isolating the core memory engine of the generalized fractional derivative, the Weighted Fractional Weyl Integral, we replace the instantaneous gradient with a dynamically weighted historical sequence. This fractional memory operator acts as a natural regularizer. Empirical evaluations demonstrate that our method prevents overfitting in medical diagnostics and achieves an approximately 40 percent improvement in PR-AUC over classical optimizers in financial fraud detection, establishing a robust bridge between pure fractional topology and applied Machine Learning.

