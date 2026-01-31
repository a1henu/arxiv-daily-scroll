---
layout: default
title: Zero-Shot Statistical Downscaling via Diffusion Posterior Sampling
---

# Zero-Shot Statistical Downscaling via Diffusion Posterior Sampling
**arXiv**：[2601.21760v1](https://arxiv.org/abs/2601.21760) · [PDF](https://arxiv.org/pdf/2601.21760.pdf)  
**作者**：Ruian Tie, Wenbo Xiong, Zhengyu Shi, Xinyu Su, Chenyu jiang, Libo Wu, Hao Li  

**一句话要点**：提出零样本统计降尺度框架ZSSD，通过扩散后验采样解决气候模型降尺度中的物理不一致和梯度消失问题。

**关键词**：零样本学习, 统计降尺度, 扩散模型, 气候建模, 物理一致性, 梯度消失

## 3 点简述
- 核心问题：传统监督降尺度因缺乏配对数据和领域差异难以泛化至全球气候模型，现有零样本方法在大尺度因子下存在物理不一致和梯度消失。
- 方法要点：ZSSD利用从再分析数据学习的物理一致气候先验，结合统一坐标指导，确保物理有效性和大尺度场一致性。
- 实验或效果：ZSSD在99百分位误差上显著优于现有零样本基线，能跨异质GCMs重建复杂天气事件如热带气旋。

## 摘要（原文）

> Conventional supervised climate downscaling struggles to generalize to Global Climate Models (GCMs) due to the lack of paired training data and inherent domain gaps relative to reanalysis. Meanwhile, current zero-shot methods suffer from physical inconsistencies and vanishing gradient issues under large scaling factors. We propose Zero-Shot Statistical Downscaling (ZSSD), a zero-shot framework that performs statistical downscaling without paired data during training. ZSSD leverages a Physics-Consistent Climate Prior learned from reanalysis data, conditioned on geophysical boundaries and temporal information to enforce physical validity. Furthermore, to enable robust inference across varying GCMs, we introduce Unified Coordinate Guidance. This strategy addresses the vanishing gradient problem in vanilla DPS and ensures consistency with large-scale fields. Results show that ZSSD significantly outperforms existing zero-shot baselines in 99th percentile errors and successfully reconstructs complex weather events, such as tropical cyclones, across heterogeneous GCMs.

