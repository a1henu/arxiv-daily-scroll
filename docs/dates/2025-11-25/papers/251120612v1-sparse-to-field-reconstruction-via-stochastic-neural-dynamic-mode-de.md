---
layout: default
title: Sparse-to-Field Reconstruction via Stochastic Neural Dynamic Mode Decomposition
---

# Sparse-to-Field Reconstruction via Stochastic Neural Dynamic Mode Decomposition
**arXiv**：[2511.20612v1](https://arxiv.org/abs/2511.20612) · [PDF](https://arxiv.org/pdf/2511.20612.pdf)  
**作者**：Yujin Kim, Sarah Dean  

**一句话要点**：提出随机NODE-DMD以解决稀疏观测下动态系统重建与不确定性量化问题

**关键词**：动态模式分解, 不确定性量化, 稀疏观测重建, 科学机器学习, 连续场建模

## 3 点简述
- 核心问题：稀疏/噪声观测和线性近似限制动态模式分解在连续场建模中的应用
- 方法要点：扩展DMD为概率模型，支持非线性动态和任意坐标连续重建
- 实验或效果：在10%观测密度下优于基线，恢复动态结构并量化不确定性

## 摘要（原文）

> Many consequential real-world systems, like wind fields and ocean currents, are dynamic and hard to model. Learning their governing dynamics remains a central challenge in scientific machine learning. Dynamic Mode Decomposition (DMD) provides a simple, data-driven approximation, but practical use is limited by sparse/noisy observations from continuous fields, reliance on linear approximations, and the lack of principled uncertainty quantification. To address these issues, we introduce Stochastic NODE-DMD, a probabilistic extension of DMD that models continuous-time, nonlinear dynamics while remaining interpretable. Our approach enables continuous spatiotemporal reconstruction at arbitrary coordinates and quantifies predictive uncertainty. Across four benchmarks, a synthetic setting and three physics-based flows, it surpasses a baseline in reconstruction accuracy when trained from only 10% observation density. It further recovers the dynamical structure by aligning learned modes and continuous-time eigenvalues with ground truth. Finally, on datasets with multiple realizations, our method learns a calibrated distribution over latent dynamics that preserves ensemble variability rather than averaging across regimes. Our code is available at: https://github.com/sedan-group/Stochastic-NODE-DMD

