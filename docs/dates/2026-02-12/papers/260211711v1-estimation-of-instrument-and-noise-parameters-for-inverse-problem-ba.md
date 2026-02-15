---
layout: default
title: Estimation of instrument and noise parameters for inverse problem based on prior diffusion model
---

# Estimation of instrument and noise parameters for inverse problem based on prior diffusion model
**arXiv**：[2602.11711v1](https://arxiv.org/abs/2602.11711) · [PDF](https://arxiv.org/pdf/2602.11711.pdf)  
**作者**：Jean-François Giovannelli  

**一句话要点**：提出基于扩散先验的贝叶斯逆问题观测参数估计方法

**关键词**：逆问题, 贝叶斯估计, 扩散模型, 观测参数估计, 不确定性量化, MCMC算法

## 3 点简述
- 核心问题：逆问题中观测参数（响应与误差）的估计，尤其在贝叶斯正则化框架下。
- 方法要点：利用扩散过程建模先验，通过后验采样策略灵活估计观测参数与目标图像。
- 实验或效果：数值实验验证了计算效率高，估计与不确定性量化质量优良。

## 摘要（原文）

> This article addresses the issue of estimating observation parameters (response and error parameters) in inverse problems. The focus is on cases where regularization is introduced in a Bayesian framework and the prior is modeled by a diffusion process. In this context, the issue of posterior sampling is well known to be thorny, and a recent paper proposes a notably simple and effective solution. Consequently, it offers an remarkable additional flexibility when it comes to estimating observation parameters. The proposed strategy enables us to define an optimal estimator for both the observation parameters and the image of interest. Furthermore, the strategy provides a means of quantifying uncertainty. In addition, MCMC algorithms allow for the efficient computation of estimates and properties of posteriors, while offering some guarantees. The paper presents several numerical experiments that clearly confirm the computational efficiency and the quality of both estimates and uncertainties quantification.

