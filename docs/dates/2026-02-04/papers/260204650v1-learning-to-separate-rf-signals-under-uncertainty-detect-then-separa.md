---
layout: default
title: Learning to Separate RF Signals Under Uncertainty: Detect-Then-Separate vs. Unified Joint Models
---

# Learning to Separate RF Signals Under Uncertainty: Detect-Then-Separate vs. Unified Joint Models
**arXiv**：[2602.04650v1](https://arxiv.org/abs/2602.04650) · [PDF](https://arxiv.org/pdf/2602.04650.pdf)  
**作者**：Ariel Rodrigez, Alejandro Lancho, Amir Weiss  

**一句话要点**：提出统一联合模型以解决单通道射频信号在干扰类型未知下的分离问题

**关键词**：射频信号分离, 干扰类型未知, 统一联合模型, 检测后分离, 深度学习, 单通道处理

## 3 点简述
- 核心问题：射频频谱拥挤导致信号共存，需在单通道中分离非高斯干扰下的目标信号
- 方法要点：分析检测后分离策略的渐近最优性，提出基于UNet的统一联合模型进行联合检测与分离
- 实验或效果：统一联合模型在合成和实测数据上匹配检测后分离性能，展现可扩展性和实用性

## 摘要（原文）

> The increasingly crowded radio frequency (RF) spectrum forces communication signals to coexist, creating heterogeneous interferers whose structure often departs from Gaussian models. Recovering the interference-contaminated signal of interest in such settings is a central challenge, especially in single-channel RF processing. Existing data-driven methods often assume that the interference type is known, yielding ensembles of specialized models that scale poorly with the number of interferers. We show that detect-then-separate (DTS) strategies admit an analytical justification: within a Gaussian mixture framework, a plug-in maximum a posteriori detector followed by type-conditioned optimal estimation achieves asymptotic minimum mean-square error optimality under a mild temporal-diversity condition. This makes DTS a principled benchmark, but its reliance on multiple type-specific models limits scalability. Motivated by this, we propose a unified joint model (UJM), in which a single deep neural architecture learns to jointly detect and separate when applied directly to the received signal. Using tailored UNet architectures for baseband (complex-valued) RF signals, we compare DTS and UJM on synthetic and recorded interference types, showing that a capacity-matched UJM can match oracle-aided DTS performance across diverse signal-to-interference-and-noise ratios, interference types, and constellation orders, including mismatched training and testing type-uncertainty proportions. These findings highlight UJM as a scalable and practical alternative to DTS, while opening new directions for unified separation under broader regimes.

