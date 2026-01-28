---
layout: default
title: E-QRGMM: Efficient Generative Metamodeling for Covariate-Dependent Uncertainty Quantification
---

# E-QRGMM: Efficient Generative Metamodeling for Covariate-Dependent Uncertainty Quantification
**arXiv**：[2601.19256v1](https://arxiv.org/abs/2601.19256) · [PDF](https://arxiv.org/pdf/2601.19256.pdf)  
**作者**：Zhiyang Liang, Qingkai Zhang  

**一句话要点**：提出E-QRGMM以加速协变量依赖不确定性量化，通过立方埃尔米特插值与梯度估计提升计算效率。

**关键词**：不确定性量化, 生成模型, 协变量依赖, 分位数回归, 计算效率, 自助法

## 3 点简述
- 核心问题：现有方法如保形预测和经典自助法在协变量特定条件下处理不确定性量化时存在局限性。
- 方法要点：集成立方埃尔米特插值与梯度估计，将网格复杂度从O(n^{1/2})降至O(n^{1/5})，保持收敛率。
- 实验或效果：在合成和实际数据集上，E-QRGMM在分布准确性和训练速度间实现优于QRGMM和其他深度生成模型的权衡。

## 摘要（原文）

> Covariate-dependent uncertainty quantification in simulation-based inference is crucial for high-stakes decision-making but remains challenging due to the limitations of existing methods such as conformal prediction and classical bootstrap, which struggle with covariate-specific conditioning. We propose Efficient Quantile-Regression-Based Generative Metamodeling (E-QRGMM), a novel framework that accelerates the quantile-regression-based generative metamodeling (QRGMM) approach by integrating cubic Hermite interpolation with gradient estimation. Theoretically, we show that E-QRGMM preserves the convergence rate of the original QRGMM while reducing grid complexity from $O(n^{1/2})$ to $O(n^{1/5})$ for the majority of quantile levels, thereby substantially improving computational efficiency. Empirically, E-QRGMM achieves a superior trade-off between distributional accuracy and training speed compared to both QRGMM and other advanced deep generative models on synthetic and practical datasets. Moreover, by enabling bootstrap-based construction of confidence intervals for arbitrary estimands of interest, E-QRGMM provides a practical solution for covariate-dependent uncertainty quantification.

