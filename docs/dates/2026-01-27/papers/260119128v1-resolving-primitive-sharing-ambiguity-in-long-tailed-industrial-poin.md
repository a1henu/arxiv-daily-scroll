---
layout: default
title: Resolving Primitive-Sharing Ambiguity in Long-Tailed Industrial Point Cloud Segmentation via Spatial Context Constraints
---

# Resolving Primitive-Sharing Ambiguity in Long-Tailed Industrial Point Cloud Segmentation via Spatial Context Constraints
**arXiv**：[2601.19128v1](https://arxiv.org/abs/2601.19128) · [PDF](https://arxiv.org/pdf/2601.19128.pdf)  
**作者**：Chao Yin, Qing Han, Zhiwei Hou, Yue Liu, Anjin Dai, Hongda Hu, Ji Yang, Wei Yao  

**一句话要点**：提出空间上下文约束方法，解决工业点云分割中长尾分布与几何歧义问题。

**关键词**：工业点云分割, 长尾分布, 几何歧义, 空间上下文约束, 类平衡损失, 数字孪生

## 3 点简述
- 核心问题：工业点云分割中，安全关键组件因长尾分布和几何歧义被误分类。
- 方法要点：基于类平衡损失框架，引入边界和密度约束模块，无需修改网络结构。
- 实验效果：在Industrial3D数据集上，尾类性能提升21.7%，关键组件IoU显著改善。

## 摘要（原文）

> Industrial point cloud segmentation for Digital Twin construction faces a persistent challenge: safety-critical components such as reducers and valves are systematically misclassified. These failures stem from two compounding factors: such components are rare in training data, yet they share identical local geometry with dominant structures like pipes. This work identifies a dual crisis unique to industrial 3D data extreme class imbalance 215:1 ratio compounded by geometric ambiguity where most tail classes share cylindrical primitives with head classes. Existing frequency-based re-weighting methods address statistical imbalance but cannot resolve geometric ambiguity. We propose spatial context constraints that leverage neighborhood prediction consistency to disambiguate locally similar structures. Our approach extends the Class-Balanced (CB) Loss framework with two architecture-agnostic mechanisms: (1) Boundary-CB, an entropy-based constraint that emphasizes ambiguous boundaries, and (2) Density-CB, a density-based constraint that compensates for scan-dependent variations. Both integrate as plug-and-play modules without network modifications, requiring only loss function replacement. On the Industrial3D dataset (610M points from water treatment facilities), our method achieves 55.74% mIoU with 21.7% relative improvement on tail-class performance (29.59% vs. 24.32% baseline) while preserving head-class accuracy (88.14%). Components with primitive-sharing ambiguity show dramatic gains: reducer improves from 0% to 21.12% IoU; valve improves by 24.3% relative. This resolves geometric ambiguity without the typical head-tail trade-off, enabling reliable identification of safety-critical components for automated knowledge extraction in Digital Twin applications.

