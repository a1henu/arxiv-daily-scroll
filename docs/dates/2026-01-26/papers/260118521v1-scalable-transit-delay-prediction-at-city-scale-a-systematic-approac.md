---
layout: default
title: Scalable Transit Delay Prediction at City Scale: A Systematic Approach with Multi-Resolution Feature Engineering and Deep Learning
---

# Scalable Transit Delay Prediction at City Scale: A Systematic Approach with Multi-Resolution Feature Engineering and Deep Learning
**arXiv**：[2601.18521v1](https://arxiv.org/abs/2601.18521) · [PDF](https://arxiv.org/pdf/2601.18521.pdf)  
**作者**：Emna Boudabbous, Mohamed Karaa, Lokman Sboui, Julio Montecinos, Omar Alam  

**一句话要点**：提出结合多分辨率特征工程与深度学习的城市级公交延误预测框架，以解决可扩展性问题。

**关键词**：公交延误预测, 多分辨率特征工程, 深度学习, 城市级可扩展性, 自适应PCA, 混合聚类

## 3 点简述
- 核心问题：现有公交延误预测系统规模有限，依赖手工特征，缺乏可扩展架构。
- 方法要点：通过多分辨率特征工程生成1683个时空特征，使用自适应PCA压缩，并引入混合聚类方法优化训练。
- 实验或效果：在蒙特利尔公交网络上验证，全局LSTM模型在准确性与效率间取得最佳平衡，优于Transformer模型。

## 摘要（原文）

> Urban bus transit agencies need reliable, network-wide delay predictions to provide accurate arrival information to passengers and support real-time operational control. Accurate predictions help passengers plan their trips, reduce waiting time, and allow operations staff to adjust headways, dispatch extra vehicles, and manage disruptions. Although real-time feeds such as GTFS-Realtime (GTFS-RT) are now widely available, most existing delay prediction systems handle only a few routes, depend on hand-crafted features, and offer little guidance on how to design a scalable, reusable architecture.
>   We present a city-scale prediction pipeline that combines multi-resolution feature engineering, dimensionality reduction, and deep learning. The framework generates 1,683 spatiotemporal features by exploring 23 aggregation combinations over H3 cells, routes, segments, and temporal patterns, and compresses them into 83 components using Adaptive PCA while preserving 95% of the variance. To avoid the "giant cluster" problem that occurs when dense urban areas fall into a single H3 region, we introduce a hybrid H3+topology clustering method that yields 12 balanced route clusters (coefficient of variation 0.608) and enables efficient distributed training.
>   We compare five model architectures on six months of bus operations from the Société de transport de Montréal (STM) network in Montréal. A global LSTM with cluster-aware features achieves the best trade-off between accuracy and efficiency, outperforming transformer models by 18 to 52% while using 275 times fewer parameters. We also report multi-level evaluation at the elementary segment, segment, and trip level with walk-forward validation and latency analysis, showing that the proposed pipeline is suitable for real-time, city-scale deployment and can be reused for other networks with limited adaptation.

