---
layout: default
title: SparseLaneSTP: Leveraging Spatio-Temporal Priors with Sparse Transformers for 3D Lane Detection
---

# SparseLaneSTP: Leveraging Spatio-Temporal Priors with Sparse Transformers for 3D Lane Detection
**arXiv**：[2601.04968v1](https://arxiv.org/abs/2601.04968) · [PDF](https://arxiv.org/pdf/2601.04968.pdf)  
**作者**：Maximilian Pittner, Joel Janai, Mario Faigle, Alexandru Paul Condurache  

**一句话要点**：提出SparseLaneSTP，利用稀疏Transformer整合时空先验以解决3D车道检测中的特征对齐与模糊性问题。

**关键词**：3D车道检测, 稀疏Transformer, 时空注意力, 自动驾驶, 车道先验, 时序正则化

## 3 点简述
- 核心问题：现有方法忽视车道几何先验和时序信息，导致特征对齐差和模糊场景检测困难。
- 方法要点：引入车道特定时空注意力机制、连续车道表示和时序正则化，集成到稀疏Transformer中。
- 实验或效果：在现有基准和新数据集上实现最先进性能，并贡献精确一致的3D车道数据集。

## 摘要（原文）

> 3D lane detection has emerged as a critical challenge in autonomous driving, encompassing identification and localization of lane markings and the 3D road surface. Conventional 3D methods detect lanes from dense birds-eye-viewed (BEV) features, though erroneous transformations often result in a poor feature representation misaligned with the true 3D road surface. While recent sparse lane detectors have surpassed dense BEV approaches, they completely disregard valuable lane-specific priors. Furthermore, existing methods fail to utilize historic lane observations, which yield the potential to resolve ambiguities in situations of poor visibility. To address these challenges, we present SparseLaneSTP, a novel method that integrates both geometric properties of the lane structure and temporal information into a sparse lane transformer. It introduces a new lane-specific spatio-temporal attention mechanism, a continuous lane representation tailored for sparse architectures as well as temporal regularization. Identifying weaknesses of existing 3D lane datasets, we also introduce a precise and consistent 3D lane dataset using a simple yet effective auto-labeling strategy. Our experimental section proves the benefits of our contributions and demonstrates state-of-the-art performance across all detection and error metrics on existing 3D lane detection benchmarks as well as on our novel dataset.

