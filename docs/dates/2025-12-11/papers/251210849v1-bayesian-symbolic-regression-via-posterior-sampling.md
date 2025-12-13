---
layout: default
title: Bayesian Symbolic Regression via Posterior Sampling
---

# Bayesian Symbolic Regression via Posterior Sampling
**arXiv**：[2512.10849v1](https://arxiv.org/abs/2512.10849) · [PDF](https://arxiv.org/pdf/2512.10849.pdf)  
**作者**：Geoffrey F. Bomarito, Patrick E. Leser  

**一句话要点**：提出基于序贯蒙特卡洛的贝叶斯符号回归框架，以增强噪声数据下的鲁棒性和不确定性量化能力。

**关键词**：贝叶斯符号回归, 序贯蒙特卡洛, 不确定性量化, 噪声鲁棒性, 符号表达式搜索

## 3 点简述
- 核心问题：符号回归对噪声敏感，限制了其在数据驱动方程发现中的广泛应用。
- 方法要点：采用序贯蒙特卡洛近似符号表达式的后验分布，结合概率选择、自适应退火和归一化边际似然高效搜索。
- 实验或效果：相比传统遗传编程，该方法在噪声基准数据集上表现更优，减少过拟合，提升泛化能力和可解释性。

## 摘要（原文）

> Symbolic regression is a powerful tool for discovering governing equations directly from data, but its sensitivity to noise hinders its broader application. This paper introduces a Sequential Monte Carlo (SMC) framework for Bayesian symbolic regression that approximates the posterior distribution over symbolic expressions, enhancing robustness and enabling uncertainty quantification for symbolic regression in the presence of noise. Differing from traditional genetic programming approaches, the SMC-based algorithm combines probabilistic selection, adaptive tempering, and the use of normalized marginal likelihood to efficiently explore the search space of symbolic expressions, yielding parsimonious expressions with improved generalization. When compared to standard genetic programming baselines, the proposed method better deals with challenging, noisy benchmark datasets. The reduced tendency to overfit and enhanced ability to discover accurate and interpretable equations paves the way for more robust symbolic regression in scientific discovery and engineering design applications.

