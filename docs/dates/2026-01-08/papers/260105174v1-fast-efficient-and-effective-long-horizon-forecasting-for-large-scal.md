---
layout: default
title: FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts
---

# FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts
**arXiv**：[2601.05174v1](https://arxiv.org/abs/2601.05174) · [PDF](https://arxiv.org/pdf/2601.05174.pdf)  
**作者**：Yiji Zhao, Zihao Zhong, Ao Wang, Haomin Wen, Ming Jin, Yuxuan Liang, Huaiyu Wan, Hao Wu  

**一句话要点**：提出FaST框架，基于异构感知的专家混合模型，解决大规模时空图长时预测的计算效率与准确性挑战。

**关键词**：时空图预测, 长时预测, 专家混合模型, 计算效率, 大规模图, 自适应注意力

## 3 点简述
- 核心问题：现有模型在大规模时空图上进行长时预测时，计算成本高、内存消耗大，难以扩展到一周预测。
- 方法要点：采用自适应图代理注意力机制减轻计算负担，并设计并行专家混合模块替换传统前馈网络，提升效率。
- 实验或效果：在真实数据集上，FaST在长时预测准确性和计算效率方面均优于现有基线，支持数千节点的一周预测。

## 摘要（原文）

> Spatial-Temporal Graph (STG) forecasting on large-scale networks has garnered significant attention. However, existing models predominantly focus on short-horizon predictions and suffer from notorious computational costs and memory consumption when scaling to long-horizon predictions and large graphs. Targeting the above challenges, we present FaST, an effective and efficient framework based on heterogeneity-aware Mixture-of-Experts (MoEs) for long-horizon and large-scale STG forecasting, which unlocks one-week-ahead (672 steps at a 15-minute granularity) prediction with thousands of nodes. FaST is underpinned by two key innovations. First, an adaptive graph agent attention mechanism is proposed to alleviate the computational burden inherent in conventional graph convolution and self-attention modules when applied to large-scale graphs. Second, we propose a new parallel MoE module that replaces traditional feed-forward networks with Gated Linear Units (GLUs), enabling an efficient and scalable parallel structure. Extensive experiments on real-world datasets demonstrate that FaST not only delivers superior long-horizon predictive accuracy but also achieves remarkable computational efficiency compared to state-of-the-art baselines. Our source code is available at: https://github.com/yijizhao/FaST.

