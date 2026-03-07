---
layout: default
title: CATNet: Collaborative Alignment and Transformation Network for Cooperative Perception
---

# CATNet: Collaborative Alignment and Transformation Network for Cooperative Perception
**arXiv**：[2603.05255v1](https://arxiv.org/abs/2603.05255) · [PDF](https://arxiv.org/pdf/2603.05255.pdf)  
**作者**：Gong Chen, Chaokun Zhang, Tao Tang, Pengcheng Lv, Feng Li, Xin Xie  

**一句话要点**：提出CATNet以解决协同感知中的高时延和多源噪声问题

**关键词**：协同感知, 时延补偿, 噪声抑制, 特征对齐, 自适应融合, 交通场景

## 3 点简述
- 核心问题：真实世界多源数据集成存在高时延和噪声干扰，影响协同感知性能。
- 方法要点：通过STSync对齐异步特征流，WTDen抑制噪声并重构特征，AdpSel动态选择关键特征进行融合。
- 实验或效果：在多个数据集上验证，CATNet在复杂交通条件下优于现有方法，展现鲁棒性和适应性。

## 摘要（原文）

> Cooperative perception significantly enhances scene understanding by integrating complementary information from diverse agents. However, existing research often overlooks critical challenges inherent in real-world multi-source data integration, specifically high temporal latency and multi-source noise. To address these practical limitations, we propose Collaborative Alignment and Transformation Network (CATNet), an adaptive compensation framework that resolves temporal latency and noise interference in multi-agent systems. Our key innovations can be summarized in three aspects. First, we introduce a Spatio-Temporal Recurrent Synchronization (STSync) that aligns asynchronous feature streams via adjacent-frame differential modeling, establishing a temporal-spatially unified representation space. Second, we design a Dual-Branch Wavelet Enhanced Denoiser (WTDen) that suppresses global noise and reconstructs localized feature distortions within aligned representations. Third, we construct an Adaptive Feature Selector (AdpSel) that dynamically focuses on critical perceptual features for robust fusion. Extensive experiments on multiple datasets demonstrate that CATNet consistently outperforms existing methods under complex traffic conditions, proving its superior robustness and adaptability.

