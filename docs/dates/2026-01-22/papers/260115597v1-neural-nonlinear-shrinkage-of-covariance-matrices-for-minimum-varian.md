---
layout: default
title: Neural Nonlinear Shrinkage of Covariance Matrices for Minimum Variance Portfolio Optimization
---

# Neural Nonlinear Shrinkage of Covariance Matrices for Minimum Variance Portfolio Optimization
**arXiv**：[2601.15597v1](https://arxiv.org/abs/2601.15597) · [PDF](https://arxiv.org/pdf/2601.15597.pdf)  
**作者**：Liusha Yang, Siqi Zhao, Shuqi Chai  

**一句话要点**：提出基于神经网络的非线性协方差矩阵收缩估计器，用于最小方差投资组合优化。

**关键词**：协方差矩阵估计, 非线性收缩, 最小方差投资组合, 神经网络, Transformer, 投资组合优化

## 3 点简述
- 核心问题：传统协方差矩阵估计在最小方差投资组合优化中可能不准确，影响风险控制。
- 方法要点：结合Ledoit-Wolf收缩估计与轻量级Transformer网络，学习非线性特征值收缩函数，以投资组合风险为损失函数训练。
- 实验或效果：在S&P500股票日收益数据上实证，相比基准方法，该方法能持续降低样本外实现风险。

## 摘要（原文）

> This paper introduces a neural network-based nonlinear shrinkage estimator of covariance matrices for the purpose of minimum variance portfolio optimization. It is a hybrid approach that integrates statistical estimation with machine learning. Starting from the Ledoit-Wolf (LW) shrinkage estimator, we decompose the LW covariance matrix into its eigenvalues and eigenvectors, and apply a lightweight transformer-based neural network to learn a nonlinear eigenvalue shrinkage function. Trained with portfolio risk as the loss function, the resulting precision matrix (the inverse covariance matrix) estimator directly targets portfolio risk minimization. By conditioning on the sample-to-dimension ratio, the approach remains scalable across different sample sizes and asset universes. Empirical results on stock daily returns from Standard & Poor's 500 Index (S&P500) demonstrate that the proposed method consistently achieves lower out-of-sample realized risk than benchmark approaches. This highlights the promise of integrating structural statistical models with data-driven learning.

