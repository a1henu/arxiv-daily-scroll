---
layout: default
title: FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts
---

# FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts
**arXiv**：[2601.05174v1](https://arxiv.org/abs/2601.05174) · [PDF](https://arxiv.org/pdf/2601.05174.pdf)  
**作者**：Yiji Zhao, Zihao Zhong, Ao Wang, Haomin Wen, Ming Jin, Yuxuan Liang, Huaiyu Wan, Hao Wu  

**一句话要点**：提出FaST框架，基于异构感知混合专家模型，实现大规模时空图的长时预测与高效计算。

**关键词**：时空图预测, 长时预测, 混合专家模型, 计算效率, 大规模图

## 3 点简述
- 核心问题：现有模型在大规模时空图上进行长时预测时计算成本高、内存消耗大。
- 方法要点：采用自适应图代理注意力机制和并行混合专家模块，提升计算效率。
- 实验或效果：在真实数据集上验证了FaST在长时预测精度和计算效率上的优越性。

## 摘要（原文）

> Spatial-Temporal Graph (STG) forecasting on large-scale networks has garnered significant attention. However, existing models predominantly focus on short-horizon predictions and suffer from notorious computational costs and memory consumption when scaling to long-horizon predictions and large graphs. Targeting the above challenges, we present FaST, an effective and efficient framework based on heterogeneity-aware Mixture-of-Experts (MoEs) for long-horizon and large-scale STG forecasting, which unlocks one-week-ahead (672 steps at a 15-minute granularity) prediction with thousands of nodes. FaST is underpinned by two key innovations. First, an adaptive graph agent attention mechanism is proposed to alleviate the computational burden inherent in conventional graph convolution and self-attention modules when applied to large-scale graphs. Second, we propose a new parallel MoE module that replaces traditional feed-forward networks with Gated Linear Units (GLUs), enabling an efficient and scalable parallel structure. Extensive experiments on real-world datasets demonstrate that FaST not only delivers superior long-horizon predictive accuracy but also achieves remarkable computational efficiency compared to state-of-the-art baselines. Our source code is available at: https://github.com/yijizhao/FaST.

