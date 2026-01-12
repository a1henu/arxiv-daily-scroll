---
layout: default
title: Adaptive Disentangled Representation Learning for Incomplete Multi-View Multi-Label Classification
---

# Adaptive Disentangled Representation Learning for Incomplete Multi-View Multi-Label Classification
**arXiv**：[2601.05785v1](https://arxiv.org/abs/2601.05785) · [PDF](https://arxiv.org/pdf/2601.05785.pdf)  
**作者**：Quanjiang Li, Zhiming Liu, Tianxiang Xu, Tingjin Luo, Chenping Hou  

**一句话要点**：提出自适应解耦表示学习方法以解决多视图多标签分类中的特征缺失与标注不完整问题

**关键词**：多视图学习, 多标签分类, 表示解耦, 特征补全, 标签语义建模, 自适应学习

## 3 点简述
- 核心问题：多视图多标签学习常面临特征缺失和标注不完整，现有方法在特征恢复、表示解耦和标签语义建模方面存在局限
- 方法要点：通过邻域感知跨模态特征传播和随机掩码策略实现鲁棒视图补全，利用类别级关联优化标签原型，并基于互信息目标促进共享表示一致性
- 实验或效果：在公共数据集和实际应用中验证了ADRL的优越性能，通过原型特定特征选择和伪标签引导的视图融合提升分类效果

## 摘要（原文）

> Multi-view multi-label learning frequently suffers from simultaneous feature absence and incomplete annotations, due to challenges in data acquisition and cost-intensive supervision. To tackle the complex yet highly practical problem while overcoming the existing limitations of feature recovery, representation disentanglement, and label semantics modeling, we propose an Adaptive Disentangled Representation Learning method (ADRL). ADRL achieves robust view completion by propagating feature-level affinity across modalities with neighborhood awareness, and reinforces reconstruction effectiveness by leveraging a stochastic masking strategy. Through disseminating category-level association across label distributions, ADRL refines distribution parameters for capturing interdependent label prototypes. Besides, we formulate a mutual-information-based objective to promote consistency among shared representations and suppress information overlap between view-specific representation and other modalities. Theoretically, we derive the tractable bounds to train the dual-channel network. Moreover, ADRL performs prototype-specific feature selection by enabling independent interactions between label embeddings and view representations, accompanied by the generation of pseudo-labels for each category. The structural characteristics of the pseudo-label space are then exploited to guide a discriminative trade-off during view fusion. Finally, extensive experiments on public datasets and real-world applications demonstrate the superior performance of ADRL.

