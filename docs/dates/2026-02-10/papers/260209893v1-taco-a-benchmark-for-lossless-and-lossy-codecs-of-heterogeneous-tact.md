---
layout: default
title: TaCo: A Benchmark for Lossless and Lossy Codecs of Heterogeneous Tactile Data
---

# TaCo: A Benchmark for Lossless and Lossy Codecs of Heterogeneous Tactile Data
**arXiv**：[2602.09893v1](https://arxiv.org/abs/2602.09893) · [PDF](https://arxiv.org/pdf/2602.09893.pdf)  
**作者**：Zhengxue Cheng, Yan Zhao, Keyu Wang, Hengdi Zhang, Li Song  

**一句话要点**：提出TaCo基准以评估异构触觉数据无损与有损编解码器性能

**关键词**：触觉数据压缩, 编解码器基准, 异构数据处理, 机器人感知, 无损与有损压缩

## 3 点简述
- 触觉数据压缩在带宽受限的实时机器人应用中至关重要，但异构性和复杂性使其研究不足。
- TaCo基准评估30种压缩方法，包括现成算法和神经编解码器，覆盖五个数据集和四个关键任务。
- 开发数据驱动的TaCo-LL和TaCo-L编解码器，在压缩效率和任务性能间提供关键权衡框架。

## 摘要（原文）

> Tactile sensing is crucial for embodied intelligence, providing fine-grained perception and control in complex environments. However, efficient tactile data compression, which is essential for real-time robotic applications under strict bandwidth constraints, remains underexplored. The inherent heterogeneity and spatiotemporal complexity of tactile data further complicate this challenge. To bridge this gap, we introduce TaCo, the first comprehensive benchmark for Tactile data Codecs. TaCo evaluates 30 compression methods, including off-the-shelf compression algorithms and neural codecs, across five diverse datasets from various sensor types. We systematically assess both lossless and lossy compression schemes on four key tasks: lossless storage, human visualization, material and object classification, and dexterous robotic grasping. Notably, we pioneer the development of data-driven codecs explicitly trained on tactile data, TaCo-LL (lossless) and TaCo-L (lossy). Results have validated the superior performance of our TaCo-LL and TaCo-L. This benchmark provides a foundational framework for understanding the critical trade-offs between compression efficiency and task performance, paving the way for future advances in tactile perception.

