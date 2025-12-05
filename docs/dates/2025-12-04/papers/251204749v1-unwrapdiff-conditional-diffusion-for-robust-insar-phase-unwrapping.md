---
layout: default
title: UnwrapDiff: Conditional Diffusion for Robust InSAR Phase Unwrapping
---

# UnwrapDiff: Conditional Diffusion for Robust InSAR Phase Unwrapping
**arXiv**：[2512.04749v1](https://arxiv.org/abs/2512.04749) · [PDF](https://arxiv.org/pdf/2512.04749.pdf)  
**作者**：Yijia Song, Juliet Biggs, Alin Achim, Robert Popescu, Simon Orrego, Nantheera Anantrasirichai  

**一句话要点**：提出UnwrapDiff，基于条件扩散模型以增强InSAR相位解缠的鲁棒性。

**关键词**：InSAR相位解缠, 条件扩散模型, 去噪扩散概率模型, 最小成本流算法, 合成数据集, 变形监测

## 3 点简述
- 核心问题：InSAR相位解缠受噪声和失相关影响，导致变形信号重建困难。
- 方法要点：结合传统最小成本流算法输出作为条件引导，采用去噪扩散概率模型框架。
- 实验或效果：在合成数据集上平均降低NRMSE 10.11%，在困难案例如岩脉侵入中表现更优。

## 摘要（原文）

> Phase unwrapping is a fundamental problem in InSAR data processing, supporting geophysical applications such as deformation monitoring and hazard assessment. Its reliability is limited by noise and decorrelation in radar acquisitions, which makes accurate reconstruction of the deformation signal challenging. We propose a denoising diffusion probabilistic model (DDPM)-based framework for InSAR phase unwrapping, UnwrapDiff, in which the output of the traditional minimum cost flow algorithm (SNAPHU) is incorporated as conditional guidance. To evaluate robustness, we construct a synthetic dataset that incorporates atmospheric effects and diverse noise patterns, representative of realistic InSAR observations. Experiments show that the proposed model leverages the conditional prior while reducing the effect of diverse noise patterns, achieving on average a 10.11\% reduction in NRMSE compared to SNAPHU. It also achieves better reconstruction quality in difficult cases such as dyke intrusions.

