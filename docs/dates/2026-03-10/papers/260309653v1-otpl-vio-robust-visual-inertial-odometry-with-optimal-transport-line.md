---
layout: default
title: OTPL-VIO: Robust Visual-Inertial Odometry with Optimal Transport Line Association and Adaptive Uncertainty
---

# OTPL-VIO: Robust Visual-Inertial Odometry with Optimal Transport Line Association and Adaptive Uncertainty
**arXiv**：[2603.09653v1](https://arxiv.org/abs/2603.09653) · [PDF](https://arxiv.org/pdf/2603.09653.pdf)  
**作者**：Zikun Chen, Wentao Zhao, Yihe Niu, Tianchen Deng, Jingchuan Wang  

**一句话要点**：提出OTPL-VIO，通过最优传输线关联和自适应不确定性，增强低纹理和光照变化场景下的视觉惯性里程计鲁棒性。

**关键词**：视觉惯性里程计, 线特征关联, 最优传输, 自适应不确定性, 低纹理场景, 实时系统

## 3 点简述
- 核心问题：低纹理和光照突变场景中，点特征稀疏不稳定，导致关联模糊和估计不足。
- 方法要点：使用无训练深度描述符和熵正则化最优传输进行线匹配，引入可靠性自适应加权优化约束。
- 实验或效果：在EuRoC和UMA-VI数据集及真实环境中验证，精度和鲁棒性优于基线，保持实时性能。

## 摘要（原文）

> Robust stereo visual-inertial odometry (VIO) remains challenging in low-texture scenes and under abrupt illumination changes, where point features become sparse and unstable, leading to ambiguous association and under-constrained estimation. Line structures offer complementary geometric cues, yet many efficient point-line systems still rely on point-guided line association, which can break down when point support is weak and may lead to biased constraints. We present a stereo point-line VIO system in which line segments are equipped with dedicated deep descriptors and matched using an entropy-regularized optimal transport formulation, enabling globally consistent correspondences under ambiguity, outliers, and partial observations. The proposed descriptor is training-free and is computed by sampling and pooling network feature maps. To improve estimation stability, we analyze the impact of line measurement noise and introduce reliability-adaptive weighting to regulate the influence of line constraints during optimization. Experiments on EuRoC and UMA-VI, together with real-world deployments in low-texture and illumination-challenging environments, demonstrate improved accuracy and robustness over representative baselines while maintaining real-time performance.

