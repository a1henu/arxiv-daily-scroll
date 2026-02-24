---
layout: default
title: Dirichlet Scale Mixture Priors for Bayesian Neural Networks
---

# Dirichlet Scale Mixture Priors for Bayesian Neural Networks
**arXiv**：[2602.19859v1](https://arxiv.org/abs/2602.19859) · [PDF](https://arxiv.org/pdf/2602.19859.pdf)  
**作者**：August Arnstad, Leiv Rønneberg, Geir Storvik  

**一句话要点**：提出Dirichlet尺度混合先验以提升贝叶斯神经网络在稀疏性和鲁棒性方面的性能

**关键词**：贝叶斯神经网络, 先验分布, 稀疏性, 鲁棒性, 冷后验效应, 特征选择

## 3 点简述
- 贝叶斯神经网络中先验分布指定困难，常被忽略，影响模型解释性和鲁棒性
- 引入Dirichlet尺度混合先验，通过结构化稀疏诱导收缩，促进网络稀疏化和特征选择
- 实验显示该先验在相关小数据场景下提升预测性能、对抗攻击鲁棒性，并缓解冷后验效应

## 摘要（原文）

> Neural networks are the cornerstone of modern machine learning, yet can be difficult to interpret, give overconfident predictions and are vulnerable to adversarial attacks. Bayesian neural networks (BNNs) provide some alleviation of these limitations, but have problems of their own. The key step of specifying prior distributions in BNNs is no trivial task, yet is often skipped out of convenience. In this work, we propose a new class of prior distributions for BNNs, the Dirichlet scale mixture (DSM) prior, that addresses current limitations in Bayesian neural networks through structured, sparsity-inducing shrinkage. Theoretically, we derive general dependence structures and shrinkage results for DSM priors and show how they manifest under the geometry induced by neural networks. In experiments on simulated and real world data we find that the DSM priors encourages sparse networks through implicit feature selection, show robustness under adversarial attacks and deliver competitive predictive performance with substantially fewer effective parameters. In particular, their advantages appear most pronounced in correlated, moderately small data regimes, and are more amenable to weight pruning. Moreover, by adopting heavy-tailed shrinkage mechanisms, our approach aligns with recent findings that such priors can mitigate the cold posterior effect, offering a principled alternative to the commonly used Gaussian priors.

