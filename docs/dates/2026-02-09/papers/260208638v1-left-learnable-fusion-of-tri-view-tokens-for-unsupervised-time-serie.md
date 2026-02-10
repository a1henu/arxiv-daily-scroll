---
layout: default
title: LEFT: Learnable Fusion of Tri-view Tokens for Unsupervised Time Series Anomaly Detection
---

# LEFT: Learnable Fusion of Tri-view Tokens for Unsupervised Time Series Anomaly Detection
**arXiv**：[2602.08638v1](https://arxiv.org/abs/2602.08638) · [PDF](https://arxiv.org/pdf/2602.08638.pdf)  
**作者**：Dezheng Wang, Tong Chen, Guansong Pang, Congyan Chen, Shihua Li, Hongzhi Yin  

**一句话要点**：提出LEFT框架，通过三视图令牌可学习融合解决无监督时间序列异常检测中的跨视图不一致问题。

**关键词**：无监督时间序列异常检测, 多视图融合, 时间-频率一致性, 自适应谱滤波器, 令牌学习

## 3 点简述
- 核心问题：无监督时间序列异常检测中，许多异常在单一视图（如时域）中难以检测，需依赖跨视图（时域、频域、多尺度）的不一致性。
- 方法要点：LEFT从时域、频域和多尺度三个视图学习令牌，引入自适应奈奎斯特约束谱滤波器生成多尺度令牌，并通过时间-频率循环一致性约束和重构目标增强跨视图一致性。
- 实验或效果：在真实世界基准测试中，LEFT达到最佳检测精度，同时训练FLOPs减少5倍，速度提升8倍。

## 摘要（原文）

> As a fundamental data mining task, unsupervised time series anomaly detection (TSAD) aims to build a model for identifying abnormal timestamps without assuming the availability of annotations. A key challenge in unsupervised TSAD is that many anomalies are too subtle to exhibit detectable deviation in any single view (e.g., time domain), and instead manifest as inconsistencies across multiple views like time, frequency, and a mixture of resolutions. However, most cross-view methods rely on feature or score fusion and do not enforce analysis-synthesis consistency, meaning the frequency branch is not required to reconstruct the time signal through an inverse transform, and vice versa. In this paper, we present Learnable Fusion of Tri-view Tokens (LEFT), a unified unsupervised TSAD framework that models anomalies as inconsistencies across complementary representations. LEFT learns feature tokens from three views of the same input time series: frequency-domain tokens that embed periodicity information, time-domain tokens that capture local dynamics, and multi-scale tokens that learns abnormal patterns at varying time series granularities. By learning a set of adaptive Nyquist-constrained spectral filters, the original time series is rescaled into multiple resolutions and then encoded, allowing these multi-scale tokens to complement the extracted frequency- and time-domain information. When generating the fused representation, we introduce a novel objective that reconstructs fine-grained targets from coarser multi-scale structure, and put forward an innovative time-frequency cycle consistency constraint to explicitly regularize cross-view agreement. Experiments on real-world benchmarks show that LEFT yields the best detection accuracy against SOTA baselines, while achieving a 5x reduction on FLOPs and 8x speed-up for training.

