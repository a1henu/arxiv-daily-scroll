---
layout: default
title: Linear Regression with Unknown Truncation Beyond Gaussian Features
---

# Linear Regression with Unknown Truncation Beyond Gaussian Features
**arXiv**：[2602.12534v1](https://arxiv.org/abs/2602.12534) · [PDF](https://arxiv.org/pdf/2602.12534.pdf)  
**作者**：Alexandros Kouridakis, Anay Mehrotra, Alkis Kalavasis, Constantine Caramanis  

**一句话要点**：提出高效算法解决特征向量仅需亚高斯分布下的未知截断线性回归问题

**关键词**：截断线性回归, 未知生存集, 亚高斯特征, 正例学习, 多项式时间算法

## 3 点简述
- 核心问题：截断线性回归中生存集未知且需从数据学习，现有方法依赖强分布假设或计算效率低
- 方法要点：基于正例学习有界区间并集的新子程序，实现多项式时间算法，仅要求特征向量亚高斯分布
- 实验或效果：算法在多项式时间内达到ε精度，突破先前指数级运行时间限制

## 摘要（原文）

> In truncated linear regression, samples $(x,y)$ are shown only when the outcome $y$ falls inside a certain survival set $S^\star$ and the goal is to estimate the unknown $d$-dimensional regressor $w^\star$. This problem has a long history of study in Statistics and Machine Learning going back to the works of (Galton, 1897; Tobin, 1958) and more recently in, e.g., (Daskalakis et al., 2019; 2021; Lee et al., 2023; 2024). Despite this long history, however, most prior works are limited to the special case where $S^\star$ is precisely known. The more practically relevant case, where $S^\star$ is unknown and must be learned from data, remains open: indeed, here the only available algorithms require strong assumptions on the distribution of the feature vectors (e.g., Gaussianity) and, even then, have a $d^{\mathrm{poly} (1/\varepsilon)}$ run time for achieving $\varepsilon$ accuracy.
>   In this work, we give the first algorithm for truncated linear regression with unknown survival set that runs in $\mathrm{poly} (d/\varepsilon)$ time, by only requiring that the feature vectors are sub-Gaussian. Our algorithm relies on a novel subroutine for efficiently learning unions of a bounded number of intervals using access to positive examples (without any negative examples) under a certain smoothness condition. This learning guarantee adds to the line of works on positive-only PAC learning and may be of independent interest.

