---
layout: default
title: Functional Continuous Decomposition
---

# Functional Continuous Decomposition
**arXiv**：[2602.20857v1](https://arxiv.org/abs/2602.20857) · [PDF](https://arxiv.org/pdf/2602.20857.pdf)  
**作者**：Teymur Aghayev  

**一句话要点**：提出Functional Continuous Decomposition以解决非平稳时间序列分析的参数化连续优化问题。

**关键词**：时间序列分析, 参数优化, 连续分解, JAX加速, 特征提取, CNN增强

## 3 点简述
- 核心问题：传统平滑算法如B样条和EMD缺乏参数化优化和连续性保证。
- 方法要点：基于JAX加速，使用Levenberg-Marquardt优化实现C^1连续拟合，分解为M个模式。
- 实验或效果：在物理、医学等领域应用，平均SRMSE为0.735，CNN结合FCD特征提升收敛速度和准确率。

## 摘要（原文）

> The analysis of non-stationary time-series data requires insight into its local and global patterns with physical interpretability. However, traditional smoothing algorithms, such as B-splines, Savitzky-Golay filtering, and Empirical Mode Decomposition (EMD), lack the ability to perform parametric optimization with guaranteed continuity. In this paper, we propose Functional Continuous Decomposition (FCD), a JAX-accelerated framework that performs parametric, continuous optimization on a wide range of mathematical functions. By using Levenberg-Marquardt optimization to achieve up to $C^1$ continuous fitting, FCD transforms raw time-series data into $M$ modes that capture different temporal patterns from short-term to long-term trends. Applications of FCD include physics, medicine, financial analysis, and machine learning, where it is commonly used for the analysis of signal temporal patterns, optimized parameters, derivatives, and integrals of decomposition. Furthermore, FCD can be applied for physical analysis and feature extraction with an average SRMSE of 0.735 per segment and a speed of 0.47s on full decomposition of 1,000 points. Finally, we demonstrate that a Convolutional Neural Network (CNN) enhanced with FCD features, such as optimized function values, parameters, and derivatives, achieved 16.8% faster convergence and 2.5% higher accuracy over a standard CNN.

