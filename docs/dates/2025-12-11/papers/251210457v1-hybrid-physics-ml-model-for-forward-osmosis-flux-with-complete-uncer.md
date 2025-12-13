---
layout: default
title: Hybrid Physics-ML Model for Forward Osmosis Flux with Complete Uncertainty Quantification
---

# Hybrid Physics-ML Model for Forward Osmosis Flux with Complete Uncertainty Quantification
**arXiv**：[2512.10457v1](https://arxiv.org/abs/2512.10457) · [PDF](https://arxiv.org/pdf/2512.10457.pdf)  
**作者**：Shiv Ratn, Shivang Rampriyan, Bahni Ray  

**一句话要点**：提出基于高斯过程回归的混合物理-机器学习框架，用于正渗透水通量预测与完全不确定性量化。

**关键词**：正渗透水通量预测, 混合物理-机器学习模型, 高斯过程回归, 不确定性量化, 膜分离技术, 数字孪生

## 3 点简述
- 核心问题：传统机理模型参数多变，纯数据驱动模型缺乏物理一致性和不确定性量化。
- 方法要点：训练高斯过程回归于物理模型预测与实验水通量之间的残差，实现混合建模。
- 实验或效果：在120个数据点上训练，测试集MAPE为0.26%，R²为0.999，验证了鲁棒性。

## 摘要（原文）

> Forward Osmosis (FO) is a promising low-energy membrane separation technology, but challenges in accurately modelling its water flux (Jw) persist due to complex internal mass transfer phenomena. Traditional mechanistic models struggle with empirical parameter variability, while purely data-driven models lack physical consistency and rigorous uncertainty quantification (UQ). This study introduces a novel Robust Hybrid Physics-ML framework employing Gaussian Process Regression (GPR) for highly accurate, uncertainty-aware Jw prediction. The core innovation lies in training the GPR on the residual error between the detailed, non-linear FO physical model prediction (Jw_physical) and the experimental water flux (Jw_actual). Crucially, we implement a full UQ methodology by decomposing the total predictive variance (sigma2_total) into model uncertainty (epistemic, from GPR's posterior variance) and input uncertainty (aleatoric, analytically propagated via the Delta method for multi-variate correlated inputs). Leveraging the inherent strength of GPR in low-data regimes, the model, trained on a meagre 120 data points, achieved a state-of-the-art Mean Absolute Percentage Error (MAPE) of 0.26% and an R2 of 0.999 on the independent test data, validating a truly robust and reliable surrogate model for advanced FO process optimization and digital twin development.

