---
layout: default
title: Towards a data-scale independent regulariser for robust sparse identification of non-linear dynamics
---

# Towards a data-scale independent regulariser for robust sparse identification of non-linear dynamics
**arXiv**：[2603.05201v1](https://arxiv.org/abs/2603.05201) · [PDF](https://arxiv.org/pdf/2603.05201.pdf)  
**作者**：Jay Raut, Daniel N. Wilke, Stephan Schmidt  

**一句话要点**：提出STCV算法以解决数据归一化对稀疏非线性动力学识别的影响

**关键词**：稀疏系统识别, 非线性动力学, 数据归一化, 统计阈值, SINDy框架, 鲁棒回归

## 3 点简述
- 数据归一化在稀疏回归中扭曲方程发现，尤其影响SINDy框架
- STCV使用无量纲统计指标替代幅度阈值，增强对数据缩放的鲁棒性
- 在标准系统和工程实验中，STCV优于STLSQ和E-SINDy，提升模型可靠性

## 摘要（原文）

> Data normalisation, a common and often necessary preprocessing step in engineering and scientific applications, can severely distort the discovery of governing equations by magnitudebased sparse regression methods. This issue is particularly acute for the Sparse Identification of Nonlinear Dynamics (SINDy) framework, where the core assumption of sparsity is undermined by the interaction between data scaling and measurement noise. The resulting discovered models can be dense, uninterpretable, and physically incorrect. To address this critical vulnerability, we introduce the Sequential Thresholding of Coefficient of Variation (STCV), a novel, computationally efficient sparse regression algorithm that is inherently robust to data scaling. STCV replaces conventional magnitude-based thresholding with a dimensionless statistical metric, the Coefficient Presence (CP), which assesses the statistical validity and consistency of candidate terms in the model library. This shift from magnitude to statistical significance makes the discovery process invariant to arbitrary data scaling. Through comprehensive benchmarking on canonical dynamical systems and practical engineering problems, including a physical mass-spring-damper experiment, we demonstrate that STCV consistently and significantly outperforms standard Sequential Thresholding Least Squares (STLSQ) and Ensemble-SINDy (E-SINDy) on normalised, noisy datasets. The results show that STCV-based methods can successfully identify the correct, sparse physical laws even when other methods fail. By mitigating the distorting effects of normalisation, STCV makes sparse system identification a more reliable and automated tool for real-world applications, thereby enhancing model interpretability and trustworthiness.

