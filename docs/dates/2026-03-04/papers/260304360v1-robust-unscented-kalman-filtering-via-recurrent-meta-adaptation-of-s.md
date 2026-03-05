---
layout: default
title: Robust Unscented Kalman Filtering via Recurrent Meta-Adaptation of Sigma-Point Weights
---

# Robust Unscented Kalman Filtering via Recurrent Meta-Adaptation of Sigma-Point Weights
**arXiv**：[2603.04360v1](https://arxiv.org/abs/2603.04360) · [PDF](https://arxiv.org/pdf/2603.04360.pdf)  
**作者**：Kenan Majewski, Michał Modzelewski, Marcin Żugaj, Piotr Lichota  

**一句话要点**：提出元自适应无迹卡尔曼滤波器，通过记忆增强元学习动态调整sigma点权重以提升非线性状态估计的鲁棒性。

**关键词**：无迹卡尔曼滤波器, 元学习, 非线性状态估计, 鲁棒滤波, 自适应权重, 循环神经网络

## 3 点简述
- 核心问题：无迹卡尔曼滤波器的性能受限于无迹变换的静态参数化，无法适应时变动态或重尾噪声。
- 方法要点：采用循环上下文编码器压缩测量创新历史，通过策略网络动态合成sigma点权重，实现端到端优化。
- 实验或效果：在机动目标跟踪中显著优于基线，对非高斯闪烁噪声具有鲁棒性，并能泛化到训练未见动态。

## 摘要（原文）

> The Unscented Kalman Filter (UKF) is a ubiquitous tool for nonlinear state estimation; however, its performance is limited by the static parameterization of the Unscented Transform (UT). Conventional weighting schemes, governed by fixed scaling parameters, assume implicit Gaussianity and fail to adapt to time-varying dynamics or heavy-tailed measurement noise. This work introduces the Meta-Adaptive UKF (MA-UKF), a framework that reformulates sigma-point weight synthesis as a hyperparameter optimization problem addressed via memory-augmented meta-learning. Unlike standard adaptive filters that rely on instantaneous heuristic corrections, our approach employs a Recurrent Context Encoder to compress the history of measurement innovations into a compact latent embedding. This embedding informs a policy network that dynamically synthesizes the mean and covariance weights of the sigma points at each time step, effectively governing the filter's trust in the prediction versus the measurement. By optimizing the system end-to-end through the filter's recursive logic, the MA-UKF learns to maximize tracking accuracy while maintaining estimation consistency. Numerical benchmarks on maneuvering targets demonstrate that the MA-UKF significantly outperforms standard baselines, exhibiting superior robustness to non-Gaussian glint noise and effective generalization to out-of-distribution (OOD) dynamic regimes unseen during training.

