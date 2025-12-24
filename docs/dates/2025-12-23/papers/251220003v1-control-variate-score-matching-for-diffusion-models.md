---
layout: default
title: Control Variate Score Matching for Diffusion Models
---

# Control Variate Score Matching for Diffusion Models
**arXiv**：[2512.20003v1](https://arxiv.org/abs/2512.20003) · [PDF](https://arxiv.org/pdf/2512.20003.pdf)  
**作者**：Khaled Kahouli, Romuald Elie, Klaus-Robert Müller, Quentin Berthet, Oliver T. Unke, Arnaud Doucet  

**一句话要点**：提出控制变量分数匹配以降低扩散模型分数估计方差

**关键词**：扩散模型, 分数匹配, 控制变量, 方差减少, 采样效率, 无数据学习

## 3 点简述
- 扩散模型分数估计存在方差权衡：DSI在低噪声方差高，TSI在高噪声方差高
- 通过控制变量框架统一DSI和TSI，推导最优时变系数实现全噪声谱方差最小化
- CVSI作为低方差插件估计器，提升无数据采样学习和推理时采样效率

## 摘要（原文）

> Diffusion models offer a robust framework for sampling from unnormalized probability densities, which requires accurately estimating the score of the noise-perturbed target distribution. While the standard Denoising Score Identity (DSI) relies on data samples, access to the target energy function enables an alternative formulation via the Target Score Identity (TSI). However, these estimators face a fundamental variance trade-off: DSI exhibits high variance in low-noise regimes, whereas TSI suffers from high variance at high noise levels. In this work, we reconcile these approaches by unifying both estimators within the principled framework of control variates. We introduce the Control Variate Score Identity (CVSI), deriving an optimal, time-dependent control coefficient that theoretically guarantees variance minimization across the entire noise spectrum. We demonstrate that CVSI serves as a robust, low-variance plug-in estimator that significantly enhances sample efficiency in both data-free sampler learning and inference-time diffusion sampling.

