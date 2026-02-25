---
layout: default
title: CGSTA: Cross-Scale Graph Contrast with Stability-Aware Alignment for Multivariate Time-Series Anomaly Detection
---

# CGSTA: Cross-Scale Graph Contrast with Stability-Aware Alignment for Multivariate Time-Series Anomaly Detection
**arXiv**：[2602.20468v1](https://arxiv.org/abs/2602.20468) · [PDF](https://arxiv.org/pdf/2602.20468.pdf)  
**作者**：Zhongpeng Qi, Jun Zhang, Wei Li, Zhuoxuan Liang  

**一句话要点**：提出CGSTA框架，通过跨尺度图对比与稳定性感知对齐解决多元时间序列异常检测中的噪声和依赖关系挑战。

**关键词**：多元时间序列异常检测, 图对比学习, 稳定性感知对齐, 动态分层图, 跨尺度学习, 噪声抑制

## 3 点简述
- 核心问题：多元时间序列异常检测面临变量间依赖关系动态变化和噪声干扰，导致现有方法易产生误报或漏报。
- 方法要点：采用动态分层图构建多尺度视图，结合跨尺度对比学习和稳定性感知对齐，以抑制噪声并增强结构感知。
- 实验或效果：在PSM和WADI基准上表现最优，在SWaT和SMAP上与基线方法性能相当，验证了框架的有效性。

## 摘要（原文）

> Multivariate time-series anomaly detection is essential for reliable industrial control, telemetry, and service monitoring. However, the evolving inter-variable dependencies and inevitable noise render it challenging. Existing methods often use single-scale graphs or instance-level contrast. Moreover, learned dynamic graphs can overfit noise without a stable anchor, causing false alarms or misses. To address these challenges, we propose the CGSTA framework with two key innovations. First, Dynamic Layered Graph Construction (DLGC) forms local, regional, and global views of variable relations for each sliding window; rather than contrasting whole windows, Contrastive Discrimination across Scales (CDS) contrasts graph representations within each view and aligns the same window across views to make learning structure-aware. Second, Stability-Aware Alignment (SAA) maintains a per-scale stable reference learned from normal data and guides the current window's fast-changing graphs toward it to suppress noise. We fuse the multi-scale and temporal features and use a conditional density estimator to produce per-time-step anomaly scores. Across four benchmarks, CGSTA delivers optimal performance on PSM and WADI, and is comparable to the baseline methods on SWaT and SMAP.

