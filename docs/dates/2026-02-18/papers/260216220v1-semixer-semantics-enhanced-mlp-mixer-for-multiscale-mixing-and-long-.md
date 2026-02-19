---
layout: default
title: SEMixer: Semantics Enhanced MLP-Mixer for Multiscale Mixing and Long-term Time Series Forecasting
---

# SEMixer: Semantics Enhanced MLP-Mixer for Multiscale Mixing and Long-term Time Series Forecasting
**arXiv**：[2602.16220v1](https://arxiv.org/abs/2602.16220) · [PDF](https://arxiv.org/pdf/2602.16220.pdf)  
**作者**：Xu Zhang, Qitong Wang, Peng Wang, Wei Wang  

**一句话要点**：提出SEMixer以解决长时序预测中的多尺度依赖建模挑战

**关键词**：长时序预测, 多尺度建模, 随机注意力机制, MLP-Mixer, 语义增强, 时序混合

## 3 点简述
- 核心问题：时序数据冗余噪声及非相邻尺度间的语义鸿沟阻碍多尺度依赖有效整合
- 方法要点：引入随机注意力机制增强补丁级语义，结合多尺度渐进混合链实现高效时序混合
- 实验或效果：在10个公共数据集及21GB真实无线网络数据上验证有效性，获2025 CCF AlOps挑战赛第三名

## 摘要（原文）

> Modeling multiscale patterns is crucial for long-term time series forecasting (TSF). However, redundancy and noise in time series, together with semantic gaps between non-adjacent scales, make the efficient alignment and integration of multi-scale temporal dependencies challenging. To address this, we propose SEMixer, a lightweight multiscale model designed for long-term TSF. SEMixer features two key components: a Random Attention Mechanism (RAM) and a Multiscale Progressive Mixing Chain (MPMC). RAM captures diverse time-patch interactions during training and aggregates them via dropout ensemble at inference, enhancing patch-level semantics and enabling MLP-Mixer to better model multi-scale dependencies. MPMC further stacks RAM and MLP-Mixer in a memory-efficient manner, achieving more effective temporal mixing. It addresses semantic gaps across scales and facilitates better multiscale modeling and forecasting performance. We not only validate the effectiveness of SEMixer on 10 public datasets, but also on the \textit{2025 CCF AlOps Challenge} based on 21GB real wireless network data, where SEMixer achieves third place. The code is available at the link https://github.com/Meteor-Stars/SEMixer.

