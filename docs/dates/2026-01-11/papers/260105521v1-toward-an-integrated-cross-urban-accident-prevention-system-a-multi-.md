---
layout: default
title: Toward an Integrated Cross-Urban Accident Prevention System: A Multi-Task Spatial-Temporal Learning Framework for Urban Safety Management
---

# Toward an Integrated Cross-Urban Accident Prevention System: A Multi-Task Spatial-Temporal Learning Framework for Urban Safety Management
**arXiv**：[2601.05521v1](https://arxiv.org/abs/2601.05521) · [PDF](https://arxiv.org/pdf/2601.05521.pdf)  
**作者**：Jiayu Fang, Zhiqi Shao, Haoning Xi, Boris Choy, Junbin Gao  

**一句话要点**：提出MLA-STNet多任务时空学习框架，以解决跨城市事故预测中的异质性与数据噪声问题。

**关键词**：跨城市事故预测, 多任务学习, 时空网络, 异质性处理, 噪声鲁棒性

## 3 点简述
- 核心问题：城市事故数据存在异质性、不一致报告及噪声，阻碍跨城市统一预防系统开发。
- 方法要点：集成STG-MA模块抑制时空波动，STS-MA模块通过共享参数设计缓解跨城市异质性。
- 实验或效果：在纽约和芝加哥数据集上，MLA-STNet相比基线降低RMSE达6%，提升Recall达8%，并在噪声下保持稳定性能。

## 摘要（原文）

> The development of a cross-city accident prevention system is particularly challenging due to the heterogeneity, inconsistent reporting, and inherently clustered, sparse, cyclical, and noisy nature of urban accident data. These intrinsic data properties, combined with fragmented governance and incompatible reporting standards, have long hindered the creation of an integrated, cross-city accident prevention framework. To address this gap, we propose the Mamba Local-ttention Spatial-Temporal Network MLA-STNet, a unified system that formulates accident risk prediction as a multi-task learning problem across multiple cities. MLA-STNet integrates two complementary modules: (i)the Spatio-Temporal Geographical Mamba-Attention (STG-MA), which suppresses unstable spatio-temporal fluctuations and strengthens long-range temporal dependencies; and (ii) the Spatio-Temporal Semantic Mamba-Attention (STS-MA), which mitigates cross-city heterogeneity through a shared-parameter design that jointly trains all cities while preserving individual semantic representation spaces. We validate the proposed framework through 75 experiments under two forecasting scenarios, full-day and high-frequency accident periods, using real-world datasets from New York City and Chicago. Compared with the state-of-the-art baselines, MLA-STNet achieves up to 6% lower RMSE, 8% higher Recall, and 5% higher MAP, while maintaining less than 1% performance variation under 50% input noise. These results demonstrate that MLA-STNet effectively unifies heterogeneous urban datasets within a scalable, robust, and interpretable Cross-City Accident Prevention System, paving the way for coordinated and data-driven urban safety management.

