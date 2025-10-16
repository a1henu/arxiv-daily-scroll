---
layout: default
title: Trace Anything: Representing Any Video in 4D via Trajectory Fields
---

# Trace Anything: Representing Any Video in 4D via Trajectory Fields
**arXiv**：[2510.13802v1](https://arxiv.org/abs/2510.13802) · [PDF](https://arxiv.org/pdf/2510.13802.pdf)  
**作者**：Xinhang Liu, Yuxi Xiao, Donny Y. Chen, Jiashi Feng, Yu-Wing Tai, Chi-Keung Tang, Bingyi Kang  

**一句话要点**：提出轨迹场表示法，通过单次前馈预测视频像素轨迹，提升动态建模效率。

**关键词**：轨迹场表示, 视频动态建模, B样条参数化, 单次前馈预测, 时空融合

## 3 点简述
- 核心问题：视频动态建模需有效时空表示，像素轨迹作为原子单元。
- 方法要点：使用轨迹场映射像素到连续3D轨迹，基于B样条参数化。
- 实验效果：在轨迹场估计基准上达到SOTA，效率高且具新兴能力。

## 摘要（原文）

> Effective spatio-temporal representation is fundamental to modeling,
> understanding, and predicting dynamics in videos. The atomic unit of a video,
> the pixel, traces a continuous 3D trajectory over time, serving as the
> primitive element of dynamics. Based on this principle, we propose representing
> any video as a Trajectory Field: a dense mapping that assigns a continuous 3D
> trajectory function of time to each pixel in every frame. With this
> representation, we introduce Trace Anything, a neural network that predicts the
> entire trajectory field in a single feed-forward pass. Specifically, for each
> pixel in each frame, our model predicts a set of control points that
> parameterizes a trajectory (i.e., a B-spline), yielding its 3D position at
> arbitrary query time instants. We trained the Trace Anything model on
> large-scale 4D data, including data from our new platform, and our experiments
> demonstrate that: (i) Trace Anything achieves state-of-the-art performance on
> our new benchmark for trajectory field estimation and performs competitively on
> established point-tracking benchmarks; (ii) it offers significant efficiency
> gains thanks to its one-pass paradigm, without requiring iterative optimization
> or auxiliary estimators; and (iii) it exhibits emergent abilities, including
> goal-conditioned manipulation, motion forecasting, and spatio-temporal fusion.
> Project page: https://trace-anything.github.io/.

