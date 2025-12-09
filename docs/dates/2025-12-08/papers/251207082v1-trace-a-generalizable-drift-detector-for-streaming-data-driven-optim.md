---
layout: default
title: TRACE: A Generalizable Drift Detector for Streaming Data-Driven Optimization
---

# TRACE: A Generalizable Drift Detector for Streaming Data-Driven Optimization
**arXiv**：[2512.07082v1](https://arxiv.org/abs/2512.07082) · [PDF](https://arxiv.org/pdf/2512.07082.pdf)  
**作者**：Yuan-Ting Zhong, Ting Huang, Xiaolin Xiao, Yue-Jiao Gong  

**一句话要点**：提出TRACE以解决流数据驱动优化中的未知概念漂移检测问题

**关键词**：概念漂移检测, 流数据驱动优化, 注意力序列学习, 可迁移学习, 自适应优化

## 3 点简述
- 核心问题：流数据驱动优化中未知概念漂移的检测挑战，现有方法受限于固定漂移间隔和完全环境可观测性假设
- 方法要点：基于原则性标记化策略提取统计特征，利用注意力序列学习建模漂移模式，实现跨数据集可迁移检测
- 实验或效果：在多样化基准测试中展示出优越的泛化性、鲁棒性和有效性，并集成到流优化器中实现自适应优化

## 摘要（原文）

> Many optimization tasks involve streaming data with unknown concept drifts, posing a significant challenge as Streaming Data-Driven Optimization (SDDO). Existing methods, while leveraging surrogate model approximation and historical knowledge transfer, are often under restrictive assumptions such as fixed drift intervals and fully environmental observability, limiting their adaptability to diverse dynamic environments. We propose TRACE, a TRAnsferable C}oncept-drift Estimator that effectively detects distributional changes in streaming data with varying time scales. TRACE leverages a principled tokenization strategy to extract statistical features from data streams and models drift patterns using attention-based sequence learning, enabling accurate detection on unseen datasets and highlighting the transferability of learned drift patterns. Further, we showcase TRACE's plug-and-play nature by integrating it into a streaming optimizer, facilitating adaptive optimization under unknown drifts. Comprehensive experimental results on diverse benchmarks demonstrate the superior generalization, robustness, and effectiveness of our approach in SDDO scenarios.

