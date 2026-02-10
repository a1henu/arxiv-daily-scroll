---
layout: default
title: Tighnari v2: Mitigating Label Noise and Distribution Shift in Multimodal Plant Distribution Prediction via Mixture of Experts and Weakly Supervised Learning
---

# Tighnari v2: Mitigating Label Noise and Distribution Shift in Multimodal Plant Distribution Prediction via Mixture of Experts and Weakly Supervised Learning
**arXiv**：[2602.08282v1](https://arxiv.org/abs/2602.08282) · [PDF](https://arxiv.org/pdf/2602.08282.pdf)  
**作者**：Haixu Liu, Yufei Wang, Tianxiang Xu, Chuancheng Shi, Hongsheng Xing  

**一句话要点**：提出基于专家混合与弱监督学习的多模态植物分布预测框架，以缓解标签噪声和分布偏移问题。

**关键词**：植物分布预测, 多模态融合, 标签噪声缓解, 分布偏移处理, 专家混合模型, 弱监督学习

## 3 点简述
- 核心问题：植物分布预测中，存在-缺失数据稀缺且昂贵，存在-仅数据覆盖广但负样本标签噪声严重，且训练与测试样本间存在地理分布偏移。
- 方法要点：采用伪标签聚合策略对齐标签与遥感特征空间，结合Swin Transformer、TabM网络和时序模型，通过串行三模态交叉注意力优化多模态融合，并基于专家混合范式分区推理。
- 实验或效果：在GeoLifeCLEF 2025数据集上验证，在存在-缺失数据有限且分布偏移显著场景下，实现了优越的预测性能。

## 摘要（原文）

> Large-scale, cross-species plant distribution prediction plays a crucial role in biodiversity conservation, yet modeling efforts in this area still face significant challenges due to the sparsity and bias of observational data. Presence-Absence (PA) data provide accurate and noise-free labels, but are costly to obtain and limited in quantity; Presence-Only (PO) data, by contrast, offer broad spatial coverage and rich spatiotemporal distribution, but suffer from severe label noise in negative samples. To address these real-world constraints, this paper proposes a multimodal fusion framework that fully leverages the strengths of both PA and PO data. We introduce an innovative pseudo-label aggregation strategy for PO data based on the geographic coverage of satellite imagery, enabling geographic alignment between the label space and remote sensing feature space. In terms of model architecture, we adopt Swin Transformer Base as the backbone for satellite imagery, utilize the TabM network for tabular feature extraction, retain the Temporal Swin Transformer for time-series modeling, and employ a stackable serial tri-modal cross-attention mechanism to optimize the fusion of heterogeneous modalities. Furthermore, empirical analysis reveals significant geographic distribution shifts between PA training and test samples, and models trained by directly mixing PO and PA data tend to experience performance degradation due to label noise in PO data. To address this, we draw on the mixture-of-experts paradigm: test samples are partitioned according to their spatial proximity to PA samples, and different models trained on distinct datasets are used for inference and post-processing within each partition. Experiments on the GeoLifeCLEF 2025 dataset demonstrate that our approach achieves superior predictive performance in scenarios with limited PA coverage and pronounced distribution shifts.

