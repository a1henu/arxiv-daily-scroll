---
layout: default
title: Adaptive Methods Are Preferable in High Privacy Settings: An SDE Perspective
---

# Adaptive Methods Are Preferable in High Privacy Settings: An SDE Perspective
**arXiv**：[2603.03226v1](https://arxiv.org/abs/2603.03226) · [PDF](https://arxiv.org/pdf/2603.03226.pdf)  
**作者**：Enea Monzio Compagnoni, Alessandro Stanghellini, Rustem Islamov, Aurelien Lucchi, Anastasiia Koloskova  

**一句话要点**：通过SDE分析揭示自适应方法在高隐私设置下的优势，优化DP-SGD与DP-SignSGD的隐私-效用权衡。

**关键词**：差分隐私优化, 随机微分方程分析, 自适应方法, 隐私-效用权衡, DP-SGD, DP-SignSGD

## 3 点简述
- 核心问题：差分隐私噪声与优化自适应性的交互，影响隐私-效用权衡。
- 方法要点：基于随机微分方程分析DP-SGD和DP-SignSGD，对比固定超参数与最优学习率下的性能。
- 实验或效果：实证验证自适应方法（如DP-SignSGD和DP-Adam）在高隐私或大噪声场景下更实用，超参数无需重调。

## 摘要（原文）

> Differential Privacy (DP) is becoming central to large-scale training as privacy regulations tighten. We revisit how DP noise interacts with adaptivity in optimization through the lens of stochastic differential equations, providing the first SDE-based analysis of private optimizers. Focusing on DP-SGD and DP-SignSGD under per-example clipping, we show a sharp contrast under fixed hyperparameters: DP-SGD converges at a Privacy-Utility Trade-Off of $\mathcal{O}(1/\varepsilon^2)$ with speed independent of $\varepsilon$, while DP-SignSGD converges at a speed linear in $\varepsilon$ with an $\mathcal{O}(1/\varepsilon)$ trade-off, dominating in high-privacy or large batch noise regimes. By contrast, under optimal learning rates, both methods achieve comparable theoretical asymptotic performance; however, the optimal learning rate of DP-SGD scales linearly with $\varepsilon$, while that of DP-SignSGD is essentially $\varepsilon$-independent. This makes adaptive methods far more practical, as their hyperparameters transfer across privacy levels with little or no re-tuning. Empirical results confirm our theory across training and test metrics, and empirically extend from DP-SignSGD to DP-Adam.

