---
layout: default
title: MTS-JEPA: Multi-Resolution Joint-Embedding Predictive Architecture for Time-Series Anomaly Prediction
---

# MTS-JEPA: Multi-Resolution Joint-Embedding Predictive Architecture for Time-Series Anomaly Prediction
**arXiv**：[2602.04643v1](https://arxiv.org/abs/2602.04643) · [PDF](https://arxiv.org/pdf/2602.04643.pdf)  
**作者**：Yanan He, Yunshi Wen, Xin Wang, Tengfei Ma  

**一句话要点**：提出MTS-JEPA以解决多变量时间序列异常预测中的表示崩溃和多尺度信号捕获问题

**关键词**：多变量时间序列, 异常预测, 联合嵌入预测架构, 多分辨率建模, 软码本瓶颈, 早期预警

## 3 点简述
- 核心问题：JEPA在时间序列异常预测中易出现表示崩溃，且难以捕捉不同时间尺度的前兆信号
- 方法要点：集成多分辨率预测目标和软码本瓶颈，解耦瞬态冲击与长期趋势，捕获离散状态转换
- 实验或效果：在标准基准测试中有效防止退化解，并在早期预警协议下实现最先进性能

## 摘要（原文）

> Multivariate time series underpin modern critical infrastructure, making the prediction of anomalies a vital necessity for proactive risk mitigation. While Joint-Embedding Predictive Architectures (JEPA) offer a promising framework for modeling the latent evolution of these systems, their application is hindered by representation collapse and an inability to capture precursor signals across varying temporal scales. To address these limitations, we propose MTS-JEPA, a specialized architecture that integrates a multi-resolution predictive objective with a soft codebook bottleneck. This design explicitly decouples transient shocks from long-term trends, and utilizes the codebook to capture discrete regime transitions. Notably, we find this constraint also acts as an intrinsic regularizer to ensure optimization stability. Empirical evaluations on standard benchmarks confirm that our approach effectively prevents degenerate solutions and achieves state-of-the-art performance under the early-warning protocol.

