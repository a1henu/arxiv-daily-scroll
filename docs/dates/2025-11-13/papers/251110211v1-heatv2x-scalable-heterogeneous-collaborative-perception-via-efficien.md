---
layout: default
title: HeatV2X: Scalable Heterogeneous Collaborative Perception via Efficient Alignment and Interaction
---

# HeatV2X: Scalable Heterogeneous Collaborative Perception via Efficient Alignment and Interaction
**arXiv**：[2511.10211v1](https://arxiv.org/abs/2511.10211) · [PDF](https://arxiv.org/pdf/2511.10211.pdf)  
**作者**：Yueran Zhao, Zhang Zhang, Chao Sun, Tianze Wang, Chao Yue, Nuoran Li  

**一句话要点**：提出HeatV2X框架以解决V2X异构协作感知的可扩展性问题

**关键词**：V2X协作感知, 异构特征对齐, 可扩展框架, 图注意力网络, 微调方法

## 3 点简述
- 核心问题：V2X协作感知中多模态异构性和可扩展性挑战，导致特征对齐困难和训练成本高。
- 方法要点：使用异构图注意力训练基础代理，并通过局部和全局微调实现高效对齐与交互。
- 实验或效果：在OPV2V-H和DAIR-V2X数据集上，性能优于现有方法，显著降低训练开销。

## 摘要（原文）

> Vehicle-to-Everything (V2X) collaborative perception extends sensing beyond single vehicle limits through transmission. However, as more agents participate, existing frameworks face two key challenges: (1) the participating agents are inherently multi-modal and heterogeneous, and (2) the collaborative framework must be scalable to accommodate new agents. The former requires effective cross-agent feature alignment to mitigate heterogeneity loss, while the latter renders full-parameter training impractical, highlighting the importance of scalable adaptation. To address these issues, we propose Heterogeneous Adaptation (HeatV2X), a scalable collaborative framework. We first train a high-performance agent based on heterogeneous graph attention as the foundation for collaborative learning. Then, we design Local Heterogeneous Fine-Tuning and Global Collaborative Fine-Tuning to achieve effective alignment and interaction among heterogeneous agents. The former efficiently extracts modality-specific differences using Hetero-Aware Adapters, while the latter employs the Multi-Cognitive Adapter to enhance cross-agent collaboration and fully exploit the fusion potential. These designs enable substantial performance improvement of the collaborative framework with minimal training cost. We evaluate our approach on the OPV2V-H and DAIR-V2X datasets. Experimental results demonstrate that our method achieves superior perception performance with significantly reduced training overhead, outperforming existing state-of-the-art approaches. Our implementation will be released soon.

