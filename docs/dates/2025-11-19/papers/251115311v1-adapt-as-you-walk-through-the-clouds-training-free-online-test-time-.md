---
layout: default
title: Adapt-As-You-Walk Through the Clouds: Training-Free Online Test-Time Adaptation of 3D Vision-Language Foundation Models
---

# Adapt-As-You-Walk Through the Clouds: Training-Free Online Test-Time Adaptation of 3D Vision-Language Foundation Models
**arXiv**：[2511.15311v1](https://arxiv.org/abs/2511.15311) · [PDF](https://arxiv.org/pdf/2511.15311.pdf)  
**作者**：Mehran Tamjidi, Hamidreza Dastmalchi, Mohammadreza Alimoradijazi, Ali Cheraghian, Aijun An, Morteza Saberi  

**一句话要点**：提出Uni-Adapter以解决3D视觉语言基础模型在分布偏移下的性能下降问题

**关键词**：3D视觉语言基础模型, 测试时适应, 动态原型学习, 图标签平滑, 免训练适应, 分布偏移缓解

## 3 点简述
- 核心问题：3D视觉语言基础模型在噪声、不完整或分布外数据中性能下降
- 方法要点：基于动态原型学习和图标签平滑，实现免训练在线测试时适应
- 实验或效果：在多个3D基准上显著提升性能，如ModelNet-40C提高10.55%

## 摘要（原文）

> 3D Vision-Language Foundation Models (VLFMs) have shown strong generalization and zero-shot recognition capabilities in open-world point cloud processing tasks. However, these models often underperform in practical scenarios where data are noisy, incomplete, or drawn from a different distribution than the training data. To address this, we propose Uni-Adapter, a novel training-free online test-time adaptation (TTA) strategy for 3D VLFMs based on dynamic prototype learning. We define a 3D cache to store class-specific cluster centers as prototypes, which are continuously updated to capture intra-class variability in heterogeneous data distributions. These dynamic prototypes serve as anchors for cache-based logit computation via similarity scoring. Simultaneously, a graph-based label smoothing module captures inter-prototype similarities to enforce label consistency among similar prototypes. Finally, we unify predictions from the original 3D VLFM and the refined 3D cache using entropy-weighted aggregation for reliable adaptation. Without retraining, Uni-Adapter effectively mitigates distribution shifts, achieving state-of-the-art performance on diverse 3D benchmarks over different 3D VLFMs, improving ModelNet-40C by 10.55%, ScanObjectNN-C by 8.26%, and ShapeNet-C by 4.49% over the source 3D VLFMs.

