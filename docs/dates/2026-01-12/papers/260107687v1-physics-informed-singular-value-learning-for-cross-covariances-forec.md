---
layout: default
title: Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets
---

# Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets
**arXiv**：[2601.07687v1](https://arxiv.org/abs/2601.07687) · [PDF](https://arxiv.org/pdf/2601.07687.pdf)  
**作者**：Efstratios Manolakis, Christian Bongiorno, Rosario Nunzio Mantegna  

**一句话要点**：提出基于随机矩阵理论的神经网络架构，以提升非平稳金融市场中交叉协方差预测的稳健性。

**关键词**：交叉协方差预测, 随机矩阵理论, 神经网络架构, 非平稳金融市场, 奇异值学习, 样本外性能

## 3 点简述
- 现有交叉协方差清洁方法在非平稳和全局模式显著的金融市场中样本外性能不佳。
- 设计神经网络在经验奇异向量基上学习非线性映射，灵活适应非平稳动态和模式驱动失真。
- 在股票收益数据上训练，相比纯解析方法实现更优偏差-方差权衡，降低预测误差。

## 摘要（原文）

> A new wave of work on covariance cleaning and nonlinear shrinkage has delivered asymptotically optimal analytical solutions for large covariance matrices. Building on this progress, these ideas have been generalized to empirical cross-covariance matrices, whose singular-value shrinkage characterizes comovements between one set of assets and another. Existing analytical cross-covariance cleaners are derived under strong stationarity and large-sample assumptions, and they typically rely on mesoscopic regularity conditions such as bounded spectra; macroscopic common modes (e.g., a global market factor) violate these conditions. When applied to real equity returns, where dependence structures drift over time and global modes are prominent, we find that these theoretically optimal formulas do not translate into robust out-of-sample performance. We address this gap by designing a random-matrix-inspired neural architecture that operates in the empirical singular-vector basis and learns a nonlinear mapping from empirical singular values to their corresponding cleaned values. By construction, the network can recover the analytical solution as a special case, yet it remains flexible enough to adapt to non-stationary dynamics and mode-driven distortions. Trained on a long history of equity returns, the proposed method achieves a more favorable bias-variance trade-off than purely analytical cleaners and delivers systematically lower out-of-sample cross-covariance prediction errors. Our results demonstrate that combining random-matrix theory with machine learning makes asymptotic theories practically effective in realistic time-varying markets.

