---
layout: default
title: Generative and Nonparametric Approaches for Conditional Distribution Estimation: Methods, Perspectives, and Comparative Evaluations
---

# Generative and Nonparametric Approaches for Conditional Distribution Estimation: Methods, Perspectives, and Comparative Evaluations
**arXiv**：[2601.22650v1](https://arxiv.org/abs/2601.22650) · [PDF](https://arxiv.org/pdf/2601.22650.pdf)  
**作者**：Yen-Shiu Chin, Zhi-Yu Jou, Toshinari Morimoto, Chia-Tse Wang, Ming-Chung Chang, Tso-Jung Yen, Su-Yun Huang, Tailen Hsing  

**一句话要点**：综述并比较条件分布估计的生成与非参数方法，提供系统评估框架

**关键词**：条件分布估计, 非参数方法, 生成模型, 比较评估, 深度学习

## 3 点简述
- 核心问题：条件分布推断是统计学基础，用于预测和不确定性量化
- 方法要点：涵盖单指数法、基展开法和生成模型，如扩散模型
- 实验或效果：使用统一框架比较性能，包括均方误差和Wasserstein距离

## 摘要（原文）

> The inference of conditional distributions is a fundamental problem in statistics, essential for prediction, uncertainty quantification, and probabilistic modeling. A wide range of methodologies have been developed for this task. This article reviews and compares several representative approaches spanning classical nonparametric methods and modern generative models. We begin with the single-index method of Hall and Yao (2005), which estimates the conditional distribution through a dimension-reducing index and nonparametric smoothing of the resulting one-dimensional cumulative conditional distribution function. We then examine the basis-expansion approaches, including FlexCode (Izbicki and Lee, 2017) and DeepCDE (Dalmasso et al., 2020), which convert conditional density estimation into a set of nonparametric regression problems. In addition, we discuss two recent generative simulation-based methods that leverage modern deep generative architectures: the generative conditional distribution sampler (Zhou et al., 2023) and the conditional denoising diffusion probabilistic model (Fu et al., 2024; Yang et al., 2025). A systematic numerical comparison of these approaches is provided using a unified evaluation framework that ensures fairness and reproducibility. The performance metrics used for the estimated conditional distribution include the mean-squared errors of conditional mean and standard deviation, as well as the Wasserstein distance. We also discuss their flexibility and computational costs, highlighting the distinct advantages and limitations of each approach.

