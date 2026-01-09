---
layout: default
title: FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts
---

# FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts
**arXiv**：[2601.05174v1](https://arxiv.org/abs/2601.05174) · [PDF](https://arxiv.org/pdf/2601.05174.pdf)  
**作者**：Yiji Zhao, Zihao Zhong, Ao Wang, Haomin Wen, Ming Jin, Yuxuan Liang, Huaiyu Wan, Hao Wu  

**一句话要点**：提出FaST框架，基于异构感知专家混合实现大规模时空图的长时预测

**关键词**：时空图预测, 长时预测, 专家混合, 计算效率, 大规模图

## 3 点简述
- 针对大规模时空图长时预测的计算成本高和内存消耗大问题
- 采用自适应图代理注意力机制和并行专家混合模块提升效率
- 实验显示在真实数据集上优于现有方法，支持一周预测

## 摘要（原文）

> Spatial-Temporal Graph (STG) forecasting on large-scale networks has garnered significant attention. However, existing models predominantly focus on short-horizon predictions and suffer from notorious computational costs and memory consumption when scaling to long-horizon predictions and large graphs. Targeting the above challenges, we present FaST, an effective and efficient framework based on heterogeneity-aware Mixture-of-Experts (MoEs) for long-horizon and large-scale STG forecasting, which unlocks one-week-ahead (672 steps at a 15-minute granularity) prediction with thousands of nodes. FaST is underpinned by two key innovations. First, an adaptive graph agent attention mechanism is proposed to alleviate the computational burden inherent in conventional graph convolution and self-attention modules when applied to large-scale graphs. Second, we propose a new parallel MoE module that replaces traditional feed-forward networks with Gated Linear Units (GLUs), enabling an efficient and scalable parallel structure. Extensive experiments on real-world datasets demonstrate that FaST not only delivers superior long-horizon predictive accuracy but also achieves remarkable computational efficiency compared to state-of-the-art baselines. Our source code is available at: https://github.com/yijizhao/FaST.

