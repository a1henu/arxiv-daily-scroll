---
layout: default
title: The Geometry of Transfer: Unlocking Medical Vision Manifolds for Training-Free Model Ranking
---

# The Geometry of Transfer: Unlocking Medical Vision Manifolds for Training-Free Model Ranking
**arXiv**：[2602.23916v1](https://arxiv.org/abs/2602.23916) · [PDF](https://arxiv.org/pdf/2602.23916.pdf)  
**作者**：Jiaqi Tang, Shaoyang Zhang, Xiaoqi Wang, Jiaying Zhou, Yang Liu, Qingchao Chen  

**一句话要点**：提出拓扑驱动可迁移性估计框架，以无训练方式解决医学分割任务中基础模型选择问题。

**关键词**：医学视觉, 可迁移性估计, 拓扑分析, 密集预测, 无训练模型选择, 基础模型

## 3 点简述
- 核心问题：现有可迁移性估计指标基于全局统计假设，难以捕捉密集预测所需的拓扑复杂性，导致医学分割模型选择效率低。
- 方法要点：引入全局表示拓扑差异和局部边界感知拓扑一致性，通过任务自适应融合评估流形可处理性。
- 实验或效果：在OpenMind基准测试中，加权Kendall相对提升约31%，显著优于现有基线，无需微调即可高效选择模型。

## 摘要（原文）

> The advent of large-scale self-supervised learning (SSL) has produced a vast zoo of medical foundation models. However, selecting optimal medical foundation models for specific segmentation tasks remains a computational bottleneck. Existing Transferability Estimation (TE) metrics, primarily designed for classification, rely on global statistical assumptions and fail to capture the topological complexity essential for dense prediction. We propose a novel Topology-Driven Transferability Estimation framework that evaluates manifold tractability rather than statistical overlap. Our approach introduces three components: (1) Global Representation Topology Divergence (GRTD), utilizing Minimum Spanning Trees to quantify feature-label structural isomorphism; (2) Local Boundary-Aware Topological Consistency (LBTC), which assesses manifold separability specifically at critical anatomical boundaries; and (3) Task-Adaptive Fusion, which dynamically integrates global and local metrics based on the semantic cardinality of the target task. Validated on the large-scale OpenMind benchmark across diverse anatomical targets and SSL foundation models, our approach significantly outperforms state-of-the-art baselines by around \textbf{31\%} relative improvement in the weighted Kendall, providing a robust, training-free proxy for efficient model selection without the cost of fine-tuning. The code will be made publicly available upon acceptance.

