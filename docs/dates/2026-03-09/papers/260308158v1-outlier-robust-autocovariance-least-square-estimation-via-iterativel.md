---
layout: default
title: Outlier-robust Autocovariance Least Square Estimation via Iteratively Reweighted Least Square
---

# Outlier-robust Autocovariance Least Square Estimation via Iteratively Reweighted Least Square
**arXiv**：[2603.08158v1](https://arxiv.org/abs/2603.08158) · [PDF](https://arxiv.org/pdf/2603.08158.pdf)  
**作者**：Jiahong Li, Fang Deng  

**一句话要点**：提出基于迭代重加权最小二乘的自协方差最小二乘估计方法，以增强卡尔曼滤波中噪声协方差估计的异常值鲁棒性。

**关键词**：自协方差最小二乘, 迭代重加权最小二乘, 异常值鲁棒性, 卡尔曼滤波, 噪声协方差估计

## 3 点简述
- 传统自协方差最小二乘方法对测量异常值敏感，导致性能下降。
- 采用创新级自适应阈值和Huber成本函数，通过迭代重加权最小二乘框架减少异常值影响。
- 仿真显示，新方法显著降低估计误差，提升状态估计精度，接近理想下限。

## 摘要（原文）

> The autocovariance least squares (ALS) method is a computationally efficient approach for estimating noise covariances in Kalman filters without requiring specific noise models. However, conventional ALS and its variants rely on the classic least mean squares (LMS) criterion, making them highly sensitive to measurement outliers and prone to severe performance degradation. To overcome this limitation, this paper proposes a novel outlier-robust ALS algorithm, termed ALS-IRLS, based on the iteratively reweighted least squares (IRLS) framework. Specifically, the proposed approach introduces a two-tier robustification strategy. First, an innovation-level adaptive thresholding mechanism is employed to filter out heavily contaminated data. Second, the outlier-contaminated autocovariance is formulated using an $ε$-contamination model, where the standard LMS criterion is replaced by the Huber cost function. The IRLS method is then utilized to iteratively adjust data weights based on estimation deviations, effectively mitigating the influence of residual outliers. Comparative simulations demonstrate that ALS-IRLS reduces the root-mean-square error (RMSE) of noise covariance estimates by over two orders of magnitude compared to standard ALS. Furthermore, it significantly enhances downstream state estimation accuracy, outperforming existing outlier-robust Kalman filters and achieving performance nearly equivalent to the ideal Oracle lower bound in the presence of noisy and anomalous data.

